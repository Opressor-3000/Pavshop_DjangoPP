


let addToCart = document.getElementById("addtocart");

addToCart.addEventListener("click", async (e)=>{
  console.log('add to shoping cart begin');
  let data = await fetch("http://127.0.0.1:8000/api/v1/account/addtocart/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken":csrftoken
    },
    body: JSON.stringify({
      variant:e.target.dataset.product,
      user:userId
    })
  });
  console.log('add to shoping cart end');
});


