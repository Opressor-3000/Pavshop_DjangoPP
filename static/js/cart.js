

// var updateButton = document.getElementsByClassName('update_cart') 

// for(var i = 0; i < updateButton.lenght; i++) {
//    updateButton[i].addEventListener('click', function(){
//       var productId = this.dataset.product
//       var action = this.dataset.action
//       console.log('productId:', productId, 'action:', action)

//       console.log('USER:', user)

//       if (user == 'AnonimousUser') {
//          console.log('User is not authenticated')
//       }else{
//          updateUserOrder(productId, action)
//       }
//    })
// }
 

// function updateUserOrder(productId, action) {
//   console.log('User sending data ...')

//   fetch(url, {
//     method: "POST",
//     headers: {
//         'Context-Type':'application/json',
//         'X-CSRFToken':csrftoken
//     },
//     body:JSON.stringify({
//       product:productId, 
//       action:action
//     })
//   })
//   .then((response) => {
//       return response.json();
//   })
//   .then((data) => {
//     location.reload()
//   });
// }



let addToCart = document.getElementById("addtocart");

addToCart.addEventListener("click", async (e)=>{
  let data = await fetch("http://127.0.0.1:8000/api/v1/account/producttobasketapi/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken":getCookie("csrftoken")
    },
    body: JSON.stringify({
      variant:e.target.dataset.product,
      user:userId
    })
  });
});


