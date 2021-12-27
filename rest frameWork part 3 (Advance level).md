## we don't need Mixing here
### we already have: ListCreateAPIView, RetrieveUpdateDestroyAPIView --> classes
See official doc of django REST frame work: https://www.django-rest-framework.org/api-guide/generic-views/#updatemodelmixin

<hr>
see : rest frame work part 4 for the crud application using router and viewsets (only one view needed)
<hr>

```
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

class List_Create_APIView(ListCreateAPIView): # will work for GET and POST Request
      queryset= Status.objects.all() # grab all data from 'Status' table
      # 'queryset' : defines, on which model/table we are doing query and collecting obj
      
      # Now, mention the serializer class, that we are using to serialize the the object.
      serializer_class= StatusSerializer # StatusSerializer is the class we made in serializer.py to serialize the object
      
class Details_Update_Delete_APIView(RetrieveUpdateDestroyAPIView): # will work for details, Update and delete Request
      queryset= Status.objects.all() # grab all data from 'Status' table
      # 'queryset' : defines, on which model/table we are doing query and collecting obj
      
      # Now, mention the serializer class, that we are using to serialize the the object.
      serializer_class= StatusSerializer # StatusSerializer is the class we made in serializer.py to serialize the object
      lookup_field= 'id' # need to match with urls.py file's accepting key value variable
      # By lookup_field--> we are mentioning, which field it will look for the matching and send response
      
############ (advance)  Without  using the Mixin (END)

```

## Now we can use url:
```
from . import views

urlpatterns = [
    path('status/', views.List_Create_APIView.as_view()),
    path('status/<id>', views.Details_Update_Delete_APIView.as_view()),
]

```
# work done. using only two simple classbased view, we can handle crud operation by RestAPI
urls for post and create: http://127.0.0.1:8000/apiV1/status/
urls for detaills, update, delete: http://127.0.0.1:8000/apiV1/status/9