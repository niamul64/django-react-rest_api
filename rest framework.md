goto official documentation: https://www.django-rest-framework.org/

#### install 3 packages:
$pip install djangorestframework
$pip install markdown       # Markdown support for the browsable API.
$pip install django-filter $

#### Add 'rest_framework' to your INSTALLED_APPS setting.
```
INSTALLED_APPS = [
    .............other default paths,
	'App_name',
	'App_name',
	.......include all the app names that created,

	'rest_framework', 
]
```
<hr>


# RESPONSE: (get request)
###  REST API serializer--> see (json--> python obj , python obj--> jeson)
#### what is serializer: REST API always handel data in. JSON format. we will have data from a frontend as JSON format.
#### and we need to save the data in database. and if any one wants to see information from database, show as JSON formate.

### step1: Need to create serializer. (it is like forms.py)

1. create a 'serializers.py' file under the extra app(not under the main app) "status"
2. Now, inport rest_framework in this file. (from rest_framework import serializers)
3. import model (Here 'status' is the model)
4. Now, we will create a class:'StatusSerializer' this class will serialize status model data (python-> json) 
```
from django.db.models.base import Model
from rest_framework import fields, serializers
from .models import Status #importing model

class StatusSerializer(serializers.ModelSerializer): # python-> json
      class Meta:
            model= Status                      # which model data it will serialize
            fields= ['user','content','image'] # which fields will be serialized
```


## version1: using the basic and simplest view 'APIView', and get method
### step2: views.py to control or access the serializer class and provide data as json.

1. import: model and model serializer
```
# inside views.py

from status.models import Status          # model
from .serializers import StatusSerializer # serializer based on Status model
```
2. Now, builtin class view-> for json handeling. import:
```
from rest_framework.views import APIView     # jeson data handeling
from rest_framework.response import Response # handeling response
```
3. Now the actual class based view:
```
# its a built in class based view to handel response and serve data as json. (provided by django restFramework)
class StatusAPIView(APIView): 
      
      def get(self,request, format=None): # handels get request
            
            status_list= Status.objects.all() # grab all data from 'Status' table from database
            
            # Now convert and store as json(python-> json)
            statusSerializer = StatusSerializer(status_list, many=True) # now passing all data to our serializer, by many=True we are saying that multiple instance are allowed.
            
            return Response(statusSerializer.data) 
            # by 'statusSerializer.data' saying that, serve data as json format 
```
4. Now, call the view--> declare a url:
```
# goto main urls.py: (have to import include)
path('status/', include('status:urls')),

# Now, at status_app urls.py

from django.urls import path, include
from . import views
urlpatterns = [

    path('api/', views.StatusAPIView.as_view(),name="api"),
]
```
5. Now, run the server.
type the urls formate: http://127.0.0.1:8000/status/api/
we will see:

<img src="Test API RESPONSE BY HTML JS/get response.jpg" alt="alt" width="100%">

### TEST the RESPONSE by HTML JS frontend (see:'TEST the RESPONSE by HTML JS.md' folder of this repo. 'for version1')

## version2: Now, use listAPIView to make views: (less code than version1)
1. Now, lets call our previous api as version1 one and this is version 2. lets, change the urls.py 
```
# in main urls.py:
path('apiV1/', include('status.urls')),

# inside 'status' app--> urls.py
path('status/', views.StatusAPIView.as_view(),name="status"),

``` 

2. Now, for virsion1 request api url will be: localHost/apiV1/status
3. Now, views.py-> we used APIView. it is a general API View.
4. Now, we will use listAPIView. import-->
``` 
# views.py file
from rest_framework.generics import ListAPIView
```
5. class for ListAPIView: 
```
class StatusListApiView(ListAPIView): # will do the same work(like: StatusAPIView(APIView)) with only two lines of code
      queryset= Status.objects.all() # grab all data from 'Status' table
      # 'queryset' : defines, on which model/table we are doing query and collecting obj
      
      # Now, mention the serializer class, that we are using to serialize the the object.
      serializer_class= StatusSerializer # StatusSerializer is the class we made in serializer.py
      
      # rest of the things will be handeled by the class Automatically
```
6. set url path: urls.py:
```
path('status_list/', views.StatusListApiView.as_view(),name="status_list"),
```
7. Now, if use url: Localhost/apiV1/status_list/
8. Then we will get a response.
<img src="Test API RESPONSE BY HTML JS/version2.JPG" alt="alt" width="100%">

### TEST the RESPONSE by HTML JS frontend (see:'TEST the RESPONSE by HTML JS.md' folder of this repo. 'for version2' )

# RESPONSE: (POST request)
## version3: CreateAPIView, we can insert data at table by this API
1. import--> Import in views.py
```
# import in views.py
from rest_framework.generics import CreateAPIView
```
2. Now, actual view at views.py
```
class StatusCreateApiView(CreateAPIView): # handle POST request
      # we can insert data in model table by creating this API
      queryset = Status.objects.all() # at which tablie we want to insert the data.
      serializer_class = StatusSerializer # StatusSerializer is the class we made in serializer.py to serialize the object
```
3. Now, urls.py
```
path('status_create/', views.StatusCreateApiView.as_view(),name="status_create"),
```
4. Now, if we goto the browser and use url: http://127.0.0.1:8000/apiV1/status_create/

<img src="Test API RESPONSE BY HTML JS/CreateViewAPI.JPG" alt="alt" width="100%">

### TEST the RESPONSE by HTML JS frontend (see:'TEST the RESPONSE by HTML JS.md' folder of this repo. 'for version2')

5. 