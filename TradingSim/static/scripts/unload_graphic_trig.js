const add_invisible = function(elementID) {
    var loadingModal = document.getElementById(elementID);
    var xhr = new XMLHttpRequest();
    xhr.open("GET", window.location.href);
    xhr.onload = function() {
        loadingModal.classList.add("invisible")
    };
    xhr.onerror = function() {
        loadingModal.classList.add("invisible")
    };
    xhr.send();
}

document.addEventListener("DOMContentLoaded", ()=>{add_invisible("loadingGraphic")});

window.addEventListener("beforeunload", ()=>{setTimeout(()=>{add_invisible("loadingGraphic")}, 1000)});