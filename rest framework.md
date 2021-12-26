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
      queryset = Status.objects.all() # at which table we want to insert the data.
      serializer_class = StatusSerializer # StatusSerializer is the class we made in serializer.py to serialize the object
```
3. Now, urls.py
```
path('status_create/', views.StatusCreateApiView.as_view(),name="status_create"),
```
4. Now, if we goto the browser and use url: http://127.0.0.1:8000/apiV1/status_create/

<img src="Test API RESPONSE BY HTML JS/CreateViewAPI.JPG" alt="alt" width="100%">

### TEST the RESPONSE by HTML JS frontend (see:'TEST the RESPONSE by HTML JS.md' folder of this repo. 'for version2')


 ## version3: RetrieveAPIView -->see the detail of an particular obj. 
 #### Here important point is--> we have to accept a primary key through urls.py file
 1. Goto views.py, import and write class view:
```
from rest_framework.generics import RetrieveAPIView # RetrieveAPIView --> details view API--> show details of an obj

class StatusDetailAPIView(RetrieveAPIView): # hendle get request to show detail of a particular obj, of a model table 
      queryset = Status.objects.all() # from which table we want to show the data.
      serializer_class = StatusSerializer # StatusSerializer is the class we made in serializer.py to serialize the object
```
2. urls.py: Here important point is-->we have to accept a primary key through urls.py file
```
path('status_Details/<pk>', views.StatusDetailAPIView.as_view(),name="status_Details"),
```
3. Now, if we goto the browser and use url: http://127.0.0.1:8000/apiV1/status_Details/1
It will send a get request to see the details of primary key=1
<img src="Test API RESPONSE BY HTML JS/details view api browser url.JPG" alt="alt" width="100%">

## version4:( lookup_field ) Now we are using the primary key value to se the details of a obj. 
### But, what if we want to see the details of a object by searching another field, (not primary key field)
1. need to change the 'StatusDetailAPIView(RetrieveAPIView)' view (use: lookup_field)
```
class StatusDetailAPIView(RetrieveAPIView): # hendle get request to show detail of a particular obj, of a model table 
      queryset = Status.objects.all() # from which table we want to show the data.
      serializer_class = StatusSerializer # StatusSerializer is the class we made in serializer.py to serialize the object
      lookup_field= 'id' # need to match with urls.py file's accepting key value variable
```
2. urls.py :
```
path('status_Details/<id>', views.StatusDetailAPIView.as_view(),name="status_Details"), 
# here the receiving key mast be 'id', as in views, I mentioned it as lookup_field 
```
## version5: lookup_field, another approch, using 'get_object' method
1. now at views-> inside 'StatusDetailAPIView(RetrieveAPIView)' class re-write the get_object class:
```
## in urls.py file:
path('status_Details/<slug>', views.StatusDetailAPIView.as_view(),name="status_Details"),

# in views.py
class StatusDetailAPIView(RetrieveAPIView): # hendle get request to show detail of a particular obj, of a model table 
      queryset = Status.objects.all() # from which table we want to show the data.
      serializer_class = StatusSerializer # StatusSerializer is the class we made in serializer.py to serialize the object
      # lookup_field= 'id' # Now we are not using this. we are writing a function
      # By lookup_field--> we are mentioning, which field it will look for the matching and send response

      def get_object(self, *args, **kwargs): # args= arguments, **kwargs=keyword-arguments
            kwargs= self.kwargs # let's save the kwargs in a variable and print
            print(kwargs) # printing on terminal

## we will see in terminal:
# {'id': '1'} 
# means we are receiving the id value by '**kwargs', which we are sending through url patern:(http://127.0.0.1:8000/apiV1/status_Details/1)

```

2. if we change the variable name in urls.py: (like: 'slag' ), in the terminal: we will see output: {'slug': '3'}

```
## in urls.py file:
path('status_Details/<slug>', views.StatusDetailAPIView.as_view(),name="status_Details"),

# in the terminal: we will see output
# output: {'slug': '3'}
```
#### so, by using 'get_object' method we are flaxible to use any field name in urls.py

3. Now, to send response, we need to add more code to the 'get_object' method:
```
# now in urls.py:
path('status_details/<id>', views.StatusDetailAPIView.as_view(),name="status_details"),

# in views.py
class StatusDetailAPIView(RetrieveAPIView): # hendle get request to show detail of a particular obj, of a model table 
      queryset = Status.objects.all() # from which table we want to show the data.
      serializer_class = StatusSerializer # StatusSerializer is the class we made in serializer.py to serialize the object

      def get_object(self, *args, **kwargs): # args= arguments, **kwargs=keyword-arguments
            kwargs= self.kwargs # let's save the kwargs in a variable(like: id), we are getting the keyvalue by 'kwargs'
            # The key value comming as dictionary (like this: {'id': '1'} )
            kw_id= kwargs.get('id') # geting the value of 'id' form dictionary
            return Status.objects.get(id= kw_id) #using id to search details, based on the url request 'id'
            # Status is the model class
```
4. Now, if we use url on browser: http://127.0.0.1:8000/apiV1/status_details/2

<img src="Test API RESPONSE BY HTML JS/using get_object method of detailAPIView.JPG" alt="alt" width="100%">

# But instead of using 'get_object' method, version4: using 'lookup_field' is enough.


## version6:(PUT/patch request) UPDATE API VIEW, almost like create + detail-> togather in action
### put want full object, patch want only the changed obj. (search more about this on google)
1. import and views.py-->
```
from rest_framework.generics import UpdateAPIView

class StatusUpdateApiView(UpdateAPIView): # handle PUT/patch request
      # we can updating data in model table by creating this API
      queryset = Status.objects.all() # at which table we want to update the data.
      serializer_class = StatusSerializer # StatusSerializer is the class we made in serializer.py to serialize the object
      lookup_field= 'id'
      # we can use this lookup fiel(if we don't use it then primary key will automatically used)
```
2. urls.py-->
```
path('status_Update/<id>', views.StatusUpdateApiView.as_view(),name="status_Update"),
```
Now, if we use url : http://127.0.0.1:8000/apiV1/status_Update/2
we can put the value and update the existing values.
<img src="Test API RESPONSE BY HTML JS/UpdateView API from browser.JPG" alt="alt" width="100%">

### TEST the RESPONSE by HTML JS frontend, almost like version2. just we need to send an obj 'id' (see:'TEST the RESPONSE by HTML JS.md' folder of this repo. almost 'for version2')

## version7: DELETE api-->
1. import, views.py
```
from rest_framework.generics import DestroyAPIView

class StatusDeleteView(DestroyAPIView): # handle DELETE request
      queryset = Status.objects.all() # at which table we want to delete the data.
      serializer_class = StatusSerializer # StatusSerializer is the class we made in serializer.py to serialize the object
      lookup_field= 'id'
      # we can use this lookup fiel(if we don't use it then primary key will automatically used)
```
2. urls.py:
```
path('status_Delete/<id>', views.StatusDeleteView.as_view(),name="status_Delete"),
```
Now, if we use url at browser: http://127.0.0.1:8000/apiV1/status_Delete/2
#### the object with id will be deleted from 'Status' model class table , if we click delete button

# TEST the RESPONSE by HTML JS frontend for--> detail, update, delete (see:'TEST the RESPONSE by HTML JS.md' folder of this repo.)