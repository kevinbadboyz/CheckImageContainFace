import cv2

# Load image
test_image = cv2.imread('dataset/talha.jpg')

# Convert to grayscale
gray_image = cv2.cvtColor(test_image, cv2.COLOR_BGR2GRAY)

# Initialize the face detector
face_classifier = cv2.CascadeClassifier()
face_classifier.load(cv2.samples.findFile('ml/haarcascade_frontalface_default.xml'))

# Detect the face in the image
faces = face_classifier.detectMultiScale(gray_image)

# Print number the face detected
print(f'{len(faces)} faces detected in the image')

# Draw a blue rectangle over every face
for x, y, width, height in faces:
    cv2.rectangle(test_image, (x, y), (x + width, y + height), color = (255,0, 0), thickness = 2)

# Save the new image with rectangles drawn
cv2.imwrite('img-detected-1.jpg', test_image)
