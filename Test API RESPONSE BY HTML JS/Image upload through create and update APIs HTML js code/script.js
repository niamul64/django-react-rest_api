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
      }).then(response=> console.log(response)) // second '.then' used to print on console only
}


//// Now, functions (end)