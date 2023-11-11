




function getToken(name) {
   let cookieValue = null;
   if (document.cookie && document.cookie !== '') {
       const cookies = document.cookie.split(';');
       for (let i = 0; i < cookies.length; i++) {
           const cookie = cookies[i].trim();
           // Does this cookie string begin with the name we want?
           if (cookie.substring(0, name.length + 1) === (name + '=')) {
               cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
               break;
           }
       }
   }
   console.log(cookieValue);
   return cookieValue;
}

const csrftoken = getToken('csrftoken')

let addWishlist = document.getElementById("search-button");

addWishlist.addEventListener("click", async (e)=>{

   let data = await fetch("http://127.0.0.1:8000/blog/list/", {
       method: "GET",
       headers: {
           "Content-Type": "application/json",
           "X-CSRFToken":csrftoken
       },
       body: JSON.stringify({
           search: e.document.getElementById("search-posts").value
       })
   });

});