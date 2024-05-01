document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("submitButton").addEventListener("click", function(event) {
        event.preventDefault()
        
        var form = document.getElementById("order-form");
        console.log("SUBMITTING FORM...")
        form.submit();
    });

    // function triggerFormSubmission() {
    //     var submitButton = document.getElementById("submitButton");
    //     var clickEvent = new MouseEvent("click", {
    //         bubbles: true,
    //         cancelable: true,
    //         view: window
    //     });
    //     submitButton.dispatchEvent(clickEvent);
    // }
});