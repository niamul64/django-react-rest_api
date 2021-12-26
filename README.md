# django-react-rest_api (Here, in this file refarence to a file --> see: 'file_name' )
### By django_rest framework, create rest API. after creating rest api, will able to use it with any frontend application.

### 1. first create virtual environment 'env1' (see: 'virtual env.md')
### 2. Now install django==3.2.8
### 3. install packages for rest framework (see: 'rest framework.md')
### 4. Now create a django project
### 5. create django project ($ django-admin startproject [project_name]): django-admin startproject MyApi
### 6. Now, enter inside the django project file. and start a app ($ py manage.py startapp [app_name]):py manage.py startapp status
### 7. Now, goto settings.py and do all initial for project-> (see: Django-Backend(repo)-> 'initial setup for project')
### 8. Create database model classes,  see: 'django-backend' reposetory --> 'django model.md'.
### 9. register models in admin panel: (run migrate, makemigrations--> before this) 
### 10. createsuperuser (py manage.py createsuperuser): username: niamul, pass: 1
### 11. creating admin panel serialization on admin panel( see: 'admin panel serializer.md') (optional)

<hr>

### version 1:
## RESPONSE (get request): REST API serializer--> see (json--> python obj , python obj--> jeson)
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
### version1: using the basic and simplest view 'APIView', and get method.
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

### TEST the RESPONSE by HTML JS frontend (see:'TEST the RESPONSE by HTML JS.md' folder of this repo. )


## version2: use list to make views: (less code than version1)  
## from here--> see: 'rest framework.md' file, in this reposetory

