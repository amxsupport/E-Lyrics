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

SOLAlchemy
MySQL
python
Flask
Bootstrap
JavaScript
gunicorn
NGINX
DigitalOcean

### Architecture

# ![Architecture](https://i.imgur.com/DQel3Jn.png)

## Getting Started

To start using this web application, visit lyricsforlearning.net. To install it, simply clone this repository. You can start the app by running `web_app.app` and `api.v1.app` as Python modules in separate terminal windows. Please note, in order to run this app, you will need to install necessary dependencies as well as pass in the correct MySQLdb and Words API credentials respectively.

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


