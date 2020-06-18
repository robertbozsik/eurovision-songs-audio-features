# Audio Features of Songs in the Eurovision Song Contest

Şelale Urun & João Fernandes & Robert Bozsik
June 2020

# Project Description & Goals

This projects main goal is to overcome the challenges of obtaining data from different sources such as APIs \
and the website. Also to merge all the data collected and create one dataset.


# Questions

- What are the features of songs that won the Eurovision? 
- What are the features of songs that got the least points? 

# Dataset

The dataset has following columns: 

*Data gained from Web 
Year: Event Year
Host City: Event Venue
Country: Country of participants/artist
Contestant: Name of the artist.
Song: Name of the track
Points: Total number of points.
Place: Placement according to total points.

*Data gained from Spotify 
Uri: The Spotify URI for the track. \
Danceability : It describes how suitable a track is for dancing.\
Energy: It represents a perceptual measure of intensity and activity. Typically, energetic tracks feel fast, loud, and\ noisy. 
Key: The estimated overall key of the track.\
Loudness: The overall loudness of a track in decibels (dB). \
Mode: It indicates the modality of a track, the type of scale from which its melodic content is derived. \
Speechiness: It detects the presence of spoken words in a track. \
Acousticness: A confidence measure from of the track. 1.0 represents high confidence the track is acoustic. \
Instrumentalness: It predicts whether a track contains no vocals.\
Liveness: It detects the presence of an audience in the recording.\
Valence: It describes the musical positiveness conveyed by a track. Tracks with high valence sound happy, cheerful, \ euphoric.
Tempo: The overall estimated tempo of a track in beats per minute.\
Duration_ms: The duration of the track in milliseconds.
Time_signature: An estimated overall time signature of a track. 


# Workflow

1. Data Extraction: 
Techniques used in the project are Web Scrapping: https://eurovision.tv/events and Spotify Web API:  https://developer.spotify.com/documentation/web-api/libraries/ 

2. Data Merging: 
Datasets are merged with the help of functions.

3. Data Cleaning: Type Converting



# Resources:

Eurovision Song Contest Website: https://eurovision.tv/events \
Spotify API: https://developer.spotify.com/documentation/web-api/ \
Python: https://www.python.org/ \
Jupyter Notebook: https://jupyter.org/
