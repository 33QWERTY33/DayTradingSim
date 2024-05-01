document.addEventListener("DOMContentLoaded", function() {
    var loadDataBtn = document.getElementById("quickLoadModalTrigger");
    loadDataBtn.addEventListener("click", function() {
        var loadingModal = document.getElementById("loadingGraphic");
        var xhr = new XMLHttpRequest();
        xhr.open("GET", window.location.href);
        xhr.onload = function() {
            loadingModal.classList.remove("invisible")
        };
        xhr.onerror = function() {
            loadingModal.classList.remove("invisible")
        };
        xhr.send();
    });
});

// seperated loading_graphic_trig.js and this file so they could be loaded more selectively to avoid errors from javascript not finding elements by id