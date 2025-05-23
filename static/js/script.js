// static/js/script.js

document.addEventListener("DOMContentLoaded", function () {
    console.log("Todo App JS loaded.");

    // Optional: Alert user when they click "Get Started"
    const startBtn = document.querySelector('.btn');
    if (startBtn) {
        startBtn.addEventListener('click', () => {
            alert("Let's start managing your tasks!");
        });
    }
});
