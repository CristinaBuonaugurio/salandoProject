function modifyProduct(e) {
    const idproduct = e.currentTarget.dataset['id'];
    const description = document.querySelectorAll(".description");
    const quantity = document.querySelectorAll(".quantityNumber");
    let flag = false;
    for (let i = 0; i < description.length; i++) {
        if (description[i].value == "" && quantity[i].value == 0) {
            console.log("empty");
            flag = false;
        }
        else {
            newDescr = description[i].value;
            newquant = quantity[i].value;
            console.log(newDescr);
            console.log(newquant);
            flag = true;
            break;
        }
    }

    if (flag) {
        fetch('/magazine/modifyProduct', {
            method: 'POST',
            body: JSON.stringify({
                'id': idproduct,
                'description': newDescr,
                'quantity': newquant
            }),
            headers: {
                'Content-Type': 'application/json'
            }
        })
    }
}

let productButtons = document.querySelectorAll(".productButton");
productButtons.forEach(el => el.addEventListener("click", modifyProduct));


let modal = document.querySelector(".modal");
let closeButton = document.querySelector(".close-button");

function toggleModal() {
    modal.classList.toggle("show-modal");
}
function windowOnClick(event) {
    if (event.target === modal) {
        toggleModal();
    }
}

closeButton.addEventListener("click", toggleModal);
window.addEventListener("click", windowOnClick);

let button = document.getElementById("addP");
button.addEventListener("click", toggleModal);


function addNewProduct() {
    const nameProduct = document.getElementById("nameProduct").value;
    const descProduct = document.getElementById("descProduct").value;
    const category = document.getElementById("category").value;
    const cost = document.getElementById("cost").value;
    const quantity = document.getElementById("quantity").value;

    fetch('/magazine/products', {
        method: 'POST',
        body: JSON.stringify({
            'name': nameProduct,
            'description': descProduct,
            'cost': cost,
            'quantity': quantity,
            'category': category
        }),
        headers: {
            'Content-Type': 'application/json'
        }
    }).then(function (response) {
        return response.json();
    }).then(function (jsonResponse) {
        if (jsonResponse.success == true) {
            alert("Product inserted in the database successfully!");
            window.location.href = '/magazine';
        }
    })
}

let buttonNewProd = document.querySelector(".confirmNewProd");
buttonNewProd.addEventListener("click", addNewProduct);


function showtfidf() {
        document.getElementById('detailsList').innerHTML = ""; 
        document.getElementById("secProd").className = 'hidden';
        document.getElementById("tfidfClass").className = 'tfidfInfo';
        fetch('/magazine/tfidf', {
            method: 'GET'
        }).then(function (response) {
            return response.json();
        }).then(function (jsonResponse) {
            dict = jsonResponse
            for (let k in dict) {
                let pippo = dict[k];
                var sum = document.createElement('summary');
                var detail = document.createElement('details');
                detail.className = 'detailsTFIDF';
                
                sum.innerHTML = k;
                detail.appendChild(sum);
                var list = document.createElement('ul');

                for (const [key, value] of Object.entries(pippo)) {
                    console.log(key, value);
                    var liel = document.createElement('li');
                    liel.innerHTML = 'idproduct: ' + key + ' tfidf value: ' + value + ' \n';
                    list.appendChild(liel);
                }

                detail.appendChild(list);
                document.getElementById('detailsList').appendChild(detail);
            }
        })
    
}



let tfidfButton = document.getElementById("tfidf");
tfidfButton.addEventListener("click", showtfidf);

