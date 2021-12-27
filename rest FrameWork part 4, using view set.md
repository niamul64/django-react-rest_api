#### rest frame work part: for the crud application using router and viewsets (only one view needed)
#### in views.py file, we don't need more than one view for crud operation.
#### there is a one built in class to  to handle the crud application.
<br>

## using viewsets
```
### views.py file:

from rest_framework.viewsets import ModelViewSet   # import view set

# we can do the CRUD operation by only usinf this one function with viewsets (Start)
class CRUDViewSets(ModelViewSet): # ModelViewSet will help: to set CRUD operation on the model table we are defining here
      
      queryset= Status.objects.all() # grab all data from 'Status' table
      # 'queryset' : defines, on which model/table we are doing query and collecting obj
      
      # Now, mention the serializer class, that we are using to serialize the the object.
      serializer_class= StatusSerializer # StatusSerializer is the class we made in serializer.py to serialize the object
      
      # parser class for image upload: as we are having img field
      parser_classes=[parsers.FormParser,parsers.MultiPartParser]
# we can do the CRUD operation by only usinf this one function with viewsets (End)

```
## Now, we need to set urls.py for this viewsets: (it's urls.py file is little bit different)
### we need to call 'router' module from restFramework
```
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
]+ router.urls    #################################################################

```
<br><br><br>

####  Now, if we run the server and  visit (get, create): http://127.0.0.1:8000/apiV1/status/
#### or(delete, update, details):  http://127.0.0.1:8000/apiV1/status/7
### we will get the same result




