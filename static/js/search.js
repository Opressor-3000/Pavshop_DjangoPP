
let search_input = document.getElementsByClassName("search-input");
console.log(search_input)
let search_button = document.getElementsByClassName("search-button");
console.log(search_button, 'sdfghjgfdsfghjhjgfdsfghj')

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