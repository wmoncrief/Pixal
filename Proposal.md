# Project: *Video Color Analysis*
*by Team Goodnight Moon*

#### Team Members
- Clayton Petty
- Dalton Harris  
- Chris Foy
- Wes Moncrief

#### Project Goal
We will determine the average color of each frame in a given YouTube music video. We will use the average colors to compare many different music videos, using YouTube as our source. We hope to find relationships between channels, genres, and popularity based on their average frame color for the duration of the video. Our end goal is to automatically classify (with substantial accuracy) music videos that a user uploads, into our predetermined categories.

### What is the need? Who wants or benefits?
This will give insight into what genres influence the colors of a music video, and if this has any effect on popularity. It will also help us to understand how different colors are used in different genres of videos.

### What data (or datasets)?
We will use videos from YouTube. We will write a quick Python script to get the average color from each frame of each video.

### What is your "data science" toolkit? You should list specific tools / packages you will use.
- OpenCV
  - This is 'Open Computer Vision', which is implemented in Python as cv2. It will help us get data from video frames.
- Classifiers
  - We will try to classify different videos based on their frame color data. We will use a test & train set.
- Multiple Regression
  - We will use this to see if we can find correlations between videos that we expect to be related.

### Incremental Steps to Completion
1. Choose videos from YouTube to analyze
2. Map videos to their frame color data representation
3. Use regression to search for patterns in data
4. Use classifiers to attempt predictions based on author, genre, popularity, etc.


### Preliminary sketch of what you hope to find.
We are hoping to find a correlation between genre of a music video and it's average frame color. We expect to find commonality between videos by the same author - they often have the same genre in their music videos.
