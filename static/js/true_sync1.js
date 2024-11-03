





// // // setInterval(activateCode, 1 * 60 * 1000);

// // // function activateCode() {
// // //     var additionalEndpoints = [
// // //         'DriedA', 'DriedB', 'FloatA', 'FloatB', 'Quaility', 'Worker', 'Farmer', 'visit', 'In-House-Drying',
// // //         'Dispatch-Of-Dried-Nutmeg', 'Dispatch-Of-Green', 'Cracking-Summary', 'Floation-Summary',
// // //         'Package-Ciontrol', 'Editors', 'Labour-support', 'Training-support', 'land-info', 'Land-Tenur',
// // //         'Nutmeg-Trees', 'Nutmeg-Variety', 'Other-Crops', 'Coconut-Trees', 'Citrus-Mango-Trees',
// // //         'Other-Spices-Trees', 'Other-Seasoning-Trees', 'Other-Crops-Cultivated', 'Condition',
// // //         'Nutmeg-Land', 'Nutmeg-Frequency', 'Potential-Risks', 'Road-Access', 'Food-Safety-and-Quality',
// // //         'Farm-Water-Source', 'Farm-House', 'inspector-symmary', 'Policy'
// // //     ];
// // //     var openRequest = indexedDB.open('GCNA', 2);

// // //     openRequest.onsuccess = function (e) {
// // //         var db = e.target.result;

// // //         additionalEndpoints.forEach(function (endpoint) {
// // //             var transaction = db.transaction([endpoint]);
// // //             var objectStore = transaction.objectStore(endpoint);
// // //             var getRequest = objectStore.getAll();

// // //             getRequest.onsuccess = function (event) {
// // //                 var results = event.target.result;
// // //                 results.forEach(function (result) {
// // //                     fetch(`/api/${endpoint}2/${result.id}/`, {
// // //                         method: 'GET',
// // //                         headers: {
// // //                             'Content-Type': 'application/json',
// // //                             'X-CSRFToken': getCookie('csrftoken'),
// // //                         },
// // //                     })
// // //                         .then((response) => {
// // //                             if (response.status === 200) {
// // //                                 return response.json().then((data) => {
// // //                                     // Object exists and IDs match, make a PATCH request to update it
// // //                                     return fetch(`/api/${endpoint}2/${result.id}/`, {
// // //                                         method: 'PATCH',
// // //                                         headers: {
// // //                                             'Content-Type': 'application/json',
// // //                                             'X-CSRFToken': getCookie('csrftoken'),
// // //                                         },
// // //                                         body: JSON.stringify(result),
// // //                                     });
// // //                                 });
// // //                             } else {
// // //                                 // Object does not exist in Django, make a POST request to create it
// // //                                 return fetch(`/api/${endpoint}/`, {
// // //                                     method: 'POST',
// // //                                     headers: {
// // //                                         'Content-Type': 'application/json',
// // //                                         'X-CSRFToken': getCookie('csrftoken'),
// // //                                     },
// // //                                     body: JSON.stringify(result),
// // //                                 });
// // //                             }
// // //                         })
// // //                         .then((response) => response.json())
// // //                         .then((data) => {
// // //                             console.log(`Success for ${endpoint}:`, data);
// // //                         })
// // //                         .catch((error) => {
// // //                             console.error(`Error for ${endpoint}:`, error);
// // //                         });
// // //                 });
// // //             };
// // //         });
// // //     };

// // //     function getCookie(name) {
// // //         let cookieValue = null;
// // //         if (document.cookie && document.cookie !== '') {
// // //             let cookies = document.cookie.split(';');
// // //             for (let i = 0; i < cookies.length; i++) {
// // //                 let cookie = cookies[i].trim();
// // //                 if (cookie.substring(0, name.length + 1) === (name + '=')) {
// // //                     cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
// // //                     break;
// // //                 }
// // //             }
// // //         }
// // //         return cookieValue;
// // //     }
// // // }














// // // setInterval(activateCode, 1 * 60 * 1000);

// // // function activateCode() {
// // //     var additionalEndpoints = [
// // //         'DriedA', 'DriedB', 'FloatA', 'FloatB', 'Quaility', 'Worker', 'Farmer', 'visit', 'In-House-Drying',
// // //         'Dispatch-Of-Dried-Nutmeg', 'Dispatch-Of-Green', 'Cracking-Summary', 'Floation-Summary',
// // //         'Package-Ciontrol', 'Editors', 'Labour-support', 'Training-support', 'land-info', 'Land-Tenur',
// // //         'Nutmeg-Trees', 'Nutmeg-Variety', 'Other-Crops', 'Coconut-Trees', 'Citrus-Mango-Trees',
// // //         'Other-Spices-Trees', 'Other-Seasoning-Trees', 'Other-Crops-Cultivated', 'Condition',
// // //         'Nutmeg-Land', 'Nutmeg-Frequency', 'Potential-Risks', 'Road-Access', 'Food-Safety-and-Quality',
// // //         'Farm-Water-Source', 'Farm-House', 'inspector-symmary', 'Policy'
// // //     ];
// // //     var openRequest = indexedDB.open('GCNA', 2);

// // //     openRequest.onsuccess = function (e) {
// // //         var db = e.target.result;

// // //         additionalEndpoints.forEach(function (endpoint) {
// // //             var transaction = db.transaction([endpoint]);
// // //             var objectStore = transaction.objectStore(endpoint);
// // //             var getRequest = objectStore.getAll();

// // //             getRequest.onsuccess = function (event) {
// // //                 var results = event.target.result;
// // //                 results.forEach(function (result) {
// // //                     var isDeletedRequest = indexedDB.open('DELETED');

