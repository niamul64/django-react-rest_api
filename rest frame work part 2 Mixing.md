### Part2: of Django rest_Frame_work (Using Mixin: see official doc-> usder generic views)
LINK OF OFFICIAL DOC: https://www.django-rest-framework.org/api-guide/generic-views/#mixins
#### note: if we are using 1 more mixin: we have to use at least on generic class.
### Here we will use Less urls to do all the work. using different urls for every specifi work is not efficient.
### use only two urls to perform all the task.
# we will design as:
```

# if any one requests url -> will access (request)
step1: status/            ->  List(get), Create(post)
step2: status/<id>        -> details(get), delete(delete), update (put/patch)

```


# step1: status/ --> ListViewAPI(get), CreateViewAPI(post)
1. Remove all the views, and urls for these tasks handlers.
2. create a classView and inside views.py
```
from rest_framework.generics import ListAPIView

class Status_ListView_and_CreateView(ListAPIView): 
      queryset= Status.objects.all() # grab all data from 'Status' table
                                     # 'queryset': defines, on which model/table we are doing query and collecting obj
      
                                            # Now, mention the serializer class, that we are using to serialize the the object.
      serializer_class= StatusSerializer    # StatusSerializer is the class we made in serializer.py to serialize the object
```
3. Now, the class we have defined above: is the ClassView to see the list view ONLY. But we can extend the functionalty OF this class to work as create view TOO.
4. Now, use Mixin class: CreateModelMixing. So Need to import from mixing, at views.py
5. inside the class we need to over ride a function called: 'post()' to extend the functionality of this class to work as class createViewAPI.
```
from rest_framework.generics import ListAPIView
from rest_framework.mixins import CreateModelMixin


class Status_ListView_and_CreateView(CreateModelMixin, ListAPIView): 
      queryset= Status.objects.all() # grab all data from 'Status' table
      # 'queryset' : defines, on which model/table we are doing query and collecting obj
      
      # Now, mention the serializer class, that we are using to serialize the the object.
      serializer_class= StatusSerializer # StatusSerializer is the class we made in serializer.py to serialize the object
      
      ## mixing related functions.
      def post(self, request, *args, **kwargs): # This fuction will anable the Create request(Post)
            return self.create(request,  *args, **kwargs)
```
6.urls.py
```
path('status/', views.Status_ListView_and_CreateView.as_view()),
```

## Now we can use url: status/ --> AS->  List(get), Create(post) --> request
<img src="Test API RESPONSE BY HTML JS/GET and POST request using Mixing.JPG" alt="alt" width="70%">
<br>
<hr>

# step2: status/<id> --> details(get), delete(delete), update (put/patch)
#### for update--> UpdateModelMixin, for delete--> DestroyModelMixin,
1. import on views.py file:
```
from rest_framework.generics import RetrieveAPIView


class views.Status_Details_Update_Delete_view_api(RetrieveAPIView): # hendle get request to show detail of a particular obj, of a model table 
      queryset = Status.objects.all() # from which table we want to show the data.
      serializer_class = StatusSerializer # StatusSerializer is the class we made in serializer.py to serialize the object
      lookup_field= 'id' # need to match with urls.py file's accepting key value variable
# By lookup_field--> we are mentioning, which field it will look for the matching and send response

```
2. Now, the class we have defined above: is the simple DetailAPIView class to see the details of an object. 
3. Now, we can use Mixing, to extend the functionality to work as: updateAPI and deleteAPI
4. for update-->import: UpdateModelMixin, for delete-->import: DestroyModelMixin,
5. Need to over ride 2 functions:
6. first function: PUT(work as PUT request if we return self.update(), if we want PATCH request the. partial_update() will be the return parameter), 
7. second function: delete
```
from rest_framework.generics import RetrieveAPIView
from rest_framework.mixins import UpdateModelMixin ,DestroyModelMixin

class Status_Details_Update_Delete_view_api(RetrieveAPIView): # hendle get request to show detail of a particular obj, of a model table 
      queryset = Status.objects.all() # from which table we want to show the data.
      serializer_class = StatusSerializer # StatusSerializer is the class we made in serializer.py to serialize the object
      lookup_field= 'id' # need to match with urls.py file's accepting key value variable

      def put(self, request, *args, **kwargs): # this fuction will anable the update request(PUT)
            return self.update(request,  *args, **kwargs) #if we want PATCH request the. partial_update()
      
      def delete(self, request, *args, **kwargs): # this fuction will anable the delete request(delete)
            return self.destroy(request,  *args, **kwargs)    
```
## Now we can use url: status/<id> --> AS-> details(get), delete(delete), update (put/patch)--> request
<img src="Test API RESPONSE BY HTML JS/details,delete and update request using Mixing.JPG" alt="alt" width="70%">