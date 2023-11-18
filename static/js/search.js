
let search_product = document.getElementsByClassName("search-product");
console.log(search_product)
const search_button = document.getElementsByClassName("get-product");


search_button.addEventListener("click", async (e) => {
    if(search_input[0].value){
        let data = await fetch('http://127.0.0.1:8000/product/product_list/?search=${search_input}$', {
            method: "GET",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": csrftoken
            },
            body: JSON.stringify({
                search: search_input[0].value,
            })
        })
    }else{

    }
});
console.log("some")