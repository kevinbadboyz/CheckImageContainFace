from django.urls import path
# from .views import (
   
# )
from web_app import views
app_name = 'web_app'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('upload-display', views.upload_display, name = 'upload_display'),
    path('save-image', views.save_image, name = 'save_image'),
]

