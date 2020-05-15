from sender import views
from django.urls import path

app_name = 'sender'

urlpatterns = [
    path('', views.EmailSenderCreate.as_view(), name='email_create'),
    path('list/', views.EmailSenderList.as_view(), name="list"),
    path('update/', views.update_status, name="update_status"),
]
