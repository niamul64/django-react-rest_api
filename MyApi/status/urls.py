

from django.urls import path, include
from . import views

urlpatterns = [

    path('status/', views.StatusAPIView.as_view(),name="status"),
    path('status_list/', views.StatusListApiView.as_view(),name="status_list"),
    path('status_create/', views.StatusCreateApiView.as_view(),name="status_create"),
    path('status_details/<id>', views.StatusDetailAPIView.as_view(),name="status_details"),
    path('status_Update/<id>', views.StatusUpdateApiView.as_view(),name="status_Update"),
    path('status_Delete/<id>', views.StatusDeleteView.as_view(),name="status_Delete"),
]