// // //                     isDeletedRequest.onsuccess = function (event) {
// // //                         var deletedDB = event.target.result;
// // //                         var isDeletedTransaction = deletedDB.transaction([endpoint]);
// // //                         var isDeletedObjectStore = isDeletedTransaction.objectStore(endpoint);
// // //                         var isDeletedGetRequest = isDeletedObjectStore.get(result.id);

// // //                         isDeletedGetRequest.onsuccess = function (event) {
// // //                             var isDeleted = event.target.result;

// // //                             if (!isDeleted) {
// // //                                 // Object is not in the DELETED database, proceed with syncing
// // //                                 fetchAndUpdateDjango(endpoint, result);

// // //                             } else {
// // //                                 // Object is in the DELETED database, delete it from Django
// // //                                 deleteFromDjango(endpoint, result.id);
// // //                             }
// // //                         };
// // //                     };
// // //                 });
// // //             };
// // //         });
// // //     };

// // //     function fetchAndUpdateDjango(endpoint, result) {
// // //         fetch(`/api/${endpoint}2/${result.id}/`, {
// // //             method: 'GET',
// // //             headers: {
// // //                 'Content-Type': 'application/json',
// // //                 'X-CSRFToken': getCookie('csrftoken'),
// // //             },
// // //         })
// // //         .then((response) => {
// // //             if (response.status === 200) {
// // //                 return response.json().then((data) => {
// // //                     // Object exists and IDs match, make a PATCH request to update it
// // //                     return fetch(`/api/${endpoint}2/${result.id}/`, {
// // //                         method: 'PATCH',
// // //                         headers: {
// // //                             'Content-Type': 'application/json',
// // //                             'X-CSRFToken': getCookie('csrftoken'),
// // //                         },
// // //                         body: JSON.stringify(result),
// // //                     });
// // //                 });
// // //             } else {
// // //                 // Object does not exist in Django, make a POST request to create it
// // //                 return fetch(`/api/${endpoint}/`, {
// // //                     method: 'POST',
// // //                     headers: {
// // //                         'Content-Type': 'application/json',
// // //                         'X-CSRFToken': getCookie('csrftoken'),
// // //                     },
// // //                     body: JSON.stringify(result),
// // //                 });
// // //             }
// // //         })
// // //         .then((response) => response.json())
// // //         .then((data) => {
// // //             console.log(`Success for ${endpoint}:`, data);
// // //         })
// // //         .catch((error) => {
// // //             console.error(`Error for ${endpoint}:`, error);
// // //         });
// // //     }

// // //     function deleteFromDjango(endpoint, id) {
// // //         fetch(`/api/${endpoint}2/${id}/`, {
// // //             method: 'DELETE',
// // //             headers: {
// // //                 'Content-Type': 'application/json',
// // //                 'X-CSRFToken': getCookie('csrftoken'),
// // //             },
// // //         })
// // //         .then((response) => {
// // //             if (response.status === 204) {
// // //                 console.log(`Success: Deleted ${endpoint} with ID ${id} from Django.`);
// // //             } else {
// // //                 console.error(`Error: Failed to delete ${endpoint} with ID ${id} from Django.`);
// // //             }
// // //         })
// // //         .catch((error) => {
// // //             console.error(`Error: Failed to delete ${endpoint} with ID ${id} from Django.`, error);
// // //         });
// // //     }

// // //     function getCookie(name) {
// // //         let cookieValue = null;
// // //         if (document.cookie && document.cookie !== '') {
// // //             let cookies = document.cookie.split(';');
// // //             for (let i = 0; i < cookies.length; i++) {
// // //                 let cookie = cookies[i].trim();
// // //                 if (cookie.substring(0, name.length + 1) === (name + '=')) {
// // //                     cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
// // //                     break;
// // //                 }
// // //             }
// // //         }
// // //         return cookieValue;
// // //     }
// // // }











// // // setInterval(activateCode, 1 * 60 * 1000);

// // // function activateCode() {
// // //     var additionalEndpoints = [
// // //         'DriedA', 'DriedB', 'FloatA', 'FloatB', 'Quaility', 'Worker', 'Farmer', 'visit', 'In-House-Drying',
// // //         'Dispatch-Of-Dried-Nutmeg', 'Dispatch-Of-Green', 'Cracking-Summary', 'Floation-Summary',
// // //         'Package-Ciontrol', 'Editors', 'Labour-support', 'Training-support', 'land-info', 'Land-Tenur',
// // //         'Nutmeg-Trees', 'Nutmeg-Variety', 'Other-Crops', 'Coconut-Trees', 'Citrus-Mango-Trees',
// // //         'Other-Spices-Trees', 'Other-Seasoning-Trees', 'Other-Crops-Cultivated', 'Condition',
// // //         'Nutmeg-Land', 'Nutmeg-Frequency', 'Potential-Risks', 'Road-Access', 'Food-Safety-and-Quality',
// // //         'Farm-Water-Source', 'Farm-House', 'inspector-symmary', 'Policy'
// // //     ];

// // //     var openRequest = indexedDB.open('GCNA', 2);

// // //     openRequest.onsuccess = function (e) {
// // //         var db = e.target.result;
// // //         var syncPromises = [];

// // //         additionalEndpoints.forEach(function (endpoint) {
// // //             var transaction = db.transaction([endpoint]);
// // //             var objectStore = transaction.objectStore(endpoint);
// // //             var getRequest = objectStore.getAll();

// // //             getRequest.onsuccess = function (event) {
// // //                 var results = event.target.result;
// // //                 results.forEach(function (result) {
// // //                     syncPromises.push(checkAndSyncWithDjango(endpoint, result));
// // //                 });

// // //                 // Wait for all promises to resolve before proceeding
// // //                 Promise.all(syncPromises).then(() => {
// // //                     console.log('Sync complete.');
// // //                 });
// // //             };
// // //         });
// // //     }

