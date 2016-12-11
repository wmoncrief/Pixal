# Pixal - Music Video Genre Analysis

## Project Home Page
https://foymula.github.io/pixalwebsite/

## Pixal Page
http://ec2-52-90-111-50.compute-1.amazonaws.com/



## Overview and Motivation

Our team wanted to find out if it was possible to intelligently determine the genre of a video by its youtube metadata (likes, dislikes, view count, etc.) and its average frame colors throughout the video.

After thorough analysis, Pixal emerged: a web interface that takes a YouTube URL as input, and outputs a genre classifier and an average-color-per-frame image. This is done using a combination of OpenCV color analysis and scikit-learn machine learning, and makes intelligent assumptions on our data to output a substantially accurate genre classification for the input video.

## Related Work

Our motivation primarily comes from GitHub user Sacert's 'Colors of Film' analysis, in which he analyzed popular Hollywood films and extracted avereage frame colors. He used OpenCV and some built-in python libraries to generate his output, which is an image with colors from each frame of the movie. Below is the output image for Harry Potter and the Prizoner of Azkaban:

## Initial Questions

When we began our analysis, the question we asked was, "Can we accurately predict music genre by analyzing various aspects of a music video". This question was obviously extremely broad, and we quickly realized that we needed to narrow the scope and focus in on a few important/relevant features.

Thus, we revised our question to, "Can we accurately predict music genre by analyzing average frame color and youtube's video metadata (likes, dislikes, viewcount, etc.)". This question was much more manageable, but was more geared towards a final product than the actual data science process.

We then divided our project into two separate questions, with connected, but different goals. Firstly, "What are the most defining/relevant features for a music video when it comes to genre", and, "Is it possible to leverage these features to accurately predict the genre of a music video". These are the two questions that our project really sought to answer.

## Takeaways

1. When looking at individual feature data, we notice that the genre classifiers seem to either classify everything as that particular genre, or nothing as that particular genre. This seems to indicate that none of the genres are very distinct from the others.

2. As a result of this, we see a high number of false positives or false negatives in all of our predictions.

3. No particular feature seems to be extremely important when classifying genres, which could indicate that no feature is particularly useful. We would normally expect that some features stick out as the most useful or indicative of a genre. Because we do not see this, it could mean that all of the features are not particularly useful.

Even though we did not create a strong classifier, we still count our project as successful. We learned that despite the differences in the sounds of music, the quantifiable traits (color data, metadata) that we examined are very similar.
