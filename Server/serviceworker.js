self.addEventListener('install', function (event) {
    console.log('[Service Worker] Installing Service Worker ...', event);
});

self.addEventListener('activate', event => {
    console.log('[Service Worker] Activating Service Worker ...', event);
});

self.addEventListener('fetch', function(event) {
    console.log('[Service Worker] Fetching Service Worker ...', event);
});