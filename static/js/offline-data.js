// offline-data.js

// Initialize Dexie database
const db = new Dexie('myDatabase');
db.version(1).stores({
    items: '++id,name', // Define your data schema here
});

// Function to fetch and store data
async function fetchDataAndStore() {
    try {
        const response = await fetch('/api/data/'); // Replace with your API endpoint
        const data = await response.json();

        // Store data in IndexedDB
        await db.items.bulkPut(data);
    } catch (error) {
        console.error('Error fetching and storing data:', error);
    }
}

// Function to retrieve data from IndexedDB
async function getDataFromDB() {
    try {
        return await db.items.toArray();
    } catch (error) {
        console.error('Error retrieving data from IndexedDB:', error);
    }
}





// offline-data.js

// ... Other code ...

// Function to fetch and store data
async function fetchDataAndStore() {
    try {
        const response = await fetch('/api/Farmer/'); // Replace with your API endpoint
        const data = await response.json();

        // Store data in IndexedDB
        await db.items.bulkPut(data);
        
        // Refresh the displayed data
        displayData();
    } catch (error) {
        console.error('Error fetching and storing data:', error);
    }
}

// ... Other code ...

