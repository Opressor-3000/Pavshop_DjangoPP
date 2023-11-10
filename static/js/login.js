


//  СОХРАНИТЬ В LOCAL STORAGE TOKEN 

let loginBtn = document.querySelector("#login-btn");

loginBtn.addEventListener("click", async ()=> {
   let email = document.querySelector(".email").value
   let password = document.querySelector(".password").value
   let body = {
      email,
      password
   }
   let data = await fetch("http://127.0.0.1:8000/api/v1/account/token/", {
      method: "POST",
      headers: {
         "Content_Type": "application/json"
      },
      body: JSON.stringify(body)
   });
   let response = await data.json();
   localStorage.setItem("access_token", response["access"]);
   localStorage.setItem("refresh_token", response["refresh"]);    
});