let searchBlog_blog = document.getElementsByClassName("search-blog");

let searchBloginput = document.getElementById('search-input')
console.log(searchBlogInput.value)
var url = new URL(window.location.href);
url.searchParams.set("searchBlog", searchBlogInput.value);
window.history.replaceState(null, null, url);
getsearchBlog()

const getsearchBlog = async () => {
    const searchBlog_button = document.getElementById("get-product");
    const searchBlog = url.searchParams.get("searchBlog") ? url.searchParams.get("searchBlog") : ""
    searchBlog_button.addEventListener("click", async (e)=>{
        if(searchBlog_input.value){
            let data = await fetch('http://127.0.0.1:8000/product/product_list/?searchBlog=${searchBlog}', {
                method: "GET",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": csrftoken
                },
                body: JSON.stringify({
                    searchBlog: searchBlogInput.value,
                })
            })
        }
    });
};
console.log("some")