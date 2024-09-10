from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
import json
import base64
import random
import string
from .models import Category, Profile
from django.http import JsonResponse
import cv2
from web.settings import MEDIA_ROOT, BASE_DIR

def index(request, template_name = 'index.html'):
    context = {}
    return render(request, template_name, context)

def upload_display(request, template_name = 'upload-image.html'):
    context = {}
    return render(request, template_name, context)

@csrf_exempt
def save_image(request):
    if request.method == 'POST':
        data = request.body
        data = json.loads(data[0: len(data)])
        c = Category.objects.get(id = 1)
        temp = len('data:image/jpeg;base64,')
        for d in data:
            d = d[temp: len(d)]
            imgdata = base64.b64decode(d)            
            filename_end = str(datetime.now().strftime('%Y%m%d-%H-%M-%S'))
            filename = randomString() + '-' + filename_end + '.jpg'            
            
            with open('media/' + filename, 'wb') as f:
                f.write(imgdata)
                
                file_location = 'media/' + str(filename)
                image = cv2.imread(file_location)

                # Convert to grayscale
                gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

                # Initialize the face detector                
                face_classifier = cv2.CascadeClassifier(BASE_DIR / 'ml/haarcascade_frontalface_default.xml')

                # Detect the face in the image
                faces = face_classifier.detectMultiScale(gray_image)

                if(len(faces) == 0):
                    print('Do not save data at all....')                    
                    return redirect('web_app:index')
                    
                else:
                    # Print number the face detected
                    print(f'{len(faces)} faces detected in the image')
                    
                    # Draw a blue rectangle over every face
                    for x, y, width, height in faces:
                        cv2.rectangle(image, (x, y), (x + width, y + height), color = (255,0, 0), thickness = 1)

                    # Save the new image with rectangles drawn
                    cv2.imwrite('media/dataset/' + str(filename), image)

            profile = Profile.objects.create(category = c, avatar = filename)
            profile.save()
        return JsonResponse({
            'data' : 'Success'
        })
    return redirect('/')


def randomString(stringLength = 5):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))