# Audio Features of Songs in the Eurovision Song Contest
This project was submitted as the first project of the Ironhack Bootcamp for Data Analysis in Berlin.\
It was made with Python, Jupyter Notebook and the Spotify API.

# Team members:
Şelale Urun & João Fernandes & Robert Bozsik

# Project Description & Goals:
The goal of the project was to gather data from different sources, including APIs and web scraping. Merge the data and gain a clean dataset ready for further analysis.

# Workflow:
1. Data Extraction: 

    1.1. We scraped the Eurovision website (https://eurovision.tv/events) for information on the songs that have 
entered Eurovision since 1956.

    Code: 1_scrape_eurovision.ipynb

    1.2. We used the song names to submit search queries to the Spotify API (with the help of the Spotipy library)
in order to obtain Spotify's Unique Resource Identifiers (URI) for each song. Out of the 20 results returned by 
the API for each search, we chose the first one where the artist name matched the artist name we had scraped in 1.1.

    Code: 2_Spotify_song_search.ipynb

    1.3. We submitted the URIs in a second query to the Spotify API to get the audio features for each song.

    Code: 3_Spotify_audio_features.ipynb

2. Data Merging: 

    Code: 4_Merging_the_data.ipynb

    2.1. We merged the scraped data and the data obtained through the Spotify API in a single dataframe. 

3. Data Cleaning:

    Code: 4_Merging_the_data.ipynb

    3.1. We dropped the rows for which we weren't able to get audio feature information. We also had to convert the type 
of some columns, as well as alter the "Place" column from ordinals ("1st", "2nd"...) to numerals (1, 2...).

More details on the workflow are available as comments in the jupyter notebooks.

The presentation is available on Google Drive: 
https://docs.google.com/presentation/d/1dEkCgTrxBN5ORkngL4GVtywA2y_l7e_gzB8o4SXS9g4/edit?usp=sharing

# Dataset:
The merged dataset has following columns: 

Data gained from Web 
 - Year: Event Year
 - Host City: Event Venue
 - Country: Country of participants/artist
 - Contestant: Name of the artist
 - Song: Name of the track
 - Points: Total number of points
 - Place: Placement according to total points

Data gained from Spotify 
 - Uri: The Spotify URI for the track
 - Danceability : It describes how suitable a track is for dancing
 - Energy: It represents a perceptual measure of intensity and activity. Typically, energetic tracks feel fast, loud, and noisy
 - Key: The estimated overall key of the track
 - Loudness: The overall loudness of a track in decibels (dB)
 - Mode: It indicates the modality of a track, the type of scale from which its melodic content is derived.
 - Speechiness: It detects the presence of spoken words in a track
 - Acousticness: A confidence measure from of the track. 1.0 represents high confidence the track is acoustic
 - Instrumentalness: It predicts whether a track contains no vocals
 - Liveness: It detects the presence of an audience in the recording
 - Valence: It describes the musical positiveness conveyed by a track
 - Tempo: The overall estimated tempo of a track in beats per minute
 - Duration_ms: The duration of the track in milliseconds
 - Time_signature: An estimated overall time signature of a track.

# Questions for further analysis:
- Are there any features that correlate with placing high in Eurovision?
- What are the features of songs that won the Eurovision? 
- What are the features of songs that got the least points? 

# Resources:
Eurovision Song Contest Website: https://eurovision.tv/events \
Spotify API: https://developer.spotify.com/documentation/web-api/ \
Spotipy: https://spotipy.readthedocs.io/en/2.12.0/ \
Python: https://www.python.org/ \
Jupyter Notebook: https://jupyter.org/
