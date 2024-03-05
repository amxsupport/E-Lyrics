// Adds event listener for navigation back to homepage
document.addEventListener('DOMContentLoaded', function (event) {
  document.getElementById('home-page').addEventListener('click', function () {
    window.location.href = 'http://0.0.0.0:5000';
  });
  setupSuggestionPost();
