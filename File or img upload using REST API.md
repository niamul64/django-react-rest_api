### in our model: we have a field to upload an image.
#### Parser classes, that allow you to accept requests with various media types
### Here we will see how we can upload an image by API
Official document: https://www.django-rest-framework.org/api-guide/parsers/
```
class Status(models.Model):
      user =models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE)
      content = models.TextField(null=True, blank= True)
      image = models.ImageField(upload_to=upload_status_image, null=True, blank=True)   # image field
      updated = models.DateTimeField(auto_now= True)
      created = models.DateTimeField(auto_now_add= True)
```

# Parser classes: first we will see 'MultiPartParse' and 'FileUploadParser'
#### You will typically want to use both FormParser and MultiPartParser together in order to fully support HTML form data.
<br>

### 1. Now, in views.py file: from parsers import FormParser and MuMultiPartParse
```
## in views.py file
from rest_framework.parsers import FormParser, MultiPartParser
```
### 2. We need to use parsers in each class views where the image will come.
### 3. So, we need to add parsers in create view and update view
```
class List_Create_APIView(ListCreateAPIView): # will work for GET and POST Request
      queryset= Status.objects.all() # grab all data from 'Status' table
      # 'queryset' : defines, on which model/table we are doing query and collecting obj
      
      # Now, mention the serializer class, that we are using to serialize the the object.
      serializer_class= StatusSerializer # StatusSerializer is the class we made in serializer.py to serialize the object
      
      # parser class for image upload:
      parser_classes=[parsers.FormParser,parsers.MultiPartParser] ####################################################
      
      
class Details_Update_Delete_APIView(RetrieveUpdateDestroyAPIView): 
      queryset= Status.objects.all() # grab all data from 'Status' table
      # 'queryset' : defines, on which model/table we are doing query and collecting obj
      
      # Now, mention the serializer class, that we are using to serialize the the object.
      serializer_class= StatusSerializer # StatusSerializer is the class we made in serializer.py to serialize the object
      lookup_field= 'id' # need to match with urls.py file's accepting key value variable
      # By lookup_field--> we are mentioning, which field it will look for the matching and send response
      
      # parser class for image upload:
      parser_classes=[parsers.FormParser,parsers.MultiPartParser] ####################################################
```

### Now check from HTML js code to upload a image through create and update APIs 
### see in folder 'Test API RESPONSE BY HTML JS/HTML js code to upload a image through create and update APIs' in this reposetory