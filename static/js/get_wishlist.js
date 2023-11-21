
window.addEventListener('load', async () => {
   console.log('++++++++++++++++++++++++++++++++++++++++++++WISHLIST');
   let data = await fetch("http://127.0.0.1:8000/api/v1/account/wishlist/", {
     method: "GET",
     headers: {
       "Content-Type": "application/json",
       "X-CSRFToken": csrftoken
     },
   });
   let wishlistData = await data.json();
   let wishlistContainer = document.getElementById("wishlistdetails");
   for (let product of wishlistData) {
     console.log(product.variant.title)
     wishlistContainer.innerHTML += `
     <li class="col-sm-6">
       <div class="media"> 
         <!-- Media Image -->
         <div class="media-left media-middle"> <a href="${product.variant.get_absolute_url}" class="item-img"> <img class="media-object" src="${product.variant.get_main_img}" alt=""> </a> </div>
         
         <!-- Item Name -->
         <div class="media-body">
           <div class="position-center-center">
             <h5>${product.variant.title}</h5>
             <p>${product.variant.product_id.description}</p>
           </div>
         </div>
       </div>
     </li>
     
     <!-- PRICE -->
     <li class="col-sm-2">
       <div class="position-center-center"> <span class="price"><small>$</small>${product.variant.price}</span> </div>
     </li>
 
     <!-- ADD TO WISHLIST -->
     <li class="col-sm-1">
     <div class="position-center-center" id="add-product">
       <a href="" id="addtowishlist" data-product=${product.variant.id}>
         <i class="icon-heart" id="addwishlist">
       </i>
       </a> </div>
     </li>`;
   }
   console.log('++++++++++++++++++2+++++++++++++++++++++++++WISHLIST')
 })
 