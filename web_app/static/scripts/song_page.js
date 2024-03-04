document.addEventListener('DOMContentLoaded', function (event) {
  const index = window.location.href.lastIndexOf('/');
  const id = window.location.href.substring(index + 1);
  const songApiUrl = 'http://0.0.0.0:5001/api/v1/songs/' + id;
  songDetails(songApiUrl);
  songWords(id);
  console.log("first");

// Fetches all data for specific song and sets up navigation to other songs with same genre
  async function songDetails(songApiUrl) {
    try {
      let songApiResponse = await fetch(songApiUrl)
      let songData = await songApiResponse.json()
      document.getElementById('song-title').innerHTML = `${songData.title}`;
      document.getElementById('song-artist').innerHTML = `${songData.artist}`;
      document.getElementById('song-lyrics').innerHTML = `${songData.lyrics}`;
      document.getElementById('song-genre').innerHTML = `Genre: ${songData.genre}`;
      document.getElementById('song-genre').setAttribute('text', songData.genre);
      document.getElementById('song-image').setAttribute('src', songData.image_url);
      genre = document.getElementById('song-genre').getAttribute('text');
      const genreApiUrl = 'http://0.0.0.0:5001/api/v1/songs/genre/' + genre;
      console.log("second");
      let genreApiResponse = await fetch(genreApiUrl)
      genreData = await genreApiResponse.json()
      if (genreData.length > 1) {
        document.getElementById('genre-suggestions').insertAdjacentHTML('beforeEnd', `<p>Other ${genreData[0].genre} songs to explore:</p><ul id="suggestion-list"></ul><a class="card-link" href="#"></a>`);
        suggestionDict = suggestions(genreData);
        for (const [key, value] of Object.entries(suggestionDict)) {
          item = document.createElement('LI');
          text = document.createTextNode(value);
          item.appendChild(text);
          item.setAttribute('id', key);
          document.getElementById('suggestion-list').appendChild(item);
          suggestionNav(key);
        }
      } else {
        document.getElementById('genre-suggestions').insertAdjacentHTML('beforeEnd', `<p>Check back for more ${genreData[0].genre} songs!</p><a class="card-link" href="#"></a>`);
      }} catch(err){
	console.error(err);
    }}

 // Fetches associated words and modifies lyrics HTML for highlighting of selected words
  async function songWords(id) {
    try {
      const songWordsApiUrl = 'http://0.0.0.0:5001/api/v1/songs/' + id + '/words';
      let songWordsResponse = await fetch(songWordsApiUrl);
      let songWordsData = await songWordsResponse.json();
      console.log("third");
      for (i = 0; i < songWordsData.length; i++) {
	item = document.createElement('LI');
	text = document.createTextNode(songWordsData[i].text);
	item.appendChild(text);
	document.getElementById('wordlist').appendChild(item);
	setupWordFetch(item);
      }
      featuredWords = document.getElementById('wordlist').querySelectorAll('li');
      modFeaturedWords = [];
      for (i = 0; i < featuredWords.length; i++) { modFeaturedWords.push(featuredWords[i].innerText); }
      lyrics = document.getElementById('song-lyrics').innerHTML;
      console.log(lyrics);
      modLyrics = lyrics.replace(/\n/g, '+\n');
      console.log('Modified: ' + modLyrics);
      words = modLyrics.split(/\+| /);
      console.log(words);
      for (i = 0; i < words.length; i++) {
        console.log(words[i]);
        if (modFeaturedWords.includes(words[i].replace(/[\".,\/#!$%\^&\*;:{}=\-_`~()\n]/g, ''))) {
          console.log('Found: ' + words[i]);
          words[i] = `<span class = ${words[i].replace(/[\".,\/#!$%\^&\*;:{}=\-_`~()]/g, '')}>` + words[i] + '</span>';
        }
      }
      document.getElementById('song-lyrics').innerHTML = words.join(' ');
    } catch(err) {
      console.error(err);
    }
  }

