if ('serviceWorker' in navigator && 'SyncManager' in window) {
  navigator.serviceWorker.ready.then(function (registration) {
    // Register a sync event
    registration.sync.register('syncData')
      .then(function () {
        console.log('Sync event registered.');
      })
      .catch(function (error) {
        console.error('Sync registration failed:', error);
      });
  });
}

// Later, when you want to trigger the sync:
function triggerSync() {
  if ('serviceWorker' in navigator && 'SyncManager' in window) {
    navigator.serviceWorker.ready.then(function (registration) {
      registration.sync.register('syncData')
        .then(function () {
          console.log('Sync event triggered.');
        })
        .catch(function (error) {
          console.error('Sync trigger failed:', error);
        });
    });
  }
}

// Inside your service worker (sw.js), handle the sync event
self.addEventListener('sync', function (event) {
  if (event.tag === 'syncData') {
    event.waitUntil(syncData());
  }
});

function syncData() {
  // Retrieve data from IndexedDB and send it to the server
  // Implement your synchronization logic here
}



