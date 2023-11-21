



//  ЭТОТ СКРИПТ ДОЛЖЕН ВНЕДОИТЬ ВСЕ ДАННЫЕ АККАУТА НА СТРАНИЦУ ACCOUNT 
//  ДАННЫЕ ПРИХОДЯТЬ С ПОМОШЬЮ --API--   
//  ORDERS, WISHLIST, POSTS, REVIEWS POST, REVIEWS PRODUCT,  


//--------------------------------------------------------------------------------------------------------------------------
  // WISHLIST FETCH +++++++++++++++++++++++++++++++++++++++++++++++++++

window.addEventListener('load', async () => {
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
        <div class="media-left media-middle"> <a href="${product.variant.get_absolute_url}" class="item-img"> <img class="media-object" src="" alt=""> </a> </div>
        
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
  console.log('++++++++++++++++++++++++++++++++++++++++++++WISHLIST')
})



//=++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
//     ORDER FETCH ------------------------------------------------------------------------------------


window.addEventListener('load', async () => {
  let data = await fetch("http://127.0.0.1:8000/api/v1/account/orders/", {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrftoken
    },
  });
  let orderData = await data.json();
  let orderContainer = document.getElementById("orderdetails");
  for (let product of orderData) {
    console.log(product)
    orderContainer.innerHTML += `
    <li class="col-sm-6">
      <div class="media"> 
        <!-- Media Image -->
        <div class="media-left media-middle"> <a href="${product.get_absolute_url}" class="item-img"> <img class="media-object" src="" alt=""> </a> </div>
        
        <!-- Item Name -->
        <div class="media-body">
          <div class="position-center-center">
            <h5>${product.title}</h5>
            <p>${product.product_id}</p>
          </div>
        </div>
      </div>
    </li>
    
    <!-- PRICE -->
    <li class="col-sm-2">
      <div class="position-center-center"> <span class="price"><small>$</small>${product.price}</span> </div>
    </li>

    <!-- ADD TO WISHLIST -->
    <li class="col-sm-1">
    <div class="position-center-center" id="add-product">
      <a href="" id="addtowishlist" data-product=${product.id}>
        <i class="icon-heart" id="addwishlist">
      </i>
      </a> </div>
    </li>`;
  }
  console.log('+++++++++++++++++++++++++++++++++++++++++++++ORDER')
})


//++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
//              SHOPCART   FETCH     ----------------------------------------------------------------

window.addEventListener('load', async () => {
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
        <div class="media-left media-middle"> <a href="${product.get_absolute_url}" class="item-img"> <img class="media-object" src="" alt=""> </a> </div>
        
        <!-- Item Name -->
        <div class="media-body">
          <div class="position-center-center">
            <h5>${product.title}</h5>
            <p>${product.product_id}</p>
          </div>
        </div>
      </div>
    </li>
    
    <!-- PRICE -->
    <li class="col-sm-2">
      <div class="position-center-center"> <span class="price"><small>$</small>${product.price}</span> </div>
    </li>

    <!-- ADD TO WISHLIST -->
    <li class="col-sm-1">
    <div class="position-center-center" id="add-product">
      <a href="" id="addtowishlist" data-product=${product.id}>
        <i class="icon-heart" id="addwishlist">
      </i>
      </a> </div>
    </li>`;
  }
  console.log('++++++++++++++++++++++++++++++++++++++++++++SHOPCART')
})