// // //     function checkAndSyncWithDjango(endpoint, result) {
// // //         return new Promise((resolve) => {
// // //             var isDeletedRequest = indexedDB.open('DELETED');

// // //             isDeletedRequest.onsuccess = function (event) {
// // //                 var deletedDB = event.target.result;
// // //                 var isDeletedTransaction = deletedDB.transaction([endpoint]);
// // //                 var isDeletedObjectStore = isDeletedTransaction.objectStore(endpoint);
// // //                 var isDeletedGetRequest = isDeletedObjectStore.get(result.id);

// // //                 isDeletedGetRequest.onsuccess = function (event) {
// // //                     var isDeleted = event.target.result;

// // //                     if (!isDeleted) {
// // //                         // Object is not in the DELETED database, proceed with syncing
// // //                         fetchAndSyncWithDjango(endpoint, result).then(() => {
// // //                             resolve();
// // //                         });
// // //                     } else {
// // //                         // Object is in the DELETED database, delete it from Django
// // //                         deleteFromDjango(endpoint, result.id).then(() => {
// // //                             resolve();
// // //                         });
// // //                     }
// // //                 };
// // //             };
// // //         });
// // //     }

// // //     function fetchAndSyncWithDjango(endpoint, result) {
// // //         fetch(`/api/${endpoint}2/${result.id}/`, {
// // //             method: 'GET',
// // //             headers: {
// // //                 'Content-Type': 'application/json',
// // //                 'X-CSRFToken': getCookie('csrftoken'),
// // //             },
// // //         })
// // //             .then((response) => {
// // //                 if (response.status === 200) {
// // //                     return response.json().then((data) => {
// // //                         // Object exists and IDs match, make a PATCH request to update it
// // //                         return fetch(`/api/${endpoint}2/${result.id}/`, {
// // //                             method: 'PATCH',
// // //                             headers: {
// // //                                 'Content-Type': 'application/json',
// // //                                 'X-CSRFToken': getCookie('csrftoken'),
// // //                             },
// // //                             body: JSON.stringify(result),
// // //                         });
// // //                     });
// // //                 } else {
// // //                     // Object does not exist in Django, make a POST request to create it
// // //                     return fetch(`/api/${endpoint}/`, {
// // //                         method: 'POST',
// // //                         headers: {
// // //                             'Content-Type': 'application/json',
// // //                             'X-CSRFToken': getCookie('csrftoken'),
// // //                         },
// // //                         body: JSON.stringify(result),
// // //                     });
// // //                 }
// // //             })
// // //             .then((response) => response.json())
// // //             .then((data) => {
// // //                 console.log(`Success for ${endpoint}:`, data);
// // //             })
// // //             .catch((error) => {
// // //                 console.error(`Error for ${endpoint}:`, error);
// // //             });

// // //         return new Promise((resolve) => {
// // //             resolve();
// // //         });
// // //     }

// // //     function deleteFromDjango(endpoint, id) {
// // //         return new Promise((resolve) => {
// // //             fetch(`/api/${endpoint}2/${id}/`, {
// // //                 method: 'DELETE',
// // //                 headers: {
// // //                     'Content-Type': 'application/json',
// // //                     'X-CSRFToken': getCookie('csrftoken'),
// // //                 },
// // //             })
// // //                 .then((response) => {
// // //                     if (response.status === 204) {
// // //                         console.log(`Success: Deleted ${endpoint} with ID ${id} from Django.`);
// // //                     } else {
// // //                         console.error(`Error: Failed to delete ${endpoint} with ID ${id} from Django.`);
// // //                     }
// // //                 })
// // //                 .catch((error) => {
// // //                     console.error(`Error: Failed to delete ${endpoint} with ID ${id} from Django.`, error);
// // //                 })
// // //                 .finally(() => {
// // //                     resolve();
// // //                 });
// // //         });
// // //     }

// // //     function getCookie(name) {
// // //         let cookieValue = null;
// // //         if (document.cookie && document.cookie !== '') {
// // //             let cookies = document.cookie.split(';');
// // //             for (let i = 0; i < cookies.length; i++) {
// // //                 let cookie = cookies[i].trim();
// // //                 if (cookie.substring(0, name.length + 1) === (name + '=')) {
// // //                     cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
// // //                     break;
// // //                 }
// // //             }
// // //         }
// // //         return cookieValue;
// // //     }
// // // }








// // // setInterval(activateCode, 1 * 60 * 1000);

// // // function activateCode() {
// // //     var additionalEndpoints = [
// // //         'DriedA', 'DriedB', 'FloatA', 'FloatB', 'Quaility', 'Worker', 'Farmer', 'visit', 'In-House-Drying',
// // //         'Dispatch-Of-Dried-Nutmeg', 'Dispatch-Of-Green', 'Cracking-Summary', 'Floation-Summary',
// // //         'Package-Ciontrol', 'Editors', 'Labour-support', 'Training-support', 'land-info', 'Land-Tenur',
// // //         'Nutmeg-Trees', 'Nutmeg-Variety', 'Other-Crops', 'Coconut-Trees', 'Citrus-Mango-Trees',
// // //         'Other-Spices-Trees', 'Other-Seasoning-Trees', 'Other-Crops-Cultivated', 'Condition',
// // //         'Nutmeg-Land', 'Nutmeg-Frequency', 'Potential-Risks', 'Road-Access', 'Food-Safety-and-Quality',
// // //         'Farm-Water-Source', 'Farm-House', 'inspector-symmary', 'Policy'
// // //     ];

// // //     var openRequest = indexedDB.open('GCNA', 2);

// // //     openRequest.onsuccess = function (e) {
// // //         var db = e.target.result;
// // //         var syncPromises = [];

// // //         additionalEndpoints.forEach(function (endpoint) {
// // //             var transaction = db.transaction([endpoint]);
// // //             var objectStore = transaction.objectStore(endpoint);
// // //             var getRequest = objectStore.getAll();

