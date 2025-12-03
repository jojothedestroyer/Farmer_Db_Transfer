

function populateFormFromIndexedDB() {
    if (navigator.onLine === false) {
        // You are offline, fetch data from IndexedDB and populate the form fields
        const dbPromise = openIndexedDBConnection();
        dbPromise.then(db => {
            // Fetch and populate form fields from IndexedDB
            const transaction = db.transaction('Worker', 'readonly');
            const objectStore = transaction.objectStore('Worker');
            const request = objectStore.get('your_key'); // Replace 'your_key' with the key you want to retrieve

            request.onsuccess = function(event) {
                const result = event.target.result;
                if (result) {
                    // Populate your form fields here
                    document.getElementById('Worker_ID_No').value = result.Worker_ID_No;
                    document.getElementById('Nutmeg_ID_No').value = result.Nutmeg_ID_No;
                }
            };
        }).catch(error => {
            console.error('Error accessing IndexedDB:', error);
        });
    }
}

// Call the function to populate form fields from IndexedDB
populateFormFromIndexedDB();
