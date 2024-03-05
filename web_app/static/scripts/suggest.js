// Adds event listener for navigation back to homepage
document.addEventListener('DOMContentLoaded', function (event) {
  document.getElementById('home-page').addEventListener('click', function () {
    window.location.href = 'http://0.0.0.0:5000';
  });
  setupSuggestionPost();
  /**
 * Adds event listener for setting up form for submitting a suggestion
 *
 * @returns {undefined}
 */
  function setupSuggestionPost () {
    form = document.getElementById('suggestion-form');
    form.addEventListener('submit', postSuggestion);
  }