// // //             getRequest.onsuccess = function (event) {
// // //                 var results = event.target.result;
// // //                 results.forEach(function (result) {
// // //                     syncPromises.push(checkAndSyncWithDjango(endpoint, result));
// // //                 });

// // //                 // Wait for all promises to resolve before proceeding
// // //                 Promise.all(syncPromises).then(() => {
// // //                     console.log('Sync complete.');
// // //                 });
// // //             };
// // //         });
// // //     }

// // //     function checkAndSyncWithDjango(endpoint, result) {
// // //         return new Promise((resolve) => {
// // //             var isDeletedRequest = indexedDB.open('DELETED');

// // //             isDeletedRequest.onsuccess = function (event) {
// // //                 var deletedDB = event.target.result;
// // //                 var isDeletedTransaction = deletedDB.transaction([endpoint]);
// // //                 var isDeletedObjectStore = isDeletedTransaction.objectStore(endpoint);
// // //                 var isDeletedGetRequest = isDeletedObjectStore.get(result.id);

// // //                 isDeletedGetRequest.onsuccess = function (event) {
// // //                     var isDeleted = event.target.result;

// // //                     if (!isDeleted) {
// // //                         // Object is not in the DELETED database, proceed with syncing
// // //                         fetchAndSyncWithDjango(endpoint, result).then(() => {
// // //                             resolve();
// // //                         });
// // //                     } else {
// // //                         // Object is in the DELETED database, delete it from Django
// // //                         deleteFromDjango(endpoint, result.id).then(() => {
// // //                             resolve();
// // //                         });
// // //                     }
// // //                 };
// // //             };
// // //         });
// // //     }

// // //     function fetchAndSyncWithDjango(endpoint, result) {
// // //         return fetch(`/api/${endpoint}2/${result.id}/`, {
// // //             method: 'GET',
// // //             headers: {
// // //                 'Content-Type': 'application/json',
// // //                 'X-CSRFToken': getCookie('csrftoken'),
// // //             },
// // //         })
// // //             .then((response) => {
// // //                 if (response.status === 200) {
// // //                     return response.json().then((data) => {
// // //                         // Object exists and IDs match, make a PATCH request to update it
// // //                         return fetch(`/api/${endpoint}2/${result.id}/`, {
// // //                             method: 'PATCH',
// // //                             headers: {
// // //                                 'Content-Type': 'application/json',
// // //                                 'X-CSRFToken': getCookie('csrftoken'),
// // //                             },
// // //                             body: JSON.stringify(result),
// // //                         });
// // //                     });
// // //                 } else {
// // //                     // Object does not exist in Django, make a POST request to create it
// // //                     return fetch(`/api/${endpoint}/`, {
// // //                         method: 'POST',
// // //                         headers: {
// // //                             'Content-Type': 'application/json',
// // //                             'X-CSRFToken': getCookie('csrftoken'),
// // //                         },
// // //                         body: JSON.stringify(result),
// // //                     });
// // //                 }
// // //             })
// // //             .then((response) => response.json())
// // //             .then((data) => {
// // //                 console.log(`Success for ${endpoint}:`, data);
// // //             })
// // //             .catch((error) => {
// // //                 console.error(`Error for ${endpoint}:`, error);
// // //             });
// // //     }

// // //     function deleteFromDjango(endpoint, id) {
// // //         return fetch(`/api/${endpoint}2/${id}/`, {
// // //             method: 'DELETE',
// // //             headers: {
// // //                 'Content-Type': 'application/json',
// // //                 'X-CSRFToken': getCookie('csrftoken'),
// // //             },
// // //         })
// // //             .then((response) => {
// // //                 if (response.status === 204) {
// // //                     console.log(`Success: Deleted ${endpoint} with ID ${id} from Django.`);
// // //                 } else {
// // //                     console.error(`Error: Failed to delete ${endpoint} with ID ${id} from Django.`);
// // //                 }
// // //             })
// // //             .catch((error) => {
// // //                 console.error(`Error: Failed to delete ${endpoint} with ID ${id} from Django.`, error);
// // //             });
// // //     }

// // //     function getCookie(name) {
// // //         let cookieValue = null;
// // //         if (document.cookie && document.cookie !== '') {
// // //             let cookies = document.cookie.split(';');
// // //             for (let i = 0; i < cookies.length; i++) {
// // //                 let cookie = cookies[i].trim();
// // //                 if (cookie.substring(0, name.length + 1) === (name + '=')) {
// // //                     cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
// // //                     break;
// // //                 }
// // //             }
// // //         }
// // //         return cookieValue;
// // //     }
// // // }








// // // Activate code periodically
// // setInterval(activateCode, 1 * 60 * 1000);

// // function activateCode() {
// //     var additionalEndpoints = [
// //         'DriedA', 'DriedB', 'FloatA', 'FloatB', 'Quaility', 'Worker', 'Farmer', 'visit', 'In-House-Drying',
// //         'Dispatch-Of-Dried-Nutmeg', 'Dispatch-Of-Green', 'Cracking-Summary', 'Floation-Summary',
// //         'Package-Ciontrol', 'Editors', 'Labour-support', 'Training-support', 'land-info', 'Land-Tenur',
// //         'Nutmeg-Trees', 'Nutmeg-Variety', 'Other-Crops', 'Coconut-Trees', 'Citrus-Mango-Trees',
// //         'Other-Spices-Trees', 'Other-Seasoning-Trees', 'Other-Crops-Cultivated', 'Condition',
// //         'Nutmeg-Land', 'Nutmeg-Frequency', 'Potential-Risks', 'Road-Access', 'Food-Safety-and-Quality',
// //         'Farm-Water-Source', 'Farm-House', 'inspector-symmary', 'Policy'
// //     ];

