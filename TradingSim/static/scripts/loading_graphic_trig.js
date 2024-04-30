document.addEventListener("DOMContentLoaded", function() {
    var loadDataBtn = document.getElementById("loadModalTrigger");
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