




//  СДЕСЬ ДОЛЖЕН БЫТЬ СКРИПТ КОТОРЫЕ ПРИ НАЖАТИИ НА ЗНАЧОК ВОЗВРАЩАЕТ id ЭЛЕМЕНТА
//  И ПЕРЕДАЕТ ЕГО В URL WISHLIST ДЛЯ ЗАПУСКА ФУНКЦИИ КОТОРАЯ ДОБАВИТЬ ЭЛЕМЕНТ 
//  В БД ТАБЛИЦУ WISHLIST




let addWishlist = document.getElementById("add_wishlist");

addWishlist.addEventListener("click", async (e)=>{
    console.log('add to wishlist begin')
    let data = await fetch("http://127.0.0.1:8000/api/v1/account/add_wishlist/", {
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
    console.log('add to wishlist end')
});