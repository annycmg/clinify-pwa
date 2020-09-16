if ( window.Notification ) {
    function showNotification(){
        let notificationOpts = {
            body: 'Lembre-se de manter seu perfil sempre atualizado :)',
            icon: '/static/images/heartbeat-icon-home-144.png'
        }
        new Notification('Sua saúde em dia!', notificationOpts);
    }
    if ( Notification.permission === 'granted' ) {
        showNotification();
    } else if (Notification.permission !== 'denied') {
        Notification.requestPermission((permission) => {
            if (permission === 'granted') {
                showNotification();
            }
        });
    }
}


