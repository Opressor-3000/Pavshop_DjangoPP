const catCheckbox = document.getElementsByClassName("category_checkbox")


for (var i = 0; i < catCheckbox.length; i++) {
   catCheckbox[i].addEventListener("change", (e) => {
      var searchParams = new URLSearchParams(window.location.search);
      searchParams.set("category", e.target.value);
      window.location.search = searchParams.toString();
      if (e.target.checkhed){
        
      }
   })
}

const colCheckbox = document.getElementsByClassName("colour_checkbox")

for (var i = 0; i < colCheckbox.length; i++) {
   colCheckbox[i].addEventListener("change", (e) => {
      var searchParams = new URLSearchParams(window.location.search);
      searchParams.set("color", e.target.value);
      window.location.search = searchParams.toString();
      if (e.target.checkhed){
        
      }
   })
}

const brandCheckbox = document.getElementsByClassName("brand_checkbox")

for (var i = 0; i < brandCheckbox.length; i++) {
   brandCheckbox[i].addEventListener("change", (e) => {
      var searchParams = new URLSearchParams(window.location.search);
      searchParams.set("brand", e.target.value);
      window.location.search = searchParams.toString();
      if (e.target.checkhed){
        
      }
   })
}