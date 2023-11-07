const catCheckbox = document.getElementsByClassName("category_checkbox")


for (var i = 0; i < catCheckbox.length; i++) {
   catCheckbox[i].addEventListener("change", (e) => {
      var url = new URL(window.location.href);
      
      console.log(e.target.value);
      const catList=[]
      
      for (var i = 0; i < catCheckbox.length; i++){
         if(catCheckbox[i].checked){
            catList.push(catCheckbox[i].value)
         }
        
      }
      url.searchParams.set("category", catList);
      window.history.replaceState(null,null,url);
      getProducts()
   })
}

const getProducts= async()=>{

 var url = new URL(window.location.href);
   const category=url.searchParams.get("category");

   
   const response= await fetch(`http://127.0.0.1:8000/api/products/variants/?product_id__category_id__slug=${category}`)

   const data=await response.json()
   console.log(data);

   const products=document.getElementsByClassName("papular-block")[0]

   for(var i=0;i<data.length;i++){
      products.innerHTML+=`

      <div class="col-md-4">
      <div class="item"> 
        <!-- Sale Tags -->
        <div class="on-sale"> 10% <span>OFF</span> </div>
        <!-- Item img -->
        <div class="item-img"> <img class="img-1" src="{{ var.get_main_img }}" alt="" >
          <!-- Overlay -->
          <div class="overlay">
            <div class="position-center-center">
              <div class="inn">
                <a href="{{ var.get_main_img }}" data-lighter>
                  <i class="icon-magnifier"></i></a>
                <button data-product={{ var.id }} data-action="add_to_cart" class='update_cart' >
                  <i class="icon-basket"></i>
                </button> 
                <a href="#." ><i class="icon-heart"></i></a>
              </div>
            </div>
          </div>
        </div>
        <!-- Item Name {{ var.slug.get_absolute_url }} -->
        <div class="item-name"> <a href="{% url 'product:product' var.slug %}">{{ var.title }}</a>
          <p>{{ var.product.description }}</p>
        </div>
        <!-- Price --> 
        <span class="price"><small>$</small>${data[i].price}</span> 
      </div>
    </div>
      `

      
   }






}

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