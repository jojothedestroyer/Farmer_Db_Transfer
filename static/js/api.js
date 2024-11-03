
// Check if the browser is online
function isOnline() {
    return navigator.onLine;
}

// Function to retrieve data from IndexedDB
function getDataFromIndexedDB() {
    const openRequest = indexedDB.open('myDatabase', 1);

    return new Promise((resolve, reject) => {
        openRequest.onsuccess = function (event) {
            const db = event.target.result;
            const transaction = db.transaction(['myData'], 'readonly');
            const objectStore = transaction.objectStore('myData');

            const getRequest = objectStore.getAll();

            getRequest.onsuccess = function (event) {
                const data = event.target.result;
                resolve(data);
            };

            getRequest.onerror = function (event) {
                reject(event.target.error);
            };
        };

        openRequest.onerror = function (event) {
            reject(event.target.error);
        };
    });
}

// Function to fetch data from the Django API
function fetchDataFromDjangoAPI() {
    return fetch('api/Worker/')  // Replace with your actual API endpoint URL
        .then(response => response.json())
        .then(data => {
            // Store the retrieved data in IndexedDB
            saveDataToIndexedDB(data);
            return data;
        });
}

// Function to handle data retrieval based on network status
function retrieveData() {
    if (isOnline()) {
        return fetchDataFromDjangoAPI();
    } else {
        return getDataFromIndexedDB();
    }
}

// Example of how to use the retrieveData function
retrieveData()
    .then(data => {
        // Use the retrieved data in your PWA
        console.log(data);
    })
    .catch(error => {
        console.error('Error retrieving data:', error);
    });



function fetchDataFromIndexedDB() {
    const openRequest = indexedDB.open('myDatabase', 1);

    openRequest.onsuccess = function (event) {
        const db = event.target.result;
        const transaction = db.transaction(['myData'], 'readonly');
        const objectStore = transaction.objectStore('myData');

        const request = objectStore.getAll();

        request.onsuccess = function (event) {
            const data = request.result;
            if (data && data.length > 0) {
                // Use the retrieved data (e.g., populate the form)
                // Example: populateFormWithData(data);
            }
        };
    };
}




// JavaScript code in your PWA's script file (e.g., fetch-and-store-data.js)
function loginFromIndexedDB(form) {
    const openRequest = indexedDB.open('myDatabase', 1);

    openRequest.onsuccess = function (event) {
        const db = event.target.result;
        const transaction = db.transaction(['myData'], 'readonly');
        const objectStore = transaction.objectStore('myData');

        const Nutmeg_ID_No = form.elements.Nutmeg_ID_No.value;
        const Worker_ID_No = form.elements.Worker_ID_No.value;

        const request = objectStore.getAll();

        request.onsuccess = function (event) {
            const data = request.result;
            const user = data.find(item => item.Nutmeg_ID_No === Nutmeg_ID_No && item.Worker_ID_No === Worker_ID_No);

            if (user) {
                // Perform the login logic here (e.g., set session variables)
                // You can also redirect the user if the login is successful
                request.session['Worker_ID_No'] = user.Worker_ID_No;
                request.session['Nutmeg_ID_No'] = user.Nutmeg_ID_No;
                window.location.href = '/table001/';
            } else {
                // Handle login failure (e.g., show an error message)
                alert('Invalid username or password.');
            }
        };
    };
}

// Add an event listener for the form submission
document.getElementById('form').addEventListener('submit', function (event) {
    event.preventDefault(); // Prevent the default form submission

    // Call the login function with the form data
    loginFromIndexedDB(this);
});





