
// // Get request
// ///'asios'(from react frame work)
// axios.get("http://127.0.0.1:8000/apiV1/status_list/").then(response => console.log(response))
// // By using .then we can grab data or printing on screen


// /// post request CreateAPIView
// let statuss = { //making a js object for JSON body
//       user: 1,
//       content: "i am from js file, AXIOS using",
//       image: null
// } // JSON BODY closed

// axios.post("http://127.0.0.1:8000/apiV1/status_create/",
//       statuss,// sending the body
//       {
//             headers: // specifying the content type
//             {
//                   "Content-Type": "application/json",
//             }// we can easily find the content type by using the url 'http://127.0.0.1:8000/apiV1/status_create/' at browser
//       }
//       ///2. Now, if we have only to user object.(user is a foreign key value, we are not inserting from here, just mentioning) and we are sending 100 for user value the this code will throw an exception error. so we need to catch the error.

// ).then(response => console.log(response))
//       .catch(error => console.log(error.message)) // catching the exception message and just printing it again on console



// // Get request (details view API) just need to pass an id with the url
// ///'asios'(from react frame work)
// axios.get("http://127.0.0.1:8000/apiV1/status_details/3").then(response => console.log(response))
// // By using .then we can grab data or printing on screen


// delete request // delete API test (same as detail view api, only need to use axios.delete)
///'asios'(from react frame work)
//axios.delete("http://127.0.0.1:8000/apiV1/status_Delete/4/",).then(response => console.log(response)) // obj with id 3 will be deleted
// // By using .then we can grab data or printing on screen




/// put/patch/update request CreateAPIView
let update_status = { //making a js object for JSON body
      user: 1,
      content: "i am from js file, AXIOS using for update",
      image: null
} // JSON BODY closed

axios.put("http://127.0.0.1:8000/apiV1/status_Update/5",
      update_status,// sending the body
      {
            headers: // specifying the content type
            {
                  "Content-Type": "application/json"
            }// we can easily find the content type by using the url 'http://127.0.0.1:8000/apiV1/status_create/' at browser
      }
      ///2. Now, if we have only to user object.(user is a foreign key value, we are not inserting from here, just mentioning) and we are sending 100 for user value the this code will throw an exception error. so we need to catch the error.

).then(response => console.log(response))

