

var updateButton = document.getElementsByClassName('update_cart') 

for(var i = 0; i < updateButton.lenght; i++) {
   updateButton[i].addEventListener('click', function(){
      var productId = this.dataset.product
      var action = this.dataset.action
      console.log('productId:', productId, 'action:', action)

      console.log('USER:', user)

      if (user == 'AnonimousUser') {
         console.log('User is not authenticated')
      }else{
         updateUserOrder(productId, action)
      }
   })
}
 

function updateUserOrder(productId, action) {
   console.log('User sending data ...')

   var url = '/add_item/'

   fetch(url, {
      method: "POST",
      headers: {
         'Context-Type':'application/json',
         'X-CSRFToken':csrftoken
      },
      body:JSON.stringify({'productId':productId, 'action':action})
   })
   .then((response) => {
       return response.json();
   })
   .then((data) => {
      console.log('Data:', data)
      location.reload()
   });
}




for(var i=0;i<data.length;i++){
   products.innerHTML+=`<ul>
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
};



if('{{request.user}}'!=='AnonymousUser'){
  document.getElementById('addtocart').addEventListener('click', function(){
    if(document.getElementById('quantity').value) {
      var selectedQuantity=document.getElementById('quantity').value;
    }else{
      var selectedQuantity = 1
    }

    var productId = '{{product.id}}'
    var action = this.dataset.action
    var quantity = selectedQuantity

    addtocart(productId,action,quantity)

function addtocart(productId, action, quantity) {
  var url = '/account/shopping_cart/'
  fetch(url, {
      method:"POST",
      headers: {
          "X-CSRFToken": getCookie("csrftoken"),
          "Accept": "application/json",
          'Content-Type': 'application/json'
      },
      body:JSON.stringify({ 'productId':productId,
                            'action':action,
                            'userId':userId,
                            'quantity':quantity
                          })
  })
  .then((response)=>{
      return response.json();
  })
  .then((data)=>{
      console.log(data);
      main_pop();
  });
}