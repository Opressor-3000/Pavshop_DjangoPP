



//  ЭТОТ СКРИПТ ДОЛЖЕН ВНЕДОИТЬ ВСЕ ДАННЫЕ АККАУТА НА СТРАНИЦУ ACCOUNT 
//  ДАННЫЕ ПРИХОДЯТЬ С ПОМОШЬЮ --API--   
//  ORDERS, WISHLIST, POSTS, REVIEWS POST, REVIEWS PRODUCT,  




const shopping_cart=document.getElementsByClassName("shopping_cart")[0]
let wishlit = 1


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

`
<ul class="row cart-details">
<li class="col-sm-6">
  <div class="media"> 
    <!-- Media Image -->
    <div class="media-left media-middle"> <a href="{% url 'product:product' sc.slug %}" class="item-img"> <img class="media-object" src="{% static 'images/cart-img-3.jpg' %}" alt=""> </a> </div>
    
    <!-- Item Name -->
    <div class="media-body">
      <div class="position-center-center">
        <h5>{{ sc.title }}</h5>
        <p>{{ sc.get_product}}</p>
      </div>
    </div>
  </div>
</li>

<!-- PRICE -->
<li class="col-sm-2">
  <div class="position-center-center"> <span class="price"><small>$</small>{{ sc.price }}</span> </div>
</li>

<!-- QTY -->
<li class="col-sm-1">
  <div class="position-center-center">
    <div class="quinty"> 
      <!-- QTY -->
      <select class="selectpicker">
        <option>1</option>
      </select>
    </div>
  </div>
</li>

<!-- TOTAL PRICE -->
<li class="col-sm-2">
  <div class="position-center-center"> <span class="price"><small>$</small>{{ sc.total.price }}</span> </div>
</li>

<!-- REMOVE -->
<li class="col-sm-1">
  <div class="position-center-center"> <a href=""><i class="icon-close"></i></a> </div>
</li>
</ul>
`