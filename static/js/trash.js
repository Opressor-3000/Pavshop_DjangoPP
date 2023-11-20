
const getProfile= async()=>{
   var url = new URL(window.location.href);
 
   const response= await fetch(`http://127.0.0.1:8000/api/v1/account/`)
 
   const data=await response.json()
 
   const profile = document.getElementsByClassName("cart-detail")[0]
   profile.innerHTML=""
 
   for(var i=0;i<data.results.length;i++){
     profile.innerHTML+=`
     
     `
   }
 }
 
 
 // Удаление из корзины 
 let dltFromCart = document.getElementById("remove-product");
 
 
 dltFromCart.addEventListener("click", async (e)=>{
   let data = await fetch("http://127.0.0.1:8000/api/v1/delete/", {
       method: "GET",
       headers: {
           "Content-Type": "application/json",
           "X-CSRFToken":csrftoken
       },
       body: JSON.stringify({
           delete: e.document.getElementById("product-id")[0].value
       })
   });
 });
 
 
 const removeBtn = document.querySelectorAll('.remove-product')
 removeBtn.forEach (function (rBtn) {
     rBtn.addEventListener('click', function () {
     });
 }); 
 
 
 
 
 const shopping_cart=document.getElementsByClassName("shopping_cart")[0]
 const delete_btn=document.getElementsByClassName("delete_variant")
 
 delete_btn.forEach(element => {
   element.addEventListener("click",(e)=>{
     
   })
 });
 
 let wishlist
 
 
 async function shoppingCart(){
    const response=await fetch("http://127.0.0.1:8000/api/v1/account/",{
     
    })
 
 }
 
 window.addEventListener('load', async ()=>{
    let data = await fetch("http://127.0.0.1:8000/api/v1/account/", {
       method: "GET",
       headers: {
          "Context-Type": "application/json",
          "Authorization": `Bearer ${localStorage.getItem("access_token")}`
       }
      
    });
    let account = await data.json()
    let orderContainer = document.getElementById("");
 
    for (let order of account.orders) {
 
    }
 })
 
 
 
 
 // class=product_review
 `
 <div role="tabpanel" class="tab-pane fade" id="review"> 
                   <div class="media">
                     <div class="media-left"> 
                       <!--  Image -->
                       <div class="avatar"> <img class="media-object" src="{{ r.avatar }}" alt=""> </div>
                     </div>
                     <!--  Details -->
                     {% for review in user_reviews %}
                     <div class="media-body">
                     <button data-product="{{product.id}}" class="delete_btn"></button>
                       <a href="{% url 'product:product' review.product.slug %}"><h6>{{ review.product.title }}<span class="pull-right">{{ review.date }}</span> </h6></a>
                       <p class="font-playfair">{{ review.text }}</p>
                     </div>
                     {% endfor %}
                   </div>
                 </div>
 `
 
 
 
 // class = post_review 
 `
 <div class="media">
 <div class="media-left"> 
   <!--  Image -->
   <div class="avatar"> <a href="#"> <img class="media-object" src="images/avatar-1.jpg" alt=""> </a> </div>
 </div>
 <!--  Details -->
 <div class="media-body">
   <p><a href="{% url 'product:product' review.product.slug %}">Product</a></p>
   <p class="font-playfair">“Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut
     labore et dolore magna aliqua.”</p>
   <h6>TYRION LANNISTER <span class="pull-right">MAY 10, 2016</span> </h6>
 </div>
 </div>
 `
 
 
 
 // class = shopcart details 
 
 





// ------------------------------------------CART------------------------------------------- 


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


// ---------------------------



// for(var i=0;i<data.length;i++){
//    products.innerHTML+=`<ul>
//             <li class="col-sm-6">
//               <div class="media"> 
//                 <!-- Media Image -->
//                 <div class="media-left media-middle"> <a href="{% url 'product:product' sc.slug %}" class="item-img"> <img class="media-object" src="{% static 'images/cart-img-3.jpg' %}" alt=""> </a> </div>
                
