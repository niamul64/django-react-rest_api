## image upload by API using parser
### previously we ware sending the data as Json,
### But here we are sending image file. json can't handle it.
<br><br>

## Here we will use 'asios'(from react frame work).
#### For crud APIs: search on google: axious, will see the github link first, goto the link and copy script (Using unpkg CDN:) to access onlie axious features online.
### CDN: <script src="https://unpkg.com/axios/dist/axios.min.js"></script>
<br>

### 1. Now, we will create a js file to keep our code 'script.js'
```
<!-- inside html body -->

<script src="script.js"></script> 
<script src="https://unpkg.com/axios/dist/axios.min.js"></script>
```
### 2. Now in the HTML file, we will make a form: to upload each field of database table
```
      <form action="" id="myForm">
            <input type="number" value="1" id='user'>
            <br>
            <input type="text" value="I am for image up using parser" id='content'>
            <br>
            <input type="file" id='image'>
            <br>
            <br>
            <button type="submit" id="submit" >Submit</button>
      </form>
```
### 3. at js file: access the form and image field (by 2 separet event listener)

1. Now, first handle the image field: if any change happen on the image field then just print on browser console.-> (lets see how its work)

```
document.getElementById('myForm') // get the form from HTML page by its id, then add a event listener
.addEventListener('submit', handleSubmit); // after submit, event will be trigard and 'handleSubmit()' function will be called

document.getElementById('image')// get the image field from HTML page by its id, then add a event listener
.addEventListener('change', handleImage) // if any change heppen in the image field the call handleImage

//// Now, functions:
let myImage = null // a variable to keep the image// if the image field changed then this variable will be not null

function handleImage(e){ // recieve a event through 'e'
      
      myImage= e.target; // keeping the image on previously declared variable
      
      console.log(myImage); // just printing on console of the browser
}

function handleSubmit(e){ // recieve a event through 'e'
      e.preventDefault() // just keeping like this for now//      
}
```
#### Now, if we run the html on live_server. then after selecting the image, it will print on browser console.

<img src="select image in form and print on console.JPG" alt="alt" width="100%">
<br>

### Now, we are geting Html imput tag here in the console: to get the image object we need to specify files:
```
// if we only say files, then we will get a list
// as we are uploading one file, so we can get that from index 0 of the arry list.
      myImage= e.target.files[0]; // keeping the image on previously 

```

### 4. Till now we are getting(image selecting successful) the image and printing on browser console:
### 5. Now, lets handle the submit. When user click the submit button our--> handleSubmit(e) function will be trigered by the event listener. And send django rest api.
### 6. Now, at js file and inside the 'function handleSubmit(e)': 
1. First collect the information from the HTML file, "user, content, image"
2. Previously we ware sending the data as Json, But here we are sending image file. json can't handle it. here we will use a obj: FormData
<img src="visualizasion of html to js grab by id.JPG" alt="alt" width="100%">
<br><br>

### Now to submit --> grab all the value from HTML page, form--> make a form_data--> for body of url.
### and send -->
```

function handleSubmit(e){ // recieve a event through 'e'
      e.preventDefault() 
      let user= document.getElementById('user').value; // grabing the value of input field(from html), which id= 'user'
      let content= document.getElementById('content').value;
      // Previously we ware sending the data as Json, But here we are sending image file. json can't handle it.
      // here we will use a obj: FormData
      let form_data = new FormData(); // creating an object of Form data
      
      // 3 field to send, almost like json, with--> key_value: value
      form_data.append('user',user);
      form_data.append('content',content);
      form_data.append('image',myImage); // if image is not selected then Null will pass, otherwise image will be passed
      
      // Now we will call axios.post("") // frist call for create view//
      axios.post("http://127.0.0.1:8000/apiV1/status/", form_data,{ // sending the body to the create view url
            headers:{
                  "Content-Type" :"multipart/form-data" // as we are sending image file, 
            }
      }).then(response=> response.data) // sending the request
      .then(data => console.log(res)) // second '.then' used to print on console only
}


```
# Now, For Update: just need to use axios.put instead of axios.post and need to send a id with the link.
```
// the main part where change:
axios.put("http://127.0.0.1:8000/apiV1/status/10", form_data,{ // sending the body to the create view url
            headers:{
                  "Content-Type" :"multipart/form-data" // as we are sending image file, 
            }
      }).then(response=> response.data) // sending the request
      .then(data => console.log(res))
```

