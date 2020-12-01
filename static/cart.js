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


/*
function checkDatas(){
    if(!document.querySelectorAll('.buttonX'))
    {
        document.getElementById('cb').className = 'hidden';
        document.getElementById('pb').className = 'hidden';
    }
    else
    {
        document.getElementById('cb').className = 'cancelButton';
        document.getElementById('pb').className = 'purchaseButton';
    }
}
window.onload = checkDatas(); */


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


function confirmPurchase(){
    fetch('/shop/cart/confirm', {
        headers: {
            'Content-Type': 'application/json'
        }
    }).then(function(){
        const list = document.getElementById('listItems'); 
        list.innerHTML = "";
    })    
}

let confirButtonEvent = document.querySelector('.purchaseButton'); 
confirButtonEvent.addEventListener("click", confirmPurchase); 