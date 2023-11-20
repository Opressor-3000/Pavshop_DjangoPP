const catCheckbox = document.getElementsByClassName("category_checkbox")


for (var i = 0; i < catCheckbox.length; i++) {
   catCheckbox[i].addEventListener("change", (e) => {
      var url = new URL(window.location.href);

      const catList = []

      for (var i = 0; i < catCheckbox.length; i++) {
         if (catCheckbox[i].checked) {
            catList.push(catCheckbox[i].value.toLowerCase())
         }

      }
      url.searchParams.set("category", catList);
      window.history.replaceState(null, null, url);
      getProducts()
   })
}


const colorCheckbox = document.getElementsByClassName("color_checkbox")


for (var i = 0; i < colorCheckbox.length; i++) {
   colorCheckbox[i].addEventListener("change", (e) => {
      var url = new URL(window.location.href);

      const colorList = []

      for (var i = 0; i < colorCheckbox.length; i++) {
         if (colorCheckbox[i].checked) {
            colorList.push(colorCheckbox[i].value)
         }

      }
      url.searchParams.set("color", colorList);
      window.history.replaceState(null, null, url);
      getProducts()
   })
}


const tagCheckbox = document.getElementsByClassName("tag_checkbox")


for (var i = 0; i < tagCheckbox.length; i++) {
   tagCheckbox[i].addEventListener("change", (e) => {
      var url = new URL(window.location.href);

      const tagList = []

      for (var i = 0; i < tagCheckbox.length; i++) {
         if (tagCheckbox[i].checked) {
            tagList.push(tagCheckbox[i].value)
         }

      }
      url.searchParams.set("color", tagList);
      window.history.replaceState(null, null, url);
      getProducts()
   });
};


const getProducts = async () => {

   var url = new URL(window.location.href);
   const category = url.searchParams.get("category") ? url.searchParams.get("category") : ""
   const color = url.searchParams.get("color") ? url.searchParams.get("color") : ""
   const tag = url.searchParams.get("tag") ? url.searchParams.get("tag") : ""

   const response = await fetch(`http://127.0.0.1:8000/api/products/variants/?product_id__category_id__slug=${category}&color__title=${color}&tag__title=${tag}$`)

   const data = await response.json()

   const products = document.getElementsByClassName("papular-block")[0]
   products.innerHTML = ""
   for (var i = 0; i < data.results.length; i++) {
      products.innerHTML += `
        <div class="col-md-4">
        <div class="item"> 
          <!-- Sale Tags -->
          <div class="on-sale"> 10% <span>OFF</span> </div>
          <!-- Item img -->
          <div class="item-img"> <img class="img-1" src="${data.results[i].get_main_img}" alt="" >
            <!-- Overlay -->
            <div class="overlay">
              <div class="position-center-center">
                <div class="inn">
                  <a href="${data.results[i].get_main_img}" data-lighter>
                    <i class="icon-magnifier"></i></a>
                  <button data-product=${data.results[i].id} data-action="add_to_cart" class='update_cart' >
                    <i class="icon-basket"></i>
                  </button> 
                  <a href="#." id="add_wishlist"><i class="icon-heart" id="add_wishlist"></i></a>
                </div>
              </div>
            </div>
          </div>
          <!-- Item Name { data[i].get_absolute_url } -->
          <div class="item-name"> <a href="${data.results[i].get_absolute_url}">${data.results[i].title}</a>
            <p>${data.results[i].product_id.description.slice(0,70)}</p>
          </div>
          <!-- Price --> 
          <span class="price"><small>$</small>${data.results[i].price}</span> 
        </div>
      </div>
        `
   };
};

getProducts()