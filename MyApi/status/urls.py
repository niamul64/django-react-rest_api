

from django.urls import path, include
from . import views

urlpatterns = [
    path('status/', views.List_Create_APIView.as_view()),
    path('status/<id>', views.Details_Update_Delete_APIView.as_view()),
]
