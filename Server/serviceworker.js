self.addEventListener('install', function (event) {
    console.log('[Service Worker] Installed ...', event);
});  

self.addEventListener('activate', function (event) {
    console.log('[Service Worker] Activated ...', event);
});