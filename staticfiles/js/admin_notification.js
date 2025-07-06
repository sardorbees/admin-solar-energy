let lastKnownId = null;

function checkNewApplications() {
  fetch('/admin/check-new-application/')
    .then(response => response.json())
    .then(data => {
      if (lastKnownId !== null && data.latest_id > lastKnownId) {
        // Новый ID найден — проигрываем звук
        const audio = new Audio('../sounds/iphone.mp3');
        audio.play();
      }
      lastKnownId = data.latest_id;
    })
    .catch(error => console.error('Ошибка при проверке заявок:', error));
}

setInterval(checkNewApplications, 5000); // каждые 5 секунд
