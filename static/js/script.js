document.addEventListener("DOMContentLoaded", () => {
    const subscribeBtn = document.getElementById("subscribeBtn");
    const emailInput = document.getElementById("email");
    const successMessage = document.getElementById("successMessage");
    const errorMessage = document.getElementById("errorMessage");
    const closeBtn = document.getElementById("closeSubscription");
    const subscriptionForm = document.getElementById("subscriptionForm");

    // Close button functionality
    closeBtn.addEventListener("click", () => {
        subscriptionForm.style.display = "none";
    });

    // Subscribe button functionality
    subscribeBtn.addEventListener("click", (e) => {
        e.preventDefault();
        const email = emailInput.value.trim();

        if (validateEmail(email)) {
            // Send email to the backend
            fetch("http://127.0.0.1:8000/api/save_email/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ email: email }),
            })
                .then((response) => response.json())
                .then((data) => {
                    if (data.success) {
                        successMessage.style.display = "block";
                        errorMessage.style.display = "none";
                        emailInput.value = ""; // Clear input
                    } else {
                        errorMessage.style.display = "block";
                        errorMessage.textContent = data.message;
                        successMessage.style.display = "none";
                    }
                })
                .catch((error) => {
                    console.error("Error:", error);
                    errorMessage.style.display = "block";
                    errorMessage.textContent = "An error occurred. Please try again.";
                });
        } else {
            errorMessage.style.display = "block";
            successMessage.style.display = "none";
        }
    });

    function validateEmail(email) {
        const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return regex.test(email);
    }
});
