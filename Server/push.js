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