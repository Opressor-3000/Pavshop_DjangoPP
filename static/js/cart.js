

var updateButton = document.getElementsByClassName('update_cart') 

for(var i = 0; i < updateButton.lenght; i++) {
   updateButton[i].addEventListener('click', function(){
      var productId = this.dataset.product
      var action = this.dataset.action
      console.log('productId', productId, 'action', action)

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

   var url = '/updateitem/'

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
      console.log('Data;', data)
   });
}