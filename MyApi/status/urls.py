

from django.urls import path, include

from .views import CRUDViewSets           ##### Import the viewsets class first
from rest_framework import routers        ##### For seting the route of crud application URLS(for viewsets) 
#### router sets the link for our REST_Apis autometically: ## 'status/' or 'status/<id>/'

# to use router, we need a variable
router = routers.DefaultRouter() # creating router obj, that creates urls for our api
router.register(r'status', CRUDViewSets, basename='status') 
# here router need to be registered, 'status' is the root link, we can give any name here
# so link is now localhost/apiV1/status
# 'CRUDViewSets' is the class based views using viewsets at views.py
# 'r' just needed, no explanation

########## Now we will get the router URLs in router.urls 
########## wchih need to add with 'urlpatterns' list

urlpatterns = [
    # path('status/', views.List_Create_APIView.as_view()),
    # path('status/<id>', views.Details_Update_Delete_APIView.as_view()),
]+ router.urls
