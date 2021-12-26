

from django.urls import path, include
from . import views

urlpatterns = [

    path('status/', views.StatusAPIView.as_view(),name="status"),
    path('status_list/', views.StatusListApiView.as_view(),name="status_list"),
]
