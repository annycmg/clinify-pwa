var staticCacheName = 'staticCache-v1';
var dynamicCacheName = 'dynamicCache-v1';

var STATIC_FILES = ['/Templates/offline', '/static/js/manifest.json', '/static/css/screens.css', 
"https://fonts.googleapis.com/css?family=Josefin+Sans:600&display=swap",
"https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css",
"https://cdnjs.cloudflare.com/ajax/libs/material-design-lite/1.3.0/material.indigo-pink.min.css",
"https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js",
"https://code.jquery.com/jquery-3.1.1.min.js",
"https://code.jquery.com/jquery-3.2.1.slim.min.js",
'/static/images/bike.png',
'/static/images/breakfast.png',
'/static/images/calories.png',
'/static/images/diet.jpg',
'/static/images/dinner.png',
'/static/images/doctor.jpg',
'/static/images/edit.png',
'/static/images/exercise.jpg',
'/static/images/gym.png',
'/static/images/heartbeat-icon-home-144.png',
'/static/images/heartbeat-logo-144.png',
'/static/images/heartbeat-logo-256.png',
'/static/images/heartbeat-logo-512.png',
'/static/images/hiking.png',
'/static/images/lunch.png',
'/static/images/medication.jpg',
'/static/images/nut.png',
'/static/images/profile-background.jpg',
'/static/images/return.png',
'/static/images/run.png',
'/static/images/snack.png',
'/static/images/speed.png',
'/static/images/swim.png',
'/static/images/taco.png',
'/static/images/trash.png',
'/static/images/travel.jpg',
'/static/images/logout.png',
'/static/images/vaccine.jpg',
'/static/images/walk.png',
// '/static/images/logout.png',
]

self.addEventListener('install', function (event) {
    console.log('[Service Worker] Installing Service Worker ...', event);
    event.waitUntil(
      caches.open(staticCacheName).then(function (cache) {
          console.log('[Service Worker] Precaching App Shell');
          cache.addAll(STATIC_FILES);
        })
    )
});

self.addEventListener('activate', event => {
    console.log('[Service Worker] Activating Service Worker ...', event);
    event.waitUntil(
        caches.keys().then(cacheNames => {
            return Promise.all(
                cacheNames
                    .filter(cacheName => (cacheName.startsWith("staticCache-")))
                    .filter(cacheName => (cacheName !== staticCacheName))
                    .map(cacheName => caches.delete(cacheName))
            );
        })
    );
});

// self.addEventListener("fetch", event => {
//     event.respondWith(caches.match(event.request)
//         .then(response => {
//             return response || fetch(event.request);
//         })
//         .catch(() => {
//             return caches.match('/Templates/offline');
//         })
//     )
// });
