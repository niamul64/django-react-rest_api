
from django.db.models import query
from django.db.models.query import QuerySet
from django.views import generic
from rest_framework import parsers
from status.models import Status          # model
from .serializers import StatusSerializer # serializer based on Status model

from rest_framework.views import APIView     # jeson data handeling
from rest_framework.response import Response # handeling response
from rest_framework.generics import ListAPIView,CreateAPIView ,RetrieveAPIView,UpdateAPIView,DestroyAPIView
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin ,DestroyModelMixin
from rest_framework.parsers import FormParser, MultiPartParser
# Create your views here.

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


from rest_framework.viewsets import ModelViewSet

# we can do the CRUD operation by only usinf this one function with viewsets (Start)
class CRUDViewSets(ModelViewSet): # ModelViewSet will help: to set CRUD operation on the model table we are defining here
      
      queryset= Status.objects.all() # grab all data from 'Status' table
      # 'queryset' : defines, on which model/table we are doing query and collecting obj
      
      # Now, mention the serializer class, that we are using to serialize the the object.
      serializer_class= StatusSerializer # StatusSerializer is the class we made in serializer.py to serialize the object
      
      # parser class for image upload: as we are having img field
      parser_classes=[parsers.FormParser,parsers.MultiPartParser]
# we can do the CRUD operation by only usinf this one function with viewsets (End)






############ (advance)  Without  using the Mixin
class List_Create_APIView(ListCreateAPIView): # will work for GET and POST Request
      queryset= Status.objects.all() # grab all data from 'Status' table
      # 'queryset' : defines, on which model/table we are doing query and collecting obj
      
      # Now, mention the serializer class, that we are using to serialize the the object.
      serializer_class= StatusSerializer # StatusSerializer is the class we made in serializer.py to serialize the object
      
      # parser class for image upload:
      parser_classes=[parsers.FormParser,parsers.MultiPartParser]
      
      
class Details_Update_Delete_APIView(RetrieveUpdateDestroyAPIView): 
      queryset= Status.objects.all() # grab all data from 'Status' table
      # 'queryset' : defines, on which model/table we are doing query and collecting obj
      
      # Now, mention the serializer class, that we are using to serialize the the object.
      serializer_class= StatusSerializer # StatusSerializer is the class we made in serializer.py to serialize the object
      lookup_field= 'id' # need to match with urls.py file's accepting key value variable
      # By lookup_field--> we are mentioning, which field it will look for the matching and send response
      
      # parser class for image upload:
      parser_classes=[parsers.FormParser,parsers.MultiPartParser]
      
############ (advance)  Without  using the Mixin (END)



#### using Mixin
class Status_ListView_and_CreateView(CreateModelMixin, ListAPIView): 
      queryset= Status.objects.all() # grab all data from 'Status' table
      # 'queryset' : defines, on which model/table we are doing query and collecting obj
      
      # Now, mention the serializer class, that we are using to serialize the the object.
      serializer_class= StatusSerializer # StatusSerializer is the class we made in serializer.py to serialize the object
      
      def post(self, request, *args, **kwargs): # this fuction will anable the Create request(Post)
            return self.create(request,  *args, **kwargs)


class Status_Details_Update_Delete_view_api(RetrieveAPIView): # hendle get request to show detail of a particular obj, of a model table 
      queryset = Status.objects.all() # from which table we want to show the data.
      serializer_class = StatusSerializer # StatusSerializer is the class we made in serializer.py to serialize the object
      lookup_field= 'id' # need to match with urls.py file's accepting key value variable

      def put(self, request, *args, **kwargs): # this fuction will anable the update request(PUT)
            return self.update(request,  *args, **kwargs) #if we want PATCH request the. partial_update()
      
      def delete(self, request, *args, **kwargs): # this fuction will anable the delete request(delete)
            return self.destroy(request,  *args, **kwargs)     

#### using Mixin END




# its a built in class based view to handel response and serve data as json. (provided by django restFramework)
class StatusAPIView(APIView): 
      def get(self,request, format=None): # handels get request
            status_list= Status.objects.all() # grab all data from 'Status' table from database
            # Now convert and store as json(python-> json)
            statusSerializer = StatusSerializer(status_list, many=True) # now passing all data to our serializer, by many=True we are saying that multiple instance are allowed.
            return Response(statusSerializer.data) # by 'statusSerializer.data' saying that, serve data as json format 

class StatusListApiView(ListAPIView): # will do the same work(like: StatusAPIView(APIView)) with only two lines of code
      queryset= Status.objects.all() # grab all data from 'Status' table
      # 'queryset' : defines, on which model/table we are doing query and collecting obj
      
      # Now, mention the serializer class, that we are using to serialize the the object.
      serializer_class= StatusSerializer # StatusSerializer is the class we made in serializer.py to serialize the object
      
      # rest of the things will be handeled by the class Automatically
      
class StatusCreateApiView(CreateAPIView): # handle POST request
      # we can insert data in model table by creating this API
      queryset = Status.objects.all() # at which table we want to insert the data.
      serializer_class = StatusSerializer # StatusSerializer is the class we made in serializer.py to serialize the object

      
      
class StatusDetailAPIView(RetrieveAPIView): # hendle get request to show detail of a particular obj, of a model table 
      queryset = Status.objects.all() # from which table we want to show the data.
      serializer_class = StatusSerializer # StatusSerializer is the class we made in serializer.py to serialize the object
      lookup_field= 'id' # need to match with urls.py file's accepting key value variable

      # By lookup_field--> we are mentioning, which field it will look for the matching and send response
      # def get_object(self, *args, **kwargs): # args= arguments, **kwargs=keyword-arguments
      #       kwargs= self.kwargs # let's save the kwargs in a variable(like: id), we are getting the keyvalue by 'kwargs'
      #       # The key value comming as dictionary (like this: {'id': '1'} )
      #       kw_id= kwargs.get('id') # geting the value of 'id' form dictionary
      #       return Status.objects.get(id= kw_id) #using id to search details, based on the url request 'id'
      #       # Status is the model class
            
      #       #print(kwargs) # printing on terminal
      # ## if we print kwargs--> see in terminal:
      # # {'id': '1'} # means we are receiving the id value, which we are sending through url patern:(http://127.0.0.1:8000/apiV1/status_Details/1)
      # # if we change the variable name in urls.py: (like: 'slag' )
      # # # in the terminal: we will see output: {'slug': '3'}
      # # so, by using 'get_object' method we are flaxible to use any field name in urls.py

      
class StatusUpdateApiView(UpdateAPIView): # handle PUT request
      # we can updating data in model table by creating this API
      queryset = Status.objects.all() # at which table we want to update the data.
      serializer_class = StatusSerializer # StatusSerializer is the class we made in serializer.py to serialize the object
      lookup_field= 'id'
      # we can use this lookup fiel(if we don't use it then primary key will automatically used)
      
class StatusDeleteView(DestroyAPIView): # handle DELETE request
      queryset = Status.objects.all() # at which table we want to delete the data.
      serializer_class = StatusSerializer # StatusSerializer is the class we made in serializer.py to serialize the object
      lookup_field= 'id'
      # we can use this lookup fiel(if we don't use it then primary key will automatically used)