// //     var openRequest = indexedDB.open('GCNA', 2);

// //     openRequest.onsuccess = function (e) {
// //         var db = e.target.result;

// //         additionalEndpoints.forEach(function (endpoint) {
// //             var transaction = db.transaction([endpoint]);
// //             var objectStore = transaction.objectStore(endpoint);
// //             var getRequest = objectStore.getAll();

// //             getRequest.onsuccess = function (event) {
// //                 var results = event.target.result;
// //                 results.forEach(function (result) {
// //                     var key = result.id;
// //                     fetch(`/api/${endpoint}2/${key}/`, {
// //                         method: 'GET',
// //                         headers: {
// //                             'Content-Type': 'application/json',
// //                             'X-CSRFToken': getCookie('csrftoken'),
// //                         },
// //                     })
// //                     .then((response) => {
// //                         if (response.ok) {
// //                             return response.json();
// //                         } else {
// //                             throw new Error('Network response was not ok');
// //                         }
// //                     })
// //                     .then((data) => {
// //                         if (response.status === 200) {
// //                             return response.json().then((data) => {
// //                                 // Object exists and IDs match, make a PATCH request to update it
// //                                 return fetch(`/api/${endpoint}2/${key}/`, {
// //                                     method: 'PATCH',
// //                                     headers: {
// //                                         'Content-Type': 'application/json',
// //                                         'X-CSRFToken': getCookie('csrftoken'),
// //                                     },
// //                                     body: JSON.stringify(result),
// //                                 });
// //                             });
// //                         } else {
// //                             // Object does not exist in Django, make a POST request to create it
// //                             return fetch(`/api/${endpoint}/`, {
// //                                 method: 'POST',
// //                                 headers: {
// //                                     'Content-Type': 'application/json',
// //                                     'X-CSRFToken': getCookie('csrftoken'),
// //                                 },
// //                                 body: JSON.stringify(result),
// //                             });
// //                         }
// //                     })
// //                     .then((response) => response.json())
// //                     .then((data) => {
// //                         displayMessage(`Success for ${endpoint}: ${data.message}`);
// //                     })
// //                     .catch((error) => {
// //                         displayMessage(`Error for ${endpoint}: ${error.message}`, true);
// //                     });
// //                 });
// //             };
// //         });
// //     };

// //     function displayMessage(message, isError = false) {
// //         var messageElement = document.createElement('div');
// //         messageElement.textContent = message;
// //         messageElement.style.position = 'fixed';
// //         messageElement.style.bottom = '10px';
// //         messageElement.style.right = '10px';
// //         messageElement.style.padding = '10px';
// //         messageElement.style.backgroundColor = isError ? 'red' : 'green';
// //         messageElement.style.color = 'white';

// //         document.body.appendChild(messageElement);

// //         // Remove the message after a certain time (e.g., 5 seconds)
// //         setTimeout(function () {
// //             document.body.removeChild(messageElement);
// //         }, 5000);
// //     }

// //     function getCookie(name) {
// //         let cookieValue = null;
// //         if (document.cookie && document.cookie !== '') {
// //             let cookies = document.cookie.split(';');
// //             for (let i = 0; i < cookies.length; i++) {
// //                 let cookie = cookies[i].trim();
// //                 if (cookie.substring(0, name.length + 1) === (name + '=')) {
// //                     cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
// //                     break;
// //                 }
// //             }
// //         }
// //         return cookieValue;
// //     }
// // }









// // // setInterval(activateCode, 1 * 60 * 1000);


// // // function activateCode() {
// // //     var additionalEndpoints = [
// // //         'DriedA', 'DriedB', 'FloatA', 'FloatB', 'Quaility', 'Worker', 'Farmer', 'visit', 'In-House-Drying',
// // //         'Dispatch-Of-Dried-Nutmeg', 'Dispatch-Of-Green', 'Cracking-Summary', 'Floation-Summary',
// // //         'Package-Ciontrol', 'Editors', 'Labour-support', 'Training-support', 'land-info', 'Land-Tenur',
// // //         'Nutmeg-Trees', 'Nutmeg-Variety', 'Other-Crops', 'Coconut-Trees', 'Citrus-Mango-Trees',
// // //         'Other-Spices-Trees', 'Other-Seasoning-Trees', 'Other-Crops-Cultivated', 'Condition',
// // //         'Nutmeg-Land', 'Nutmeg-Frequency', 'Potential-Risks', 'Road-Access', 'Food-Safety-and-Quality',
// // //         'Farm-Water-Source', 'Farm-House', 'inspector-symmary', 'Policy'
// // //     ];
// // //     var openRequest = indexedDB.open('GCNA', 2);
// // //     var openRequest2 = indexedDB.open('DELETED');

// // //     openRequest.onsuccess = function (e) {
// // //         var db = e.target.result;

// // //         additionalEndpoints.forEach(function (endpoint) {
// // //             var transaction = db.transaction([endpoint]);
// // //             var objectStore = transaction.objectStore(endpoint);
// // //             var getRequest = objectStore.getAll();

// // //             getRequest.onsuccess = function (event) {
// // //                 var results = event.target.result;
// // //                 results.forEach(function (result) {
// // //                     fetch(`/api/${endpoint}2/${result.id}/`, {
// // //                         method: 'GET',
// // //                         headers: {
// // //                             'Content-Type': 'application/json',
// // //                             'X-CSRFToken': getCookie('csrftoken'),
// // //                         },
// // //                     })
// // //                     .then((response) => {
// // //                         if (response.status === 200) {
// // //                             return response.json().then((data) => {
// // //                                 // Convert field types if necessary
// // //                                 convertFieldTypes(result, data);
                                
