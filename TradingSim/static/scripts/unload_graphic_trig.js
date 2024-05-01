const add_invisible = function() {
    var loadingModal = document.getElementById("loadingGraphic");
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
document.addEventListener("DOMContentLoaded", ()=>{add_invisible()});

window.addEventListener("beforeunload", ()=>{setTimeout(()=>{add_invisible()}, 1200)}); //CLUNKY!!

// unloading the stupid loading animation thing

// ##############################################################   WIP   ##############################################################
// const add_invisible_onclick = function(elementID) {
//     var loadingModal = document.getElementById("loadingGraphic");
//     var unload_graphic_btn = document.getElementById(elementID)
//     unload_graphic_btn.addEventListener("click", function() {
//         var xhr = new XMLHttpRequest();
//         xhr.open("GET", window.location.href);
//         xhr.onload = function() {
//             loadingModal.classList.add("invisible")
//         };
//         xhr.onerror = function() {
//             loadingModal.classList.add("invisible")
//         };
//         xhr.send();
//     })
// }

// document.addEventListener("DOMContentLoaded", ()=>{add_invisible_onclick("unloadModalNoBtn")})

// document.addEventListener("DOMContentLoaded", ()=>{add_invisible_onclick("unloadModalXBtn")})
// ##############################################################   WIP   ##############################################################
