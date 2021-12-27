

from django.urls import path, include
from . import views

urlpatterns = [
    path('status/', views.Status_ListView_and_CreateView.as_view()),
]
