### if we click on image link, both from admin panel and list_view_API, we are redercting to a error url.
<img src="clicking the image link and shoing error url.JPG" alt="alt" width="50%">
<br><br>

### to see the the image, we need to add path at main urls.py file

```
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('apiV1/', include('status.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```


## Now, if we click on image, we can access the image

<hr>
<br>

# we can clean image data, after delete or update operation(see: 'image data cleaning, after delete or update operation.md' file)
