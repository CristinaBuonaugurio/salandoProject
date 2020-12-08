function deleteItemInCart(e){
    const idproduct = e.currentTarget.dataset['id']; 
    fetch('/shop/cart/delete', {
        method: 'DELETE', 
        body: JSON.stringify({
            'id' : idproduct
        }),
        headers:{
            'Content-Type' : 'application/json'
        }       
    }).then(function() {
        const item = e.target.parentElement;
        item.remove();
    })
}

let buttonsX = document.querySelectorAll('.buttonX'); 
buttonsX.forEach(el => el.addEventListener("click", deleteItemInCart)); 

function emptyCart(){
    fetch('/shop/cart/empty', {
        method : 'DELETE',
        headers:{
            'Content-Type' : 'application/json'
        }  
    }).then(function(){
        const list = document.getElementById('listItems'); 
        list.innerHTML = ""; 
    })
}

let emptyButtonEvent = document.querySelector('.cancelButton'); 
emptyButtonEvent.addEventListener("click", emptyCart); 




function confirmPurchase(methodOfPayment){
    fetch('/shop/cart/confirm', {
        method : 'POST',
        body : JSON.stringify({
            'paymentmethod' : methodOfPayment
        }),
        headers: {
            'Content-Type': 'application/json'
        }
    }).then(function(){
        const list = document.getElementById('listItems'); 
        list.innerHTML = "";
        alert("Thanks for your purchase! Will you be now redirected to the shop page!"); 
        window.location.href = '/shop'; 
    })   
}



function getMethodPayment(){
    let checkboxes = document.querySelectorAll(".payment"); 
    let methodOfPayment = ""; 
    for(let i=0; i<checkboxes.length; i++){
        const check = checkboxes[i]; 
        if(check.checked == true){
            methodOfPayment = check.dataset['id']; 
            console.log(methodOfPayment); 
        }
    }
    if (methodOfPayment == ""){
        methodOfPayment = 'CONTANTI'; //set method of default
    }
    confirmPurchase(methodOfPayment); 
}

function toggleModal() {
    modal.classList.toggle("show-modal");
}

function windowOnClick(event) {
    if (event.target === modal) {
        toggleModal();
    }
}

let modal = document.querySelector(".modal");
let closeButton = document.querySelector(".close-button");
closeButton.addEventListener("click", toggleModal);


let purchaseButton = document.querySelector('.purchaseButton'); 
purchaseButton.addEventListener("click", toggleModal); 



let confirmButtonEvent = document.querySelector('.confirmPurchase'); 
confirmButtonEvent.addEventListener("click", getMethodPayment);

