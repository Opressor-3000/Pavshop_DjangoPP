window.addEventListener('load', async () => {
   console.log('+++++++++++++++++++++++++++++++++++++++++++SHOPCART');
   let data = await fetch("http://127.0.0.1:8000/api/v1/account/shopcart/", {
     method: "GET",
     headers: {
       "Content-Type": "application/json",
       "X-CSRFToken": csrftoken
     },
   });
   let shopcartData = await data.json();
   let shopcartContainer = document.getElementById("shopcartdetails");
   for (let product of shopcartData) {
     console.log(product)
     shopcartContainer.innerHTML += `
     <li class="col-sm-6">
       <div class="media"> 
         <!-- Media Image -->
         <div class="media-left media-middle"> <a href="${product.variant.title}" class="item-img"> <img class="media-object" src="${product.variant.get_main_img}" alt=""> </a> </div>
         
         <!-- Item Name -->
         <div class="media-body">
           <div class="position-center-center">
             <h5>${product.variant.title}</h5>
             <p>${product.variant.product_id.title}</p>
           </div>
         </div>
       </div>
     </li>
     
     <!-- PRICE -->
     <li class="col-sm-2">
       <div class="position-center-center"> <span class="price"><small>$</small>${product.variant.price}</span> </div>
     </li>
 
     <li class="col-sm-1">
     <div class="position-center-center">
       <div class="quinty"> 
         <!-- QTY -->
         <div class="position-center-center"> <span class="price"><small>Count</small>${product.count}</span> </div>
        
       </div>
     </div>
   </li>
   
   <!-- TOTAL PRICE -->
   <li class="col-sm-2">
     <div class="position-center-center"> <span class="price"><small>$</small>${product.variant.price}</span> </div>
   </li>
   
   <!-- REMOVE -->
   <li class="col-sm-1">
     <div class="position-center-center"> <a href=""><i class="icon-close"></i></a> </div>
   </li>`;
   }
   console.log('++++++++++++++++++++++++++++++2+++++++++++++SHOPCART');
 })