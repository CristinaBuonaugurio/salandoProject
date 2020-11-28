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