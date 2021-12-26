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
            // By using .then we can grab or print on console
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
            // By using .then we can grab or print on console
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
            // By using .then we can grab or print on console
            // first .then: grabing the responsed data as json--> and 2nd then used to print data at console
            // Now, when runing this file on browser we will see an error 
            // to solve: search on google--> cross domain chrome or cross domain chrome
      </script>
      
</body>
```
#### at the console of browser:
<img src="for version 3 api POST request from js code.JPG" alt="alt" width="100%">

#### Now, if we use version2 code, then we will see a new entry have done in our django model table. 
 
