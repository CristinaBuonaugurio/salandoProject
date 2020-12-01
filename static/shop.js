let modal = document.querySelector(".modal");
let triggers = document.querySelectorAll(".productButton");
let closeButton = document.querySelector(".close-button");

function toggleModal() {
    modal.classList.toggle("show-modal");
}
function windowOnClick(event) {
    if (event.target === modal) {
        toggleModal();
    }
}
for (let i = 0; i < triggers.length; i++) {
    const trigger = triggers[i];
    trigger.addEventListener("click", toggleModal);
}

closeButton.addEventListener("click", toggleModal);
window.addEventListener("click", windowOnClick);


function addProduct(idB, productName) {

console.log(productName); 

fetch('/shop/add', {
    method: 'POST',
    body: JSON.stringify({
        'mail': sessionStorage.getItem('currentUser'), 
        'id' : idB,
        'numOfProd' : 1, 
        'name' : productName
    }),
    headers: {
        'Content-Type': 'application/json'
    }
}).then(function (response) {
    return response.json();
}).then(function (jsonResponse) {
    console.log(jsonResponse);
});
}

let confirmButtons = document.querySelectorAll(".modal-content .confirmButton");
confirmButtons.forEach(el => el.addEventListener("click", addProduct));

let buttons = document.querySelectorAll(".productButton"); 
buttons.forEach(el => el.addEventListener("click", function (e) {
        addProduct(e.currentTarget.dataset['idproduct'], e.currentTarget.dataset['idname']);
    })); 