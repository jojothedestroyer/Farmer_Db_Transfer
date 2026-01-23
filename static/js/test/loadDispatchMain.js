import { initializeApp } from "https://www.gstatic.com/firebasejs/11.4.0/firebase-app.js";
import { getDatabase, ref, set, get, query, orderByChild, equalTo, update, push, remove } from "https://www.gstatic.com/firebasejs/11.4.0/firebase-database.js";
import { getAuth, signInAnonymously, onAuthStateChanged } from "https://www.gstatic.com/firebasejs/11.4.0/firebase-auth.js";

// Firebase configuration
const firebaseConfig = {
    apiKey: "AIzaSyBZTB_mN_gIb6mqeM8nid4x83oKRehmFKo",
    authDomain: "farmer-project-sync.firebaseapp.com",
    databaseURL: "https://farmer-project-sync-default-rtdb.firebaseio.com",
    projectId: "farmer-project-sync",
    storageBucket: "farmer-project-sync.firebasestorage.app",
    messagingSenderId: "1366353203",
    appId: "1:1366353203:web:fa29fd29cc326a0d63ca46"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const db = getDatabase(app);
const auth = getAuth(app);
const dispatch = "Dispatch-Of-Dried-Nutmeg";
const stations = ["Grenville", "Hermitage", "Marli", "Union", "Gouyave", "Victoria"];





document.getElementById('createUserBtn').addEventListener('click', async () => {
    const userName = document.getElementById('userStationInput').value;
    const station = document.getElementById('userStationInput').value;

    if (!userName) {
        alert("Please enter your name.");
        return;
    }

    await createUser(userName, station);
});


async function handleStationArray() {

    for (const station of stations) {

        await getExtStationData(stationName)
    }
}
async function getExtStationData(stationName) {
    const existingStation = await findStation(stationName);
    if (existingStation) {
        addExtDispatchData(stationName);

    } else {
        console.log(existingStation + "  not yet created")
    }
}



async function addExtDispatchData(stationName) {

    await loadDataFromFirebase(stationName);

}




async function loadDataFromFirebase(stationName) {
    console.log("Loading data from Firebase...");
    const userRef = ref(db, `Users/${customUserId}/models`);
    const snapshot = await get(userRef);

    if (snapshot.exists()) {
        const data = snapshot.val();
        for (const modelName in data) {
            const modelData = data[modelName];
            console.log(`Loading ${modelName} from Firebase`);
            await loadModelToIndexedDB(modelName, modelData);
        }
        console.log("Data successfully loaded from Firebase.");
    } else {
        console.log("No data found in Firebase.");
    }
}




function initializeIndexedDB() {
    return new Promise((resolve, reject) => {
        const dbVersion = 2; // Increment this number if you change the schema
        var request = indexedDB.open("ExternalDispatches", dbVersion);

        request.onupgradeneeded = function (event) {
            var db = event.target.result;
            console.log("Database upgrade needed. Creating object stores...");

            const modelNames = [
                "Dispatch-Of-Dried-Nutmeg",
            ];

            modelNames.forEach((modelName) => {
                if (!db.objectStoreNames.contains(modelName)) {
                    console.log(`Creating object store: ${modelName}`);
                    db.createObjectStore(modelName, { keyPath: "id" }); // Store data by 'id'
                } else {
                    console.log(`Object store already exists: ${modelName}`);
                }
            });
        };

        request.onsuccess = function (event) {
            console.log("IndexedDB initialized successfully.");
            resolve(event.target.result);
        };

        request.onerror = function (event) {
            console.error("Error opening IndexedDB:", event);
            reject("Error opening IndexedDB:", event);
        };
    });
}











async function getIndexedDBData() {
    const db = await initializeIndexedDB();
    return new Promise((resolve, reject) => {


        const transaction = db.transaction(dispatch, "readonly");
        const store = transaction.objectStore(dispatch);
        const request = store.getAll();

        request.onsuccess = function () {
            allData.push({ dispatch, data: request.result });
            if (allData.length === dispatch.length) {
                resolve(allData);
            }
        };

        request.onerror = function () {
            reject("Error reading data from IndexedDB");
        };
    });
}



async function loadModelToIndexedDB(modelName, modelData) {
    const db = await initializeIndexedDB();
    const transaction = db.transaction(modelName, "readwrite");
    const store = transaction.objectStore(modelName);


    if (Array.isArray(modelData)) {
        for (const item of modelData) {
            if (!item || item.id == null) {
                console.error(`Item is missing 'id' field for model ${modelName}:`, item);
                continue;
            }

            let newItem = { ...item };

            // Ensure ID is unique
            while (await idExists(store, newItem.id)) {
                newItem.id += 1;
            }

            store.put(newItem); // Add or update the record
        }
    }


    // Check if modelData is an object (but not an array)
    else if (modelData && typeof modelData === 'object') {
        // If it's an object, convert it to an array of its values and iterate
        for (const item of Object.values(modelData)) {
            if (!item || item.id == null) {
                console.error(`Item is missing 'id' field for model ${modelName}:`, item);
                continue;
            }

            let updatedItem = { ...item };

            // Increment ID until unique
            while (await idExists(store, updatedItem.id)) {
                updatedItem.id += 1;
            }

            store.put(updatedItem); // Add or update the record
        }

    } else {
        // Handle other cases where modelData is neither an array nor an object
        console.error(`Unexpected modelData type for ${modelName}:`, modelData);
    }
}

function idExists(store, id) {
    return new Promise((resolve, reject) => {
        const request = store.get(id);

        request.onsuccess = () => {
            resolve(!!request.result);
        };

        request.onerror = () => {
            reject(request.error);
        };
    });
}



// async function syncDataWithFirebase(customUserId) {
//     disableUserInteraction(); // Disable user interaction while syncing
//     showLoadingSpinner(true); // Show the loading spinner
//     console.log("Syncing data with Firebase for user:", customUserId);
//     const indexedDBData = await getIndexedDBData();
//     await loadDataFromFirebase(customUserId);

//     if (indexedDBData.length === 0) {
//         console.log("IndexedDB is empty. Loading data from Firebase...");
//         await loadDataFromFirebase(customUserId);
//     } else {
//         console.log("IndexedDB contains data. Uploading to Firebase...");
//         await uploadDataToFirebase(customUserId, indexedDBData);

//         console.log("Syncing IndexedDB with Firebase...");
//         await syncIndexedDBWithFirebase(customUserId);
//     }
//     hideLoadingSpinner(); // Hide the loading spinner
//     enableUserInteraction(); // Re-enable user interaction after syncing
// }





async function findStation(stationName) {
    // Query Firebase to find a user by name
    const dataRef = ref(db, "Users");
    const stationQuery = query(dataRef, orderByChild("name"), equalTo(stationName));
    const snapshot = await get(stationQuery);

    if (snapshot.exists()) {
        // Return the first matching user's customUserId
        const stationData = snapshot.val();
        const StationId = Object.keys(stationData)[0];
        console.log("Station found in Firebase with StationId:", StationId);
        return { StationId };
    } else {
        console.log("No Station found in Firebase.");
        return null; // No user found
    }
}














async function loadDataFromFirebase(customUserId) {
    console.log("Loading data from Firebase...");
    const userRef = ref(db, `Users/${customUserId}/models`);
    const snapshot = await get(userRef);

    if (snapshot.exists()) {
        const data = snapshot.val();
        for (const modelName in data) {
            const modelData = data[modelName];
            console.log(`Loading ${modelName} from Firebase`);
            await loadModelToIndexedDB(modelName, modelData);
        }
        console.log("Data successfully loaded from Firebase.");
    } else {
        console.log("No data found in Firebase.");
    }
}

async function loadModelToIndexedDB(modelName, modelData) {
    const db = await initializeIndexedDB();
    const transaction = db.transaction(modelName, "readwrite");
    const store = transaction.objectStore(modelName);
    // Log the modelData type and content for debugging purposes
    console.log(`modelData for ${modelName}:`, modelData);
    console.log(`Type of modelData for ${modelName}:`, typeof modelData);
    // Check if modelData is an array
    if (Array.isArray(modelData)) {
        modelData.forEach(item => {
            // Ensure that the item has the necessary 'id' field
            if (item && item.id) {
                store.put(item); // Add or update the record in IndexedDB
            } else {
                console.error(`Item is missing 'id' field for model ${modelName}:`, item);
            }
        });
    }
    // Check if modelData is an object (but not an array)
    else if (modelData && typeof modelData === 'object') {
        // If it's an object, convert it to an array of its values and iterate
        Object.values(modelData).forEach(item => {
            // Ensure that the item has the necessary 'id' field
            if (item && item.id) {
                store.put(item); // Add or update the record in IndexedDB
            } else {
                console.error(`Item is missing 'id' field for model ${modelName}:`, item);
            }
        });
    } else {
        // Handle other cases where modelData is neither an array nor an object
        console.error(`Unexpected modelData type for ${modelName}:`, modelData);
    }
}

























































async function findUserByName(userName) {
    // Query Firebase to find a user by name
    const usersRef = ref(db, "Users");
    const userQuery = query(usersRef, orderByChild("name"), equalTo(userName));
    const snapshot = await get(userQuery);

    if (snapshot.exists()) {
        // Return the first matching user's customUserId
        const userData = snapshot.val();
        const customUserId = Object.keys(userData)[0];
        console.log("User found in Firebase with customUserId:", customUserId);
        return { customUserId };
    } else {
        console.log("No user found in Firebase.");
        return null; // No user found
    }
}

async function findUserByName(userName) {
    // Query Firebase to find a user by name
    const usersRef = ref(db, "Users");
    const userQuery = query(usersRef, orderByChild("name"), equalTo(userName));
    const snapshot = await get(userQuery);

    if (snapshot.exists()) {
        // Return the first matching user's customUserId
        const userData = snapshot.val();
        const customUserId = Object.keys(userData)[0];
        console.log("User found in Firebase with customUserId:", customUserId);
        return { customUserId };
    } else {
        console.log("No user found in Firebase.");
        return null; // No user found
    }
}

function generateCustomUserId(userName) {
    // Generate a unique ID based on the username and a random string
    const randomString = Math.random().toString(36).substring(2, 10);
    return `${userName}-${randomString}`;
}

