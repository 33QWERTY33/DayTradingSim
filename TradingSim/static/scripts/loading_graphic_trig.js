document.addEventListener("DOMContentLoaded", function() {
    var loadDataBtn = document.getElementById("loadModalTrigger");
    loadDataBtn.addEventListener("click", function() {
        var loadingModal = document.getElementById("loadingGraphic");
        var xhr = new XMLHttpRequest();
        // XML to manipulate only a portion of the HTTP without reloading the entire page
        xhr.open("GET", window.location.href);
        xhr.onload = function() {
            loadingModal.classList.remove("invisible")
        };
        xhr.onerror = function() {
            loadingModal.classList.remove("invisible")
        };
        xhr.send();
        // send request to remove invisible from class list for the modal (make it visible)
    });
});