// // //                                 // Object exists and IDs match, make a PATCH request to update it
// // //                                 return fetch(`/api/${endpoint}2/${result.id}/`, {
// // //                                     method: 'PATCH',
// // //                                     headers: {
// // //                                         'Content-Type': 'application/json',
// // //                                         'X-CSRFToken': getCookie('csrftoken'),
// // //                                     },
// // //                                     body: JSON.stringify(result),
// // //                                 });
// // //                             });
// // //                         } else {
// // //                             // Object does not exist in Django, make a POST request to create it
// // //                             return fetch(`/api/${endpoint}/`, {
// // //                                 method: 'POST',
// // //                                 headers: {
// // //                                     'Content-Type': 'application/json',
// // //                                     'X-CSRFToken': getCookie('csrftoken'),
// // //                                 },
// // //                                 body: JSON.stringify(result),
// // //                             });
// // //                         }
// // //                     })
// // //                     .then((response) => response.json())
// // //                     .then((data) => {
// // //                         displayMessage(`Success for ${endpoint}: ${data.message}`);
// // //                     })
// // //                     .catch((error) => {
// // //                         displayMessage(`Error for ${endpoint}: ${error.message}`, true);
// // //                     });
// // //                 });
// // //             };
// // //         });
// // //     };

// // //     openRequest2.onsuccess = function (e) {
// // //         var db = e.target.result;

// // //         additionalEndpoints.forEach(function (endpoint) {
// // //             var transaction2 = db.transaction([endpoint]);
// // //             var objectStore2 = transaction2.objectStore(endpoint);
// // //             var getRequest2 = objectStore2.getAll();

// // //             getRequest2.onsuccess = function (event) {
// // //                 var results = event.target.result;
// // //                 results.forEach(function (result) {
// // //                     fetch(`/api/${endpoint}2/${result.id}/`, {
// // //                         method: 'GET',
// // //                         headers: {
// // //                             'Content-Type': 'application/json',
// // //                             'X-CSRFToken': getCookie('csrftoken'),
// // //                         },
// // //                     })
// // //                     .then((response) => {
// // //                         if (response.status === 200) {
// // //                             return response.json().then((data) => {
// // //                                 // Object exists and IDs match, make a PATCH request to update it
// // //                                 return fetch(`/api/${endpoint}2/${result.id}/`, {
// // //                                     method: 'DELETE',
// // //                                     headers: {
// // //                                         'Content-Type': 'application/json',
// // //                                         'X-CSRFToken': getCookie('csrftoken'),
// // //                                     },
// // //                                     body: JSON.stringify(result),
// // //                                 });
// // //                             });
// // //                         }
// // //                     })
// // //                     .then(() => {
// // //                         displayMessage(`Success for Deletion ${endpoint}`);
// // //                     })
// // //                     .catch((error) => {
// // //                         displayMessage(`Error for Deletion ${endpoint}: ${error.message}`, true);
// // //                     });
// // //                 });
// // //             };
// // //         });
// // //     };

// // //     function displayMessage(message, isError = false) {
// // //         var messageElement = document.createElement('div');
// // //         messageElement.textContent = message;
// // //         messageElement.style.position = 'fixed';
// // //         messageElement.style.bottom = '10px';
// // //         messageElement.style.right = '10px';
// // //         messageElement.style.padding = '10px';
// // //         messageElement.style.backgroundColor = isError ? 'red' : 'green';
// // //         messageElement.style.color = 'white';

// // //         document.body.appendChild(messageElement);

// // //         // Remove the message after a certain time (e.g., 5 seconds)
// // //         setTimeout(function () {
// // //             document.body.removeChild(messageElement);
// // //         }, 5000);
// // //     }

// // //     function getCookie(name) {
// // //         let cookieValue = null;
// // //         if (document.cookie && document.cookie !== '') {
// // //             let cookies = document.cookie.split(';');
// // //             for (let i = 0; i < cookies.length; i++) {
// // //                 let cookie = cookies[i].trim();
// // //                 if (cookie.substring(0, name.length + 1) === (name + '=')) {
// // //                     cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
// // //                     break;
// // //                 }
// // //             }
// // //         }
// // //         return cookieValue;
// // //     }
    
// // //     function convertFieldTypes(indexedDBEntry, djangoEntry) {
// // //         for (let prop in indexedDBEntry) {
// // //             if (indexedDBEntry.hasOwnProperty(prop)) {
// // //                 // Check if the property exists in the Django entry
// // //                 if (djangoEntry.hasOwnProperty(prop)) {
// // //                     // Check if the types are different and perform conversion if necessary
// // //                     if (typeof indexedDBEntry[prop] === 'string' && Number.isInteger(djangoEntry[prop])) {
// // //                         indexedDBEntry[prop] = parseInt(indexedDBEntry[prop]);
// // //                     }
// // //                     // Add more type conversions for other types as needed
// // //                 }
// // //             }
// // //         }
// // //     }
    
// // // }


// // // setInterval(activateCode, 1 * 60 * 1000);


// // // function activateCode() {
// // //     var additionalEndpoints = [
// // //         'DriedA', 'DriedB', 'FloatA', 'FloatB', 'Quaility', 'Worker', 'Farmer', 'visit', 'In-House-Drying',
// // //         'Dispatch-Of-Dried-Nutmeg', 'Dispatch-Of-Green', 'Cracking-Summary', 'Floation-Summary',
// // //         'Package-Ciontrol', 'Editors', 'Labour-support', 'Training-support', 'land-info', 'Land-Tenur',
// // //         'Nutmeg-Trees', 'Nutmeg-Variety', 'Other-Crops', 'Coconut-Trees', 'Citrus-Mango-Trees',
// // //         'Other-Spices-Trees', 'Other-Seasoning-Trees', 'Other-Crops-Cultivated', 'Condition',
// // //         'Nutmeg-Land', 'Nutmeg-Frequency', 'Potential-Risks', 'Road-Access', 'Food-Safety-and-Quality',
// // //         'Farm-Water-Source', 'Farm-House', 'inspector-symmary', 'Policy'
// // //     ];
// // //     var openRequest = indexedDB.open('GCNA', 2);
// // //     var openRequest2 = indexedDB.open('DELETED');

