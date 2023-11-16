// ------------------------------------------CART------------------------------------------- 


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





