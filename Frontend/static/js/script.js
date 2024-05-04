// Function to display the search results
function displaySearchResults(carsData) {
    var searchResultsDiv = document.getElementById("search-results");

    carsData.forEach(function(car) {
        var carTile = document.createElement("div");
        carTile.classList.add("car-tile");

        var carDetails = `
            <div class="car-image">
                <img src="car-image-placeholder.jpg" alt="Car Image">
            </div>
            <div class="car-info">
                <p><strong>Make:</strong> ${car.Make}</p>
                <p><strong>Model:</strong> ${car.Model}</p>
                <p><strong>Year:</strong> ${car.Year}</p>
                <p><strong>Color:</strong> ${car.Color}</p>
                <p><strong>Price:</strong> $${car.Price}</p>
                <p><strong>Mileage:</strong> ${car.Mileage} miles</p>
                <p><strong>New:</strong> ${car.isNew ? "Yes" : "No"}</p>
            </div>
        `;

        carTile.innerHTML = carDetails;
        searchResultsDiv.appendChild(carTile);
    });
}


// Function to fetch the JSON data and display search results
function fetchAndDisplaySearchResults() {
    fetch("car-data.json")
        .then(response => response.json())
        .then(data => displaySearchResults(data))
        .catch(error => console.error("Error fetching data:", error));
}

// Call the function to fetch and display search results when the page loads
window.onload = fetchAndDisplaySearchResults;

// Function to redirect to search-results.html when the search button is clicked
function redirectToSearchResults() {
    window.location.href = "search-results.html";
}
