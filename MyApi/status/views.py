
from django.db.models import query
from django.db.models.query import QuerySet
from status.models import Status          # model
from .serializers import StatusSerializer # serializer based on Status model

from rest_framework.views import APIView     # jeson data handeling
from rest_framework.response import Response # handeling response
from rest_framework.generics import ListAPIView,CreateAPIView 

# Create your views here.


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
      queryset = Status.objects.all() # at which tablie we want to insert the data.
      serializer_class = StatusSerializer # StatusSerializer is the class we made in serializer.py to serialize the object
      
      
      