//                 <!-- Item Name -->
//                 <div class="media-body">
//                   <div class="position-center-center">
//                     <h5>{{ sc.title }}</h5>
//                     <p>{{ sc.get_product}}</p>
//                   </div>
//                 </div>
//               </div>
//             </li>
            
//             <!-- PRICE -->
//             <li class="col-sm-2">
//               <div class="position-center-center"> <span class="price"><small>$</small>{{ sc.price }}</span> </div>
//             </li>
            
//             <!-- QTY -->
//             <li class="col-sm-1">
//               <div class="position-center-center">
//                 <div class="quinty"> 
//                   <!-- QTY -->
//                   <select class="selectpicker">
//                     <option>1</option>
//                   </select>
//                 </div>
//               </div>
//             </li>
            
//             <!-- TOTAL PRICE -->
//             <li class="col-sm-2">
//               <div class="position-center-center"> <span class="price"><small>$</small>{{ sc.total.price }}</span> </div>
//             </li>
            
//             <!-- REMOVE -->
//             <li class="col-sm-1">
//               <div class="position-center-center"> <a href=""><i class="icon-close"></i></a> </div>
//             </li>
//             </ul>
//             `
// };



// if('{{request.user}}'!=='AnonymousUser'){
//   document.getElementById('addtocart').addEventListener('click', function(){
//     if(document.getElementById('quantity').value) {
//       var selectedQuantity=document.getElementById('quantity').value;
//     }else{
//       var selectedQuantity = 1
//     };

//   var productId = '{{ product.id }}'
//   var action = this.dataset.action
//   var quantity = selectedQuantity
//   addtocart(productId,action,quantity);

//   });
// };




// function addtocart(productId, action, quantity) {
//   var url = '/account/shopping_cart/'
//   fetch(url, {
//       method:"POST",
//       headers: {
//           "X-CSRFToken": getCookie("csrftoken"),
//           "Accept": "application/json",
//           'Content-Type': 'application/json'
//       },
//       body:JSON.stringify({ 'productId':productId,
//                             'action':action,
//                             'userId':userId,
//                             'quantity':quantity
//                           })
//   })
//   .then((response)=>{
//       return response.json();
//   })
//   .then((data)=>{
//       console.log(data);
//       main_pop();
//   })
// }



// -----------------------------FILTER-----------------------------------------------


// const colCheckbox = document.getElementsByClassName("colour_checkbox")

// for (var i = 0; i < colCheckbox.length; i++) {
//    colCheckbox[i].addEventListener("change", (e) => {
//       var searchParams = new URLSearchParams(window.location.search);
//       searchParams.set("color", e.target.value);
//       window.location.search = searchParams.toString();
//       if (e.target.checkhed){
        
//       }
//    })
// }

// const brandCheckbox = document.getElementsByClassName("brand_checkbox")

// for (var i = 0; i < brandCheckbox.length; i++) {
//    brandCheckbox[i].addEventListener("change", (e) => {
//       var searchParams = new URLSearchParams(window.location.search);
//       searchParams.set("brand", e.target.value);
//       window.location.search = searchParams.toString();
//       if (e.target.checkhed){
        
//       }
//    })
// }




// -----------------------MAIN JS -----------------------------------------------------



//  let loginBtn = document.querySelector("#login_btn");

//  loginBtn.addEventListener("click", async () => {
// 	let email = document.querySelector("#mail").value
// 	let password = document.querySelector("#psw").value
// 	let data = await fetch("http://127.0.0.1:8000/api/v1/account/token/", {
// 		method: "POST",
// 		header:{
// 			"Content-Type": "application/json"
// 		},
// 		body: JSON.stringify(body)
// 	});
// 	let response = await data.json();
// 	localStorage.setItem("pavshop_access_token", response["access"]);
// 	localStorage.setItem("pavshop_refresh_token", response["refresh"]);
//  });

//  method: "POST",
//  headers: {
// 	  "Content-Type": "application/json",
// 	  "X-CSRFToken":csrftoken
//  },
//  body: JSON.stringify({
// 	  variant:e.target.dataset.product,
// 	  user:userId
//  })



