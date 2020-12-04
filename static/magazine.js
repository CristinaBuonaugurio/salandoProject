function modifyProduct(e){
    const idproduct = e.currentTarget.dataset['id']; 
    const description = document.querySelectorAll(".description");
    const quantity = document.querySelectorAll(".quantityNumber");
    let flag = false; 
    for( let i=0; i<description.length; i++)
    {
        if(description[i].value == "" && quantity[i].value == 0)
            {
                console.log("empty"); 
                flag = false;
            }
        else 
        {
            newDescr = description[i].value; 
            newquant = quantity[i].value;
            console.log(newDescr); 
            console.log(newquant); 
            flag = true;
            break;  
        }
    }
     
    if(flag){
        fetch('/magazine/modifyProduct', {
            method : 'POST', 
            body : JSON.stringify({
                'id' : idproduct,
                'description' : newDescr, 
                'quantity' : newquant
            }), 
            headers:{
                'Content-Type' : 'application/json'
            }
        })
    }
}

let productButtons = document.querySelectorAll(".productButton"); 
productButtons.forEach(el => el.addEventListener("click", modifyProduct)); 