<hr>

# full js code:
```
document.getElementById('myForm') // get the form from HTML page by its id, then add a event listener
.addEventListener('submit', handleSubmit); // after submit, event will be trigard and 'handleSubmit()' function will be called

document.getElementById('image')// get the image field from HTML page by its id, then add a event listener
.addEventListener('change', handleImage) // if any change heppen in the image field the call handleImage


//// Now, functions:
let myImage = null // a variable to keep the image// if the image field changed then this variable will be not null

function handleImage(e){ // recieve a event through 'e'
      myImage= e.target.files[0]; // keeping the image on previously declared variable
      // console.log(myImage); // just printing on console of the browser

}

function handleSubmit(e){ // recieve a event through 'e'
      e.preventDefault() 
      let user= document.getElementById('user').value; // grabing the value of input field(from html), which id= 'user'
      let content= document.getElementById('content').value;
      // Previously we ware sending the data as Json, But here we are sending image file. json can't handle it.
      // here we will use a obj: FormData
      let form_data = new FormData(); // creating an object of Form data
      
      // 3 field to send, almost like json, with--> key_value: value
      form_data.append('user',user);
      form_data.append('content',content);
      form_data.append('image',myImage); // if image is not selected then Null will pass, otherwise image will be passed
      
      // Now we will call axios.post("") // frist call for create view//
      axios.post("http://127.0.0.1:8000/apiV1/status/", form_data,{ // sending the body to the create view url
            headers:{
                  "Content-Type" :"multipart/form-data" // as we are sending image file, 
            }
      }).then(response=> response.data) // sending the request
      .then(data => console.log(res)) // second '.then' used to print on console only
}


//// Now, functions (end)

```

# full HTML code:
```
<!DOCTYPE html>
<html lang="en">
<head>
      <meta charset="UTF-8">
      <meta http-equiv="X-UA-Compatible" content="IE=edge">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>testing API--> details, delete, update</title>
</head>
<body>
      <form action="" id="myForm">
            <input type="number" value="2" id='user'>
            <br>
            <input type="text" value="I am for image up using parser" id='content'>
            <br>
            <input type="file" id='image'>
            <br>
            <button type="submit" id="submit" >Submit</button>
      </form>


      <script src="https://unpkg.com/axios/dist/axios.min.js"></script>
      <script src="script.js"></script> 
      <!-- just connecting the js file with this HTML -->
</body>
</html>
```

### if we want to see the obj success fully send or not--> we can print response on the console, instead of data --> change in js file bottom part.
```
function handleSubmit(e){ // recieve a event through 'e'
      e.preventDefault() 
      let user= document.getElementById('user').value; // grabing the value of input field(from html), which id= 'user'
      let content= document.getElementById('content').value;
      // Previously we ware sending the data as Json, But here we are sending image file. json can't handle it.
      // here we will use a obj: FormData
      let form_data = new FormData(); // creating an object of Form data
      
      // 3 field to send, almost like json, with--> key_value: value
      form_data.append('user',user);
      form_data.append('content',content);
      form_data.append('image',myImage); // if image is not selected then Null will pass, otherwise image will be passed
      
      // Now we will call axios.post("") // frist call for create view//
      axios.post("http://127.0.0.1:8000/apiV1/status/", form_data,{ // sending the body to the create view url
            headers:{
                  "Content-Type" :"multipart/form-data" // as we are sending image file, 
            }
      }).then(response=> console.log(response))// will print the response in the console of browser. 
}
```