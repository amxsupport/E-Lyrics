# <p align="center"> ![Logo](https://i.imgur.com/yx62kSK.png) </p>

##	English Lyric Learning Hub
"English Lyric Learning Hub" aims to address the challenge of language acquisition, particularly in the context of English language learning through song lyrics. The project seeks to provide users with a comprehensive platform where they can explore and engage with English song lyrics to improve their language skills. By offering features such as linguistic breakdowns of words, interpretations, and interactive learning tools, the app endeavors to make the process of learning English through music more accessible and enjoyable.
While "English Lyric Learning Hub" offers valuable resources and tools for English language learners, it does not aim to replace traditional language learning methods or provide comprehensive language instruction. The project will not address broader issues in language education, such as curriculum development or teacher training.
The Portfolio Project is designed to assist individuals who are learning English as a second language or seeking to improve their English language proficiency. The target audience includes language learners of all levels, from beginners to advanced students, as well as educators and enthusiasts interested in using music as a language learning tool.

## Table of content

- [Inspiration](#inspiration)
- [Built With](#built-with)
- [Getting Started](#getting-started)
- [Features](#features)
    - [Song Selection](#song-selection)
    - [Words To Explore](#words-to-Explore)
    - [Linguistic Breakdown and Highlighting Of Selected Words](#linguistic-breakdown-and-highlighting-of-selected-words)
    - [Submit interpretations and view past submissions](#submit-interpretations-and-view-past-submissions)
    - [Suggest a Song Form](#suggest-a-song)
- [API](#API)
- [Future](#future)
- [Attributions](#attributions)
- [Author](#author)

## Inspiration

Our project was inspired by a shared passion for language learning and music appreciation.
We realized that many people learn English not just from textbooks but also from popular culture, especially through song lyrics.
We wanted to create a platform that harnesses the power of music to facilitate language learning in a fun and engaging way.

Initially, Lyrics for Learning was going to solely allow students to check out linguistic breakdowns for words within songs. However, after reflecting upon how I leveraged music in my own classroom and getting feedback from other teachers, I decided to also allow users to share their own interpretations of what words mean within songs. By exploring both the literal and figurative meaning of words in songs they know, students can deepen their understanding of the English language in a context that is familiar to them.

## Built With

### Technologies 🤖 : 

- [SOLAlchemy]
- [MySQL]
- [python]
- [Flask]
- [Bootstrap]
- [JavaScript]
- [gunicorn]
- [NGINX]
- [DigitalOcean]

### Architecture

# ![Architecture](https://i.imgur.com/DQel3Jn.png)

## Getting Started

To start using this web application, visit [amxsupport.tech](https://www.amxsupport.tech/E-lyrics_static/templates/homepage.html). To install it, simply clone this repository. You can start the app by running `web_app.app` and `api.v1.app` as Python modules in separate terminal windows. Please note, in order to run this app, you will need to install necessary dependencies as well as pass in the correct MySQLdb and Words API credentials respectively.

## Features

### **Song selection**

E-Lyrics offers a curated collection of "clean" and vocabulary-rich songs spanning diverse genres. Leveraging our internal RESTful API, we dynamically fetch data for each song, populating every Bootstrap card with relevant details. The song's unique identifier serves as the anchor for the "View" button embedded within the card, ensuring precise retrieval of song details upon user interaction. As the id seamlessly integrates into the song's URL, users can effortlessly access the desired content with a single click.

# ![song-selection](https://i.imgur.com/nwvSG0d.png)

### **Words To Explore**

Upon selecting a song, users are seamlessly redirected to a dedicated page tailored to that specific song. Here, comprehensive song details are dynamically retrieved from our internal RESTful API. Additionally, users are presented with a curated list of words extracted from the song lyrics, facilitating exploration and learning. To enhance the experience, event listeners are strategically placed on each word, enabling real-time linguistic analysis fetched from an external API. This feature also enables the highlighting of selected words within the lyrics, fostering deeper comprehension and engagement with the content.

# ![words-to-explore](https://i.imgur.com/zvuRlxo.png)

### **Linguistic Breakdown and Highlighting of Words**

Upon selecting a specific word within a song, our platform seamlessly fetches its linguistic breakdown from the external Words API. Subsequently, a dynamic menu is generated based on the available entries for the word, facilitating user exploration. When a user interacts with the menu by clicking on an entry, our JavaScript script identifies the corresponding sections for that entry, such as "Definition," "Synonyms," and "Examples." These sections, along with their respective content, populate a dynamic tabbed interface, providing users with a comprehensive browsing experience.

Moreover, the selected word is intelligently highlighted within the lyrics, enhancing readability and context. This functionality is achieved through meticulous parsing of the lyrics, where span elements are strategically added around words featured in the "Pick a word to explore!" list. These spans are meticulously assigned aligned classes, enabling precise targeting and seamless highlighting when a word is selected.

# ![linguistic-breakdown-and-highlighting-of-words](https://i.imgur.com/xE0iedR.png)

### **Submit Interpretations and View Past Interpretations**

Following an exploration of the linguistic nuances surrounding a word, users are invited to offer their interpretation of the artist's intent. Upon selecting "Submit," their insights are transmitted as a POST request to our internal RESTful API. Subsequently, the better-profanity module is invoked to scrutinize the submission for any profane content. In the event of profanity detection, the submission is withheld from database storage, accompanied by a user prompt cautioning against inappropriate language.

Conversely, if the interpretation passes the profanity check, it is securely stored within our database. Users can then access and peruse these submissions in the "Latest Interpretations" section, presented in an accordion-style layout for easy navigation and readability.

# ![submit-interpretations-and-view-past-interpretations](https://i.imgur.com/gyr6BQ4.png)

### **Suggest a Song Form**

To propose a new addition to our song collection for learning purposes, users can navigate to the "Suggest a Song" page and complete the provided form. This form prompts users to furnish essential details required for creating a new Song object, encompassing the artist's name, song title, and notable words for learning. Additionally, users are prompted to provide their email address and name, ensuring they receive credit for their contribution and are notified upon the song's inclusion in the collection.

# ![suggest-a-song-form](https://i.imgur.com/RGKGXVV.png)

## API

We developed an internal RESTful API to facilitate flexible data retrieval from the MySQL database for this web application. All available endpoints are located within the api.v1.views directory. Below is a concise overview of each endpoint:

/api/v1/interpretations/<word_id>/<song_id>

* GET: Fetches all Interpretation objects associated with a word from a specific song and returns a list containing them.

* POST: Creates a new interpretation for a word within a song.

/api/v1/interpretations/<interpretation_id>

* PUT: Updates an existing Interpretation object.

/api/v1/songs/<song_id>/words

* GET: Retrieves all words associated with a particular song and returns a list containing them.

/api/v1/songs

* GET: Retrieves all Song objects stored in the database and returns a list containing them.

/api/v1/songs/<text>
  
* GET: Retrieves a specific Song object from the database based on its title and returns a dictionary containing its details.

/api/v1/songs/genre/<genre>
  
* GET: Retrieves all Song objects from the database belonging to a specified genre.

/api/v1/suggestions/

* GET: Retrieves all Suggestion objects from the database and returns a list containing them.
    
* POST: Submits a new Suggestion object.

/api/v1/words/<text>
  
* GET: Retrieves the word_id associated with a specific word.

/api/v1/words_api/<text>

* GET: Fetches data for a word from an external API and returns the response to the client-side. By passing API credentials via the command line during API execution and utilizing the internal API for fetching, it ensures that credentials remain secure and are not exposed on the front-end.

## Future

After successfully launching our initial MVP within a span of 2 weeks, our vision for E-Lyrics extends far beyond its current capabilities. Our roadmap includes a plethora of exciting features aimed at enhancing user experience and engagement. Foremost among these is the implementation of a robust authentication system, empowering users to create personalized profiles. These profiles will serve as a hub for users to track their progress, revisit past interactions, and suggest new songs and words based on their preferences and usage history.

Furthermore, we envision enabling users to edit their past submissions and interact with each other by upvoting interpretations. Additionally, we are contemplating the addition of a "Top Users" leaderboard on the homepage to recognize and celebrate active contributors.

Your input and feedback are invaluable to us as we strive to shape the future of E-Lyrics. Whether you have feature ideas or wish to contribute to the project, we welcome your participation. Feel free to reach out to us with any suggestions or contributions you may have. Together, let's continue to elevate the E-Lyrics experience!

## Attributions

Shout-out to [Open Lyrics Database](https://github.com/Lyrics/lyrics) for the lyrics shown!

Licenses for images from Wikimedia Commons:

* [The xx at the Alcatraz.jpg](https://commons.wikimedia.org/wiki/File:The_xx_at_the_Alcatraz.jpg)
* [Adele Live 2016 tour.jpeg](https://commons.wikimedia.org/wiki/File:Adele_Live_2016_tour.jpeg)
* [Paul Simonon The Clash September 20 1979 Palladium NYC.jpg](https://commons.wikimedia.org/wiki/File:Paul_Simonon_The_Clash_September_20_1979_Palladium_NYC.jpg)

## Author

### **Abdelaaziz Amksa**

I'm passionate and dedicated software engineer with a proven track record of leveraging technology to drive innovation and solve complex problems. Currently excelling as a LIMS Administrator at a leading research center REMINEX SA, where I apply my technical expertise to optimize laboratory operations and facilitate scientific research.

[Github](https://github.com/amxsupport)
[LinkedIn](https://www.linkedin.com/in/abdelaaziz-amksa-28689753/)
[Twitter](https://twitter.com/abdoudev)

### **Ottman Chouqar**

[Github](https://github.com/Otmanbboy)
[LinkedIn](https://www.linkedin.com/in/ottman-chouqar-05b50494/)
