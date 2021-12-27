### Part2: of Django rest_Frame_work (Using Mixing: see official doc-> usder generic views)
LINK OF OFFICIAL DOC: https://www.django-rest-framework.org/api-guide/generic-views/#mixins

### Here we will use Less urls to do all the work. using different urls for every specifi work is not efficient.
### use only two urls to perform all the task.
# we will design as:
```

# if any one requests url -> will access (request)
step1: status/            ->  List(get), Create(post)
step2: status/<id>        -> details(get), delete(delete), update (put/patch)

```


# step1: ListViewAPI(get), CreateViewAPI(post)
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
4. Now, use Mixing class: CreateModelMixing. So Need to import from mixing, at views.py
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
## Now we can use url: status/ --> AS->  List(get), Create(post) --> request
<img src="Test API RESPONSE BY HTML JS/GET and POST request using Mixing.JPG" alt="alt" width="100%">