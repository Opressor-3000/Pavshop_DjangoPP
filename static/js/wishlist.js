




//  СДЕСЬ ДОЛЖЕН БЫТЬ СКРИПТ КОТОРЫЕ ПРИ НАЖАТИИ НА ЗНАЧОК ВОЗВРАЩАЕТ id ЭЛЕМЕНТА
//  И ПЕРЕДАЕТ ЕГО В URL WISHLIST ДЛЯ ЗАПУСКА ФУНКЦИИ КОТОРАЯ ДОБАВИТЬ ЭЛЕМЕНТ 
//  В БД ТАБЛИЦУ WISHLIST
function getToken(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getToken('csrftoken')
console.log(csrftoken);

let addWishlist = document.getElementById("add_wishlist");

addWishlist.addEventListener("click", async (e)=>{
    console.log("hereee++++");

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

});