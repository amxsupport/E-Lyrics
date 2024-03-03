// Fetches all songs from internal REST API and sets up the homepage for navigation to other pages
document.addEventListener('DOMContentLoaded', function (event) {
  fetch('http://0.0.0.0:5001/api/v1/songs')
    .then(response => response.json())
    .then(data => {
      data = data.sort();
      for (let i = 0; i < data.length; i++) {
        document.getElementById('songs').insertAdjacentHTML('beforeend', songHTML(data[i]));
        console.log(setupNav(data[i]));
      }
    })
    .catch(error => console.error(error));

  document.getElementById('suggest').addEventListener('click', function () {
    window.location.href = 'http://0.0.0.0:5000/suggest/';
  });
