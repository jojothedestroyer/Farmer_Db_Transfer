

// setInterval(transferIndexedDBData, 1 * 60 * 1000);
// function transferIndexedDBData() {
//     var request = indexedDB.open('GCNA', 2);

//     request.onsuccess = function(event) {
//         var db = event.target.result;
//         var  modelNames = ['Worker', 'Farmer', 'DriedA', 'DriedB', 'FloatA', 'FloatB', 'Quaility', 'visit', 'In-House-Drying', 'Dispatch-Of-Dried-Nutmeg', 'Dispatch-Of-Green', 'Cracking-Summary', 'Floation-Summary', 'Package-Ciontrol', 'Editors', 'Labour-support', 'Training-support', 'land-info', 'Land-Tenur', 'Nutmeg-Trees', 'Nutmeg-Variety', 'Other-Crops', 'Coconut-Trees', 'Citrus-Mango-Trees', 'Other-Spices-Trees', 'Other-Seasoning-Trees', 'Other-Crops-Cultivated', 'Condition', 'Nutmeg-Land', 'Nutmeg-Frequency', 'Potential-Risks', 'Road-Access', 'Food-Safety-and-Quality', 'Farm-Water-Source', 'Farm-House', 'inspector-symmary', 'Policy','Sanitation-A','Sanitation-B','Sanitation-C','Cracking_Schedule','Assorting_Log',
//         'Extractor_Log',
//         'Fumigation_Log','Shelves','W_Shelves','M_Shelves','W_Shelves_Dried','M_Shelves_Dried','Vehicle_Inspection','Final_Weight_Inspection','Final_Weight_Inspection_fields'];
        

//         modelNames.forEach(function(modelName) {
//             var transaction = db.transaction(modelName, 'readonly');
//             var objectStore = transaction.objectStore(modelName);
//             var getRequest = objectStore.getAll();

//             getRequest.onsuccess = function(event) {
//                 var data = event.target.result;
//                 data.forEach(function(item) {
//                     sendDataToDjango(item, modelName);
//                 });
//             };
//         });
//     };

//     request.onerror = function(event) {
//         console.error('Error opening IndexedDB', event);
//     };

//     // Call the function again after 20 seconds
//     setTimeout(transferIndexedDBData, 60 * 1000);
// }

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



















setInterval(better_transferIndexedDBData, 30 * 1000); // Trigger every 10 seconds

function better_transferIndexedDBData() {
    var request = indexedDB.open('GCNA', 2);

    request.onsuccess = function(event) {
        var db = event.target.result;
        var modelNames = ['Worker', 'Farmer', 'DriedA', 'DriedB', 'FloatA', 'FloatB', 'Quaility', 'visit', 'In-House-Drying', 'Dispatch-Of-Dried-Nutmeg', 'Dispatch-Of-Green', 'Cracking-Summary', 'Floation-Summary', 'Package-Ciontrol', 'Editors', 'Labour-support', 'Training-support', 'land-info', 'Land-Tenur', 'Nutmeg-Trees', 'Nutmeg-Variety', 'Other-Crops', 'Coconut-Trees', 'Citrus-Mango-Trees', 'Other-Spices-Trees', 'Other-Seasoning-Trees', 'Other-Crops-Cultivated', 'Condition', 'Nutmeg-Land', 'Nutmeg-Frequency', 'Potential-Risks', 'Road-Access', 'Food-Safety-and-Quality', 'Farm-Water-Source', 'Farm-House', 'inspector-symmary', 'Policy','Sanitation-A','Sanitation-B','Sanitation-C','Cracking_Schedule','Assorting_Log',
        'Extractor_Log',
        'Fumigation_Log','Shelves','W_Shelves','M_Shelves','W_Shelves_Dried','M_Shelves_Dried','Vehicle_Inspection','Final_Weight_Inspection','Final_Weight_Inspection_fields','Dispatch_Of_Dried_Nutmeg_Rec','Dispatch_Of_Green_Nutmeg_Rec','Cracking_Extraction_Summary'];

        modelNames.forEach(function(modelName) {
            var transaction = db.transaction(modelName, 'readonly');
            var objectStore = transaction.objectStore(modelName);
            var getRequest = objectStore.getAll();

            getRequest.onsuccess = function(event) {
                var data = event.target.result;
                data.forEach(function(item) {
                    better_sendDataToDjango(item, modelName);
                });
            };
        });
    };

    request.onerror = function(event) {
        console.error('Error opening IndexedDB', event);
    };

    // Call the function again after 10 seconds
    setTimeout(better_transferIndexedDBData, 30 * 1000); // Trigger every 10 seconds
}

function better_sendDataToDjango(item, modelName) {
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/check-and-add/', true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function() {
        if (xhr.readyState === XMLHttpRequest.DONE) {
            if (xhr.status === 200) {
                console.log('Entry added successfully for model:', modelName,modelName.id);
            } else {
                console.error('Error adding entry for model:', modelName, xhr.statusText);
            }
        }
    };
    xhr.send(JSON.stringify({model: modelName, data: item}));
}
