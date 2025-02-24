// Wait for 3 seconds, then fade out and remove alert messages.
setTimeout(function () {
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(function (alert) {
        alert.style.transition = "opacity 0.5s ease";
        alert.style.opacity = "0";
        setTimeout(function () {
            alert.remove();
        }, 500);
    });
}, 3000);