// // //     openRequest.onsuccess = function (e) {
// // //         var db = e.target.result;

// // //         additionalEndpoints.forEach(function (endpoint) {
// // //             var transaction = db.transaction([endpoint]);
// // //             var objectStore = transaction.objectStore(endpoint);
// // //             var getRequest = objectStore.getAll();

// // //             getRequest.onsuccess = function (event) {
// // //                 var results = event.target.result;
// // //                 results.forEach(function (result) {
// // //                     fetch(`/api/${endpoint}2/${result.id}/`, {
// // //                         method: 'GET',
// // //                         headers: {
// // //                             'Content-Type': 'application/json',
// // //                             'X-CSRFToken': getCookie('csrftoken'),
// // //                         },
// // //                     })
// // //                     .then((response) => {
// // //                         if (response.status === 200) {
// // //                             return response.json().then((data) => {
// // //                                 // Convert field types if necessary
// // //                                 convertFieldTypes(result, data);
                                
// // //                                 // Object exists and IDs match, make a PATCH request to update it
// // //                                 return fetch(`/api/${endpoint}2/${result.id}/`, {
// // //                                     method: 'PATCH',
// // //                                     headers: {
// // //                                         'Content-Type': 'application/json',
// // //                                         'X-CSRFToken': getCookie('csrftoken'),
// // //                                     },
// // //                                     body: JSON.stringify(result),
// // //                                 });
// // //                             });
// // //                         } else {
// // //                             // Object does not exist in Django, make a POST request to create it
// // //                             return fetch(`/api/${endpoint}/`, {
// // //                                 method: 'POST',
// // //                                 headers: {
// // //                                     'Content-Type': 'application/json',
// // //                                     'X-CSRFToken': getCookie('csrftoken'),
// // //                                 },
// // //                                 body: JSON.stringify(result),
// // //                             });
// // //                         }
// // //                     })
// // //                     .then((response) => response.json())
// // //                     .then((data) => {
// // //                         displayMessage(`Success for ${endpoint}: ${data.message}`);
// // //                     })
// // //                     .catch((error) => {
// // //                         displayMessage(`Error for ${endpoint}: ${error.message}`, true);
// // //                     });
// // //                 });
// // //             };
// // //         });
// // //     };

// // //     openRequest2.onsuccess = function (e) {
// // //         var db = e.target.result;

// // //         additionalEndpoints.forEach(function (endpoint) {
// // //             var transaction2 = db.transaction([endpoint]);
// // //             var objectStore2 = transaction2.objectStore(endpoint);
// // //             var getRequest2 = objectStore2.getAll();

// // //             getRequest2.onsuccess = function (event) {
// // //                 var results = event.target.result;
// // //                 results.forEach(function (result) {
// // //                     fetch(`/api/${endpoint}2/${result.id}/`, {
// // //                         method: 'GET',
// // //                         headers: {
// // //                             'Content-Type': 'application/json',
// // //                             'X-CSRFToken': getCookie('csrftoken'),
// // //                         },
// // //                     })
// // //                     .then((response) => {
// // //                         if (response.status === 200) {
// // //                             return response.json().then((data) => {
// // //                                 // Object exists and IDs match, make a PATCH request to update it
// // //                                 return fetch(`/api/${endpoint}2/${result.id}/`, {
// // //                                     method: 'DELETE',
// // //                                     headers: {
// // //                                         'Content-Type': 'application/json',
// // //                                         'X-CSRFToken': getCookie('csrftoken'),
// // //                                     },
// // //                                     body: JSON.stringify(result),
// // //                                 });
// // //                             });
// // //                         }
// // //                     })
// // //                     .then(() => {
// // //                         displayMessage(`Success for Deletion ${endpoint}`);
// // //                     })
// // //                     .catch((error) => {
// // //                         displayMessage(`Error for Deletion ${endpoint}: ${error.message}`, true);
// // //                     });
// // //                 });
// // //             };
// // //         });
// // //     };

// // //     function displayMessage(message, isError = false) {
// // //         var messageElement = document.createElement('div');
// // //         messageElement.textContent = message;
// // //         messageElement.style.position = 'fixed';
// // //         messageElement.style.bottom = '10px';
// // //         messageElement.style.right = '10px';
// // //         messageElement.style.padding = '10px';
// // //         messageElement.style.backgroundColor = isError ? 'red' : 'green';
// // //         messageElement.style.color = 'white';

// // //         document.body.appendChild(messageElement);

// // //         // Remove the message after a certain time (e.g., 5 seconds)
// // //         setTimeout(function () {
// // //             document.body.removeChild(messageElement);
// // //         }, 5000);
// // //     }

// // //     function getCookie(name) {
// // //         let cookieValue = null;
// // //         if (document.cookie && document.cookie !== '') {
// // //             let cookies = document.cookie.split(';');
// // //             for (let i = 0; i < cookies.length; i++) {
// // //                 let cookie = cookies[i].trim();
// // //                 if (cookie.substring(0, name.length + 1) === (name + '=')) {
// // //                     cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
// // //                     break;
// // //                 }
// // //             }
// // //         }
// // //         return cookieValue;
// // //     }
    
