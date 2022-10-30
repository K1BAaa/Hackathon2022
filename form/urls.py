from django.urls import path
from form import views

urlpatterns = [
    path('form/', views.send_questions)
]
