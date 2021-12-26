
// Get request
///'asios'(from react frame work)
axios.get("http://127.0.0.1:8000/apiV1/status_list/").then(response => console.log(response))
// By using .then we can grab data or printing on screen


/// post request CreateAPIView
let statuss = { //making a js object for JSON body
      user: 1,
      content: "i am from js file, AXIOS using",
      image: null
} // JSON BODY closed

axios.post("http://127.0.0.1:8000/apiV1/status_create/",
      statuss,// sending the body
      {
            headers: // specifying the content type
            {
                  "Content-Type": "application/json",
            }// we can easily find the content type by using the url 'http://127.0.0.1:8000/apiV1/status_create/' at browser
      }

).then(response => console.log(response))


