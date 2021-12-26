### Our django application can handle-> get request
### Now, we will create a HTML file WITH js code to fatch data from the django application by API.

### fetch() : used for get/post request--> in js

### for version1: 
1. First we need to run our django server.
2. Need, to create a html file where js code will be used
3. first --> print the response on console of the browser:
```
<body>
      <script>
            //  My django application handle get response when url: [localhost/status/api] is used 

            // fatch() API, is used to send the get request or fatch the data 
            fetch("http://127.0.0.1:8000/status/api/").then(response => console.log(response))
            // By using .then we can grab or print on console
            // Now, when runing this file on browser we will see an error 
            // to solve: search on google--> cross domain chrome or cross domain chrome
      </script>
</body>
```
4. Now we will access data and print on console-->
```
      <script>
            //  My django application handle get response when url: [localhost/status/api] is used 

            // fatch() API, is used to send the get request or fatch the data 
            fetch("http://127.0.0.1:8000/status/api/").then(response => response.json()).then(data => console.log(data) )
            // By using .then we can grab data or print on console
            // first .then: grabing the responsed data as json--> and 2nd then used to print data at console
            // Now, when runing this file on browser we will see an error 
            // to solve: search on google--> cross domain chrome or cross domain chrome
      </script>
```
5. Here, only those info are showing which we have mentioned in serializer, if we add more parameters in that serializer then we will get those as get response. we can add pk at serializer:
```
class StatusSerializer(serializers.ModelSerializer):
      class Meta:
            model= Status # which model data it will serialize
            fields= ['pk','user','content','image'] 
```
6. Now, we will see the id of a object as pk

### for version2: 
1. Now we will access data and print on console-->
```
      <script>
            //  My django application handle get response when url: [localhost/apiV1/status_list/] is used 

            // fatch() API, is used to send the get request or fatch the data 
            fetch("http://127.0.0.1:8000/apiV1/status_list/").then(response => response.json()).then(data => console.log(data) )
            // By using .then we can grab data or print on console.
            // first .then: grabing the responsed data as json--> and 2nd then used to print data at console
            // Now, when runing this file on browser we will see an error 
            // to solve: search on google--> cross domain chrome or cross domain chrome
      </script>
```
<img src="for version 2 printing data at browser console .JPG" alt="alt" width="100%">

### for version3: sending the POST request, we need to send a body, to create a record.
```
<body>
      <script>
            // we have 3 field to insert in table of django application
            
            let body={      // javascrip obj, we will pass it as json body of post req.
                  user: 1, //foreign key value
                  content: "this is from JS code",
                  Image: null
            }

            //  My django application handle get response when url: [localhost//apiV1/status_create/] is used 
            // fatch() API, is used to send the POST request 
            fetch("http://127.0.0.1:8000/apiV1/status_create/",
            { 
                  method: "POST", // POST request
                  body: JSON.stringify(body), // by stringify the body (declare at top) we are sending as POST req.
                  headers:{ // have to mention the content type, we are sending
                        "Content-Type": "application/json",
                  },// we can easily find the content type by using the url 'http://127.0.0.1:8000/apiV1/status_create/' at browser
            }
            ).then(response => response.json()).then(data => console.log(data) )
            // By using .then we can grab data or print on console.
            // first .then: grabing the responsed data as json--> and 2nd then used to print data at console
            // Now, when runing this file on browser we will see an error 
            // to solve: search on google--> cross domain chrome or cross domain chrome
      </script>
      
</body>
```
#### at the console of browser:
<img src="for version 3 api POST request from js code.JPG" alt="alt" width="100%">

#### Now, if we use version2 code, then we will see a new entry have done in our django model table. 
 

# Now, from here we will use 'asios'(from react frame work).
#### For crud APIs: search on google: axious, will see the github link first, goto the link and copy script (Using unpkg CDN:) to access onlie axious features onlie.
### CDN: <script src="https://unpkg.com/axios/dist/axios.min.js"></script>
1. Now, we will create a js file to keep our code 'script.js'
```
<!-- inside html--> -->
<script src="script.js"></script> 
```
### Now,
1.'axios.get' for get request.
2.'axios.post' for post request. 
3. 'axios.put' for put request.

### Now, we will see a error, when first time at the browser console for using html in live server and django togather. this is ocures, becase, our django running on a port and this live server ogf html page is running on another port.
1. solv error: install django cors headers on django project env (see: django-cors-headers doc by serching on google )
```
$ pip install django-cors-headers
```
2. Now goto settings.py and include at INSTALLED_APPS --> , MIDDLEWARE-->
```
INSTALLED_APPS = [
      ..........,
    "corsheaders",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware", #This one have to be at the top of the all middleWare
    ........,
    "django.middleware.common.CommonMiddleware", # this one should already exist. but if not then include.
]

CORS_ORIGIN_ALLOW_ALL= True # include this too, just under the middleWare list
```


### for version4: detail views with ( lookup_field )
1. inside the script.js file--> call 'axios.get' for get request.
```

///'asios'(from react frame work)
axios.get("http://127.0.0.1:8000/apiV1/status_Details/").then(response => console.log(response) )
// By using .then we can grab data or printing on browser consle
```
2. Now open the html file as live server. and see in console of the browser.
3. Now, we will see a error, first time. this is ocures, becase, our django running on a port and this live server ogf html page is running on another port.
4. solv error: install django cors headers on django project env (see: django-cors-headers doc by serching on google )
```
$ pip install django-cors-headers
```
5. Now goto settings.py and include at INSTALLED_APPS --> , MIDDLEWARE-->
```
INSTALLED_APPS = [
      ..........,
    "corsheaders",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware", #This one have to be at the top of the all middleWare
    ........,
    "django.middleware.common.CommonMiddleware", # this one should already exist. but if not then include.
]

CORS_ORIGIN_ALLOW_ALL= True # include this too, just under the middleWare list
```
#### now we will not see any error at browser console:
6. Run the django server and HTML on live server.
7. Now, reload the HTML document, and Now we are not going to see the error. and we will have our objects.
<img src="Seeing list using js with asios.JPG" alt="alt" width="100%">

### for version3: (CreateAPIView) by using 'asios'(from react frame work)
```

```