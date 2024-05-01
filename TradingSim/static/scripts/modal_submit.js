document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("submitButton").addEventListener("click", function(event) {
        event.preventDefault()
        // It already has its own click event tied to that button, so I'm just going to stop that to be safe
        
        var form = document.getElementById("order-form");
        form.submit();
    });
});