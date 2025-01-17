const inputFile = document.getElementById("input-file");
const imageView = document.getElementById("img-view");
const predictButton = document.getElementById("predict-button");
const predictionResults = document.querySelector(".prediction-results");

// Handle file selection and show image preview
inputFile.addEventListener("change", uploadImage);

function uploadImage() {
    const file = inputFile.files[0];
    if (file) {
        const imgLink = URL.createObjectURL(file);
        imageView.style.backgroundImage = `url(${imgLink})`;
        imageView.textContent = ""; // Clear the text
        imageView.style.border = "none"; // Remove the border if needed
        predictionResults.style.display = "none";
    }
}

// Predict button event handler to update only the prediction results section
predictButton.addEventListener("click", function() {
    const file = inputFile.files[0];
    if (file) {
        const formData = new FormData();
        formData.append("image", file);

        // Send the image to the Flask server
        fetch("/", {
            method: "POST",
            body: formData
        })
        .then(response => response.json()) // Expect JSON response
        .then(data => {
            // Update the prediction results section with returned HTML fragment
            predictionResults.innerHTML = data.predictions_html;
            predictionResults.style.display = "block"; // Show the prediction results box
        })
        .catch(error => {
            console.error("Error:", error);
            alert("An error occurred while making the prediction.");
        });
    } else {
        alert("Please upload an image before predicting.");
    }
});