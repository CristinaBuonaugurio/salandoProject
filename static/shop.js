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
        if( e.currentTarget.dataset['stock'] > 0){
            addProduct(e.currentTarget.dataset['idproduct'], e.currentTarget.dataset['idname']);
            e.currentTarget.dataset['stock'] = e.currentTarget.dataset['stock'] - 1; 
            if(e.currentTarget.dataset['stock'] == 0){
                e.currentTarget.style.visibility = "hidden";
            }   
        }
    })); 

function showCat(e){
    const idCategory = e.currentTarget.dataset['id']; 
    fetch('shop/'+ idCategory, {
        method : 'GET',
        headers:{
            'Content-Type' : 'application/json'
        }
    });
}

let catButtons = document.querySelectorAll(".catButton"); 
catButtons.forEach(el => el.addEventListener("click", showCat)); 


