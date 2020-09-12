self.addEventListener('install', function (event) {
    console.log('[Service Worker] Installing Service Worker ...', event);
});

self.addEventListener('activate', event => {
    console.log('[Service Worker] Activating Service Worker ...', event);
});

self.addEventListener('fetch', function(event) {
    console.log('[Service Worker] Fetching Service Worker ...', event);
});

if (window.Notification) {
    function showNotification() {
        let NotificationOpts = {
            body: 'Some notification information',
            icon: '/images/heartbeat-icon-home-144.png'
        }
        new Notification("My new notification");
    }
}

if (Notification.permission === 'granted') {
    showNotification();
} else if (Notification.permission !== 'denied') {
    Notification.requestPermission((permission) => {
        if (permission === 'granted') {
            showNotification();
        }
    });
}

self.addEventListener('push', event => {
    let n = self.registration.showNotification('A notification from service worker...');
    event.waitUntil(n);
})