// // //     function convertFieldTypes(indexedDBEntry, djangoEntry) {
// // //         for (let prop in indexedDBEntry) {
// // //             if (indexedDBEntry.hasOwnProperty(prop)) {
// // //                 // Check if the property exists in the Django entry
// // //                 if (djangoEntry.hasOwnProperty(prop)) {
// // //                     // Check if the types are different and perform conversion if necessary
// // //                     if (typeof indexedDBEntry[prop] === 'string' && Number.isInteger(djangoEntry[prop])) {
// // //                         indexedDBEntry[prop] = parseInt(indexedDBEntry[prop]);
// // //                     }
// // //                     // Add more type conversions for other types as needed
// // //                 }
// // //             }
// // //         }
// // //     }
    
// // // }


// // Function to transfer IndexedDB data to Django server
// function transferIndexedDBData() {
//     // Check if the browser is online
//     if (navigator.onLine) {
//         var request = indexedDB.open('GCNA', 2);

//         request.onsuccess = function(event) {
//             var db = event.target.result;
//             var modelNames = ['Worker', 'Farmer', 'DriedA', 'DriedB', 'FloatA', 'FloatB', 'Quaility', 'visit', 'In-House-Drying', 'Dispatch-Of-Dried-Nutmeg', 'Dispatch-Of-Green', 'Cracking-Summary', 'Floation-Summary', 'Package-Ciontrol', 'Editors', 'Labour-support', 'Training-support', 'land-info', 'Land-Tenur', 'Nutmeg-Trees', 'Nutmeg-Variety', 'Other-Crops', 'Coconut-Trees', 'Citrus-Mango-Trees', 'Other-Spices-Trees', 'Other-Seasoning-Trees', 'Other-Crops-Cultivated', 'Condition', 'Nutmeg-Land', 'Nutmeg-Frequency', 'Potential-Risks', 'Road-Access', 'Food-Safety-and-Quality', 'Farm-Water-Source', 'Farm-House', 'inspector-symmary', 'Policy','Sanitation-A','Sanitation-B','Sanitation-C','Cracking_Schedule','Assorting_Log', 'Extractor_Log', 'Fumigation_Log','Shelves'];

//             modelNames.forEach(function(modelName) {
//                 var transaction = db.transaction(modelName, 'readonly');
//                 var objectStore = transaction.objectStore(modelName);
//                 var getRequest = objectStore.getAll();

//                 getRequest.onsuccess = function(event) {
//                     var data = event.target.result;
//                     data.forEach(function(item) {
//                         sendDataToDjango(item, modelName);
//                     });
//                 };
//             });
//         };

//         request.onerror = function(event) {
//             console.error('Error opening IndexedDB', event);
//         };
//     }

//     // Call the function again after 10 seconds
//     setTimeout(transferIndexedDBData, 60 * 1000);
// }

// // Trigger the function initially
// transferIndexedDBData();

// // Function to send data to Django server
// function sendDataToDjango(item, modelName) {
//     var xhr = new XMLHttpRequest();
//     xhr.open('POST', '/check-and-add/', true);
//     xhr.setRequestHeader('Content-Type', 'application/json');
//     xhr.onreadystatechange = function() {
//         if (xhr.readyState === XMLHttpRequest.DONE) {
//             if (xhr.status === 200) {
//                 console.log('Entry added successfully for model:', modelName);
//             } else {
//                 console.error('Error adding entry for model:', modelName, xhr.statusText);
//             }
//         }
//     };
//     xhr.send(JSON.stringify({model: modelName, data: item}));
// }
//true_sync.js

// // Check if the browser is online
// if (navigator.onLine) {
//     // If online, trigger the function
//     transferIndexedDBData();
// }

// // Listen for online event
// window.addEventListener('online', function() {
//     // When online, trigger the function
//     transferIndexedDBData();
// });]


setInterval(transferIndexedDBData, 1 * 60 * 1000);
function transferIndexedDBData() {
    var request = indexedDB.open('GCNA', 2);

    request.onsuccess = function(event) {
        var db = event.target.result;
        var  modelNames = ['Worker', 'Farmer', 'DriedA', 'DriedB', 'FloatA', 'FloatB', 'Quaility', 'visit', 'In-House-Drying', 'Dispatch-Of-Dried-Nutmeg', 'Dispatch-Of-Green', 'Cracking-Summary', 'Floation-Summary', 'Package-Ciontrol', 'Editors', 'Labour-support', 'Training-support', 'land-info', 'Land-Tenur', 'Nutmeg-Trees', 'Nutmeg-Variety', 'Other-Crops', 'Coconut-Trees', 'Citrus-Mango-Trees', 'Other-Spices-Trees', 'Other-Seasoning-Trees', 'Other-Crops-Cultivated', 'Condition', 'Nutmeg-Land', 'Nutmeg-Frequency', 'Potential-Risks', 'Road-Access', 'Food-Safety-and-Quality', 'Farm-Water-Source', 'Farm-House', 'inspector-symmary', 'Policy','Sanitation-A','Sanitation-B','Sanitation-C','Cracking_Schedule','Assorting_Log',
        'Extractor_Log',
        'Fumigation_Log','Shelves'];
        

        modelNames.forEach(function(modelName) {
            var transaction = db.transaction(modelName, 'readonly');
            var objectStore = transaction.objectStore(modelName);
            var getRequest = objectStore.getAll();

            getRequest.onsuccess = function(event) {
                var data = event.target.result;
                data.forEach(function(item) {
                    sendDataToDjango(item, modelName);
                });
            };
        });
    };

    request.onerror = function(event) {
        console.error('Error opening IndexedDB', event);
    };

    // Call the function again after 20 seconds
    setTimeout(transferIndexedDBData, 60 * 1000);
}

function sendDataToDjango(item, modelName) {
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/check-and-add/', true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function() {
        if (xhr.readyState === XMLHttpRequest.DONE) {
            if (xhr.status === 200) {
                console.log('Entry added successfully for model:', modelName);
            } else {
                console.error('Error adding entry for model:', modelName, xhr.statusText);
            }
        }
    };
    xhr.send(JSON.stringify({model: modelName, data: item}));
}