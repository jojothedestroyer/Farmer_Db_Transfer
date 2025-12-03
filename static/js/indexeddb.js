// const modelNames = ['Worker', 'Farmer', 'DriedA', 'DriedB', 'FloatA', 'FloatB', 'Quaility', 'visit', 'In-House-Drying', 'Dispatch-Of-Dried-Nutmeg', 'Dispatch-Of-Green', 'Cracking-Summary', 'Floation-Summary', 'Package-Ciontrol', 'Editors', 'Labour-support', 'Training-support', 'land-info', 'Land-Tenur', 'Nutmeg-Trees', 'Nutmeg-Variety', 'Other-Crops', 'Coconut-Trees', 'Citrus-Mango-Trees', 'Other-Spices-Trees', 'Other-Seasoning-Trees', 'Other-Crops-Cultivated', 'Condition', 'Nutmeg-Land', 'Nutmeg-Frequency', 'Potential-Risks', 'Road-Access', 'Food-Safety-and-Quality', 'Farm-Water-Source', 'Farm-House', 'inspector-symmary', 'Policy','Sanitation-A','Sanitation-B','Sanitation-C','Cracking_Schedule','Assorting_Log',
// 'Extractor_Log',
// 'Fumigation_Log','Shelves'];

// function deleteDatabase() {
//     return new Promise((resolve, reject) => {
//         const request = indexedDB.deleteDatabase('GCNA');

//         request.onsuccess = function () {
//             resolve();
//         };

//         request.onerror = function (event) {
//             reject(event.target.error);
//         };
//     });
// }

// function openIndexedDBConnection() {
//     return new Promise((resolve, reject) => {
//         const request = indexedDB.open('GCNA', 2);

//         request.onupgradeneeded = function (event) {
//             const db = event.target.result;
//             modelNames.forEach(modelName => {
//                 if (!db.objectStoreNames.contains(modelName)) {
//                     db.createObjectStore(modelName, { keyPath: 'id' });
//                 }
//             });
//         };

//         request.onsuccess = function (event) {
//             resolve(event.target.result);
//         };

//         request.onerror = function (event) {
//             reject(event.target.error);
//         };
//     });
// }

// function fetchDataAndStore(db, modelName) {
//     return new Promise((resolve, reject) => {
//         fetch(`/api/${modelName}/`)
//             .then(response => response.json())
//             .then(data => {
//                 const transaction = db.transaction(modelName, 'readwrite');
//                 const objectStore = transaction.objectStore(modelName);
//                 data.forEach(item => {
//                     objectStore.put(item);
//                 });

//                 transaction.oncomplete = function () {
//                     resolve();
//                 };
//             })
//             .catch(error => {
//                 console.error('Error fetching data for model:', modelName, error);
//                 reject(error);
//             });
//     });
// }

// deleteDatabase()
//     .then(() => openIndexedDBConnection())
//     .then(db => Promise.all(modelNames.map(modelName => fetchDataAndStore(db, modelName))))
//     .then(() => console.log('All models stored successfully.'))
//     .catch(error => console.error('Error storing models:', error));










// // , 'Policy/<int:id>
// const modelNames = ['Worker', 'Farmer', 'DriedA', 'DriedB', 'FloatA', 'FloatB', 'Quaility', 'visit', 'In-House-Drying', 'Dispatch-Of-Dried-Nutmeg', 'Dispatch-Of-Green', 'Cracking-Summary', 'Floation-Summary', 'Package-Ciontrol', 'Editors', 'Labour-support', 'Training-support', 'land-info', 'Land-Tenur', 'Nutmeg-Trees', 'Nutmeg-Variety', 'Other-Crops', 'Coconut-Trees', 'Citrus-Mango-Trees', 'Other-Spices-Trees', 'Other-Seasoning-Trees', 'Other-Crops-Cultivated', 'Condition', 'Nutmeg-Land', 'Nutmeg-Frequency', 'Potential-Risks', 'Road-Access', 'Food-Safety-and-Quality', 'Farm-Water-Source', 'Farm-House', 'inspector-symmary', 'Policy','Sanitation-A','Sanitation-B','Sanitation-C','Cracking_Schedule','Assorting_Log',
// 'Extractor_Log',
// 'Fumigation_Log','Shelves'];


// function deleteDatabase(dbName) {
//     return new Promise((resolve, reject) => {
//         const request = indexedDB.deleteDatabase(dbName);


//         request.onsuccess = function () {
//             resolve();
//         };


//         request.onerror = function (event) {
//             reject(event.target.error);
//         };
//     });
// }


// function openIndexedDBConnection(dbName) {
//     return new Promise((resolve, reject) => {
//         const request = indexedDB.open(dbName, 2);


//         request.onupgradeneeded = function (event) {
//             const db = event.target.result;
//             modelNames.forEach(modelName => {
//                 db.createObjectStore(modelName, { keyPath: 'id' });
//             });
//         };


//         request.onsuccess = function (event) {
//             resolve(event.target.result);
//         };


//         request.onerror = function (event) {
//             reject(event.target.error);
//         };
//     });
// }


// function fetchDataAndStore(db, modelName) {
//     return new Promise((resolve, reject) => {
//         fetch(`/api/${modelName}/`)
//             .then(response => response.json())
//             .then(data => {
//                 const transaction = db.transaction(modelName, 'readwrite');
//                 const objectStore = transaction.objectStore(modelName);
//                 data.forEach(item => {
//                     objectStore.put(item);
//                 });


//                 transaction.oncomplete = function () {
//                     resolve();
//                 };
//             })
//             .catch(error => {
//                 console.error('Error fetching data for model:', modelName, error);
//                 reject(error);
//             });
//     });
// }


// // Create "GCNA" database
// const gcnaDBName = 'GCNA';


// deleteDatabase(gcnaDBName)
//     .then(() => openIndexedDBConnection(gcnaDBName))
//     .then(db => Promise.all(modelNames.map(modelName => fetchDataAndStore(db, modelName))))
//     .then(() => console.log(`Database "${gcnaDBName}" created successfully with data.`))
//     .catch(error => console.error(`Error creating database "${gcnaDBName}":`, error));


// // Create "DELETED" database
// const deletedDBName = 'DELETED';


// deleteDatabase(deletedDBName)
//     .then(() => openIndexedDBConnection(deletedDBName))
//     .then(db => {
//         // Close the connection to "DELETED" to ensure it is created with empty object stores
//         db.close();
//         console.log(`Database "${deletedDBName}" created successfully with empty object stores.`);
//     })
//     .catch(error => console.error(`Error creating database "${deletedDBName}":`, error));



//indexeddb.js

// const modelNames = ['Worker', 'Farmer', 'DriedA', 'DriedB', 'FloatA', 'FloatB', 'Quaility', 'visit', 'In-House-Drying', 'Dispatch-Of-Dried-Nutmeg', 'Dispatch-Of-Green', 'Cracking-Summary', 'Floation-Summary', 'Package-Ciontrol', 'Editors', 'Labour-support', 'Training-support', 'land-info', 'Land-Tenur', 'Nutmeg-Trees', 'Nutmeg-Variety', 'Other-Crops', 'Coconut-Trees', 'Citrus-Mango-Trees', 'Other-Spices-Trees', 'Other-Seasoning-Trees', 'Other-Crops-Cultivated', 'Condition', 'Nutmeg-Land', 'Nutmeg-Frequency', 'Potential-Risks', 'Road-Access', 'Food-Safety-and-Quality', 'Farm-Water-Source', 'Farm-House', 'inspector-symmary', 'Policy','Sanitation-A','Sanitation-B','Sanitation-C','Cracking_Schedule','Assorting_Log',
// 'Extractor_Log',
// 'Fumigation_Log','Shelves','W_Shelves','M_Shelves','W_Shelves_Dried','M_Shelves_Dried','Vehicle_Inspection','Final_Weight_Inspection','Final_Weight_Inspection_fields','Dispatch_Of_Dried_Nutmeg_Rec','Dispatch_Of_Green_Nutmeg_Rec','Mace_Dispatched','Mace_Purchase','Mace_Dispatched_Rec'];



// function deleteDatabase(dbName) {
//     return new Promise((resolve, reject) => {
//         const request = indexedDB.deleteDatabase(dbName);


//         request.onsuccess = function () {
//             resolve();
//         };


//         request.onerror = function (event) {
//             reject(event.target.error);
//         };
//     });
// }


// function openIndexedDBConnection(dbName) {
//     return new Promise((resolve, reject) => {
//         const request = indexedDB.open(dbName, 2);


//         request.onupgradeneeded = function (event) {
//             const db = event.target.result;
//             modelNames.forEach(modelName => {
//                 db.createObjectStore(modelName, { keyPath: 'id' });
//             });
//         };


//         request.onsuccess = function (event) {
//             resolve(event.target.result);
//         };


//         request.onerror = function (event) {
//             reject(event.target.error);
//         };
//     });
// }


// function fetchDataAndStore(db, modelName) {
//     return new Promise((resolve, reject) => {
//         fetch(`/api/${modelName}/`)
//             .then(response => response.json())
//             .then(data => {
//                 const transaction = db.transaction(modelName, 'readwrite');
//                 const objectStore = transaction.objectStore(modelName);
//                 data.forEach(item => {
//                     objectStore.put(item);
//                 });


//                 transaction.oncomplete = function () {
//                     resolve();
//                 };
//             })
//             .catch(error => {
//                 console.error('Error fetching data for model:', modelName, error);
//                 reject(error);
//             });
//     });
// }


// // Create "GCNA" database
// const gcnaDBName = 'GCNA';


// deleteDatabase(gcnaDBName)
//     .then(() => openIndexedDBConnection(gcnaDBName))
//     .then(db => Promise.all(modelNames.map(modelName => fetchDataAndStore(db, modelName))))
//     .then(() => console.log(`Database "${gcnaDBName}" created successfully with data.`))
//     .catch(error => console.error(`Error creating database "${gcnaDBName}":`, error));


// // Create "DELETED" database
// const deletedDBName = 'DELETED';


// deleteDatabase(deletedDBName)
//     .then(() => openIndexedDBConnection(deletedDBName))
//     .then(db => {
//         // Close the connection to "DELETED" to ensure it is created with empty object stores
//         db.close();
//         console.log(`Database "${deletedDBName}" created successfully with empty object stores.`);
//     })
//     .catch(error => console.error(`Error creating database "${deletedDBName}":`, error));










const modelNamesSection1 = ['Worker', 'Farmer', 'DriedA', 'DriedB', 'FloatA', 'FloatB', 'Quaility', 'visit', 'In-House-Drying', 'Dispatch-Of-Dried-Nutmeg', 'Dispatch-Of-Green', 'Cracking-Summary', 'Floation-Summary', 'Package-Ciontrol', 'Editors', 'Labour-support', 'Training-support', 'land-info', 'Land-Tenur', 'Nutmeg-Trees', 'Nutmeg-Variety', 'Other-Crops', 'Coconut-Trees', 'Citrus-Mango-Trees', 'Other-Spices-Trees', 'Other-Seasoning-Trees', 'Other-Crops-Cultivated', 'Condition', 'Nutmeg-Land', 'Nutmeg-Frequency', 'Potential-Risks', 'Road-Access', 'Food-Safety-and-Quality', 'Farm-Water-Source', 'Farm-House', 'inspector-symmary', 'Policy','Sanitation-A','Sanitation-B','Sanitation-C','Cracking_Schedule','Assorting_Log',
    'Extractor_Log',
    'Fumigation_Log','Shelves','W_Shelves','M_Shelves','W_Shelves_Dried','M_Shelves_Dried','Vehicle_Inspection','Final_Weight_Inspection','Final_Weight_Inspection_fields','Dispatch_Of_Dried_Nutmeg_Rec','Dispatch_Of_Green_Nutmeg_Rec','Cracking_Extraction_Summary'];

async function better_transferIndexedDBData() {
    const request = indexedDB.open('GCNA', 2);

    return new Promise((resolve, reject) => {
        request.onerror = function(event) {
            console.error('Error opening IndexedDB:', event.target.error);
            reject(new Error('Error opening IndexedDB'));
        };

        request.onsuccess = function(event) {
            const db = event.target.result;
            const transactionPromises = [];

            modelNamesSection1.forEach(function(modelName) {
                try {
                    if (db.objectStoreNames.contains(modelName)) {
                        const transaction = db.transaction(modelName, 'readonly');
                        const objectStore = transaction.objectStore(modelName);
                        const getRequest = objectStore.getAll();

                        getRequest.onsuccess = function(event) {
                            const data = event.target.result;
                            data.forEach(function(item) {
                                transactionPromises.push(better_sendDataToDjango(item, modelName));
                            });
                        };
                    } else {
                        console.warn(`Object store "${modelName}" not found in IndexedDB.`);
                    }
                } catch (error) {
                    console.error(`Error processing object store "${modelName}":`, error);
                }
            });

            Promise.all(transactionPromises)
                .then(() => {
                    resolve();
                })
                .catch(error => {
                    reject(error);
                });
        };
    });
}

function better_sendDataToDjango(item, modelName) {
    return new Promise((resolve, reject) => {
        const xhr = new XMLHttpRequest();
        xhr.open('POST', '/check-and-add/', true);
        xhr.setRequestHeader('Content-Type', 'application/json');
        xhr.onreadystatechange = function() {
            if (xhr.readyState === XMLHttpRequest.DONE) {
                if (xhr.status === 200) {
                    console.log('Entry added successfully for model:', modelName);
                    resolve();
                } else {
                    console.error('Error adding entry for model:', modelName, xhr.statusText);
                    reject(new Error(`Error adding entry for model: ${modelName}, Status: ${xhr.status}, Message: ${xhr.statusText}`));
                }
            }
        };
        xhr.send(JSON.stringify({model: modelName, data: item}));
    });
}

// Run Section1 first
better_transferIndexedDBData()
    .then(() => {
        console.log('Section1 completed successfully.');
        // After Section1 completes, proceed with Section2
        
        // Section2 remains unchanged from your original code snippet
        const modelNamesSection2 = modelNamesSection1;
        const gcnaDBName = 'GCNA';
        const deletedDBName = 'DELETED';
        
        function deleteDatabase(dbName) {
            return new Promise((resolve, reject) => {
                const request = indexedDB.deleteDatabase(dbName);
        
                request.onsuccess = function () {
                    resolve();
                };
        
                request.onerror = function (event) {
                    reject(event.target.error);
                };
            });
        }
        
        function openIndexedDBConnection(dbName, modelNames) {
            return new Promise((resolve, reject) => {
                const request = indexedDB.open(dbName, 2);
        
                request.onupgradeneeded = function (event) {
                    const db = event.target.result;
                    modelNames.forEach(modelName => {
                        db.createObjectStore(modelName, { keyPath: 'id' });
                    });
                };
        
                request.onsuccess = function (event) {
                    resolve(event.target.result);
                };
        
                request.onerror = function (event) {
                    reject(event.target.error);
                };
            });
        }
        
        function fetchDataAndStore(db, modelName) {
            return new Promise((resolve, reject) => {
                fetch(`/api/${modelName}/`)
                    .then(response => response.json())
                    .then(data => {
                        const transaction = db.transaction(modelName, 'readwrite');
                        const objectStore = transaction.objectStore(modelName);
                        data.forEach(item => {
                            objectStore.put(item);
                        });
        
                        transaction.oncomplete = function () {
                            resolve();
                        };
                    })
                    .catch(error => {
                        console.error('Error fetching data for model:', modelName, error);
                        reject(error);
                    });
            });
        }
        
        // Delete and recreate "GCNA" database
        deleteDatabase(gcnaDBName)
            .then(() => openIndexedDBConnection(gcnaDBName, modelNamesSection2))
            .then(db => Promise.all(modelNamesSection2.map(modelName => fetchDataAndStore(db, modelName))))
            .then(() => console.log(`Database "${gcnaDBName}" created successfully with data.`))
            .catch(error => console.error(`Error creating database "${gcnaDBName}":`, error));
        
        // Delete and create "DELETED" database with empty object stores
        deleteDatabase(deletedDBName)
            .then(() => openIndexedDBConnection(deletedDBName, [])) // Empty modelNames for "DELETED"
            .then(db => {
                db.close(); // Close the connection to finalize creation
                console.log(`Database "${deletedDBName}" created successfully with empty object stores.`);
            })
            .catch(error => console.error(`Error creating database "${deletedDBName}":`, error));
    })
    .catch(error => {
        console.error('Error in Section1:', error);
    });
