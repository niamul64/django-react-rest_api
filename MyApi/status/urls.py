

from django.urls import path, include
from . import views

urlpatterns = [
    path('status/', views.Status_ListView_and_CreateView.as_view()),
    path('status/<id>', views.Status_Details_Update_Delete_view_api.as_view()),
]
