
let search_input = document.getElementById('search-input')
console.log(search_input.value)
var url = new URL(window.location.href);
url.searchParams.set("search", search_input.value);
window.history.replaceState(null, null, url);
getSearch()

const getSearch = async () => {
    const search_button = document.getElementById("get-product");
    const search = url.searchParams.get("search") ? url.searchParams.get("search") : ""
    search_button.addEventListener("click", async (e)=>{
        if(search_input.value){
            let data = await fetch('http://127.0.0.1:8000/product/product_list/?search=${search}', {
                method: "GET",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": csrftoken
                },
                body: JSON.stringify({
                    search: search_input.value,
                })
            })
        }
    });
};
console.log("some")