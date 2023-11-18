let search_blog = document.getElementsByClassName("search-blog");

// const search_blog_button = document.getElementById("getBlog");



// search_blog_button.addEventListener("click", (e) => {
//     var url = new URL(window.location.href);

//     console.log(e.target.value);

//     url.searchParams.set("search", search_blog.value);
//     window.history.replaceState(null, null, url);
// })


// search_blog_button.addEventListener("click", async (e) => {
//     console.log(e.document.getElementById("search-blog").value);
//     string = search_blog.value
//     let data = await fetch("http://127.0.0.1:8000/blog/list/?search=${string}$", {
//         method: "GET",
//         headers: {
//             "Content-Type": "application/json",
//             "X-CSRFToken": csrftoken
//         },
//         body: JSON.stringify({
//             search: e.document.getElementById("search-posts")[0].value
//         })
//     });
// });