## Pixal Script

**Intro Montage**

*tires screech*

This is Freddy. Freddy has spent his morning watching various music videos on his tube television, but can't seem to figure out just what 
genre of video he's watching. You see how puzzled he is? Something needs to be done.

Introducing Pixal, the music video genre classifier. Input a video URL, and Pixal will analyze its duration, likes and dislikes, average frame color, and more to predict the genre of their video.

We used the OpenCV library to analyze frame color, and scikit learn machine learning to make our predictions. We created a comprehensive set of a thousand videos from YouTube to train our model, which includes two hundred videos from each Pop, Rock, Country, Rap, and EDM.

We want to look at average frame color for the duration of the video, and use these values in our machine learning algorithm. When we pass in a music video, the openCV tool captures RGB values for each frame, and puts them into a dataframe. We take these values, along with viewer statistics, and create our training model in sci-kit learn. 


After completing our training model, we notice that the output is not as accurate as we'd like. You'll notice that we often classify pop videos as rock, and rap videos as country. The average success rate of our multi-variant random forest classifier is consistently under 50%. To understand more of the deficiencies in our classifier, we looked into seeing which genres were particularly different than others. For example, you would expect that country and EDM videos would be completely different. However, when considering binary classifiers, regardless of genre, the classifiers seem to predict that either the majority of videos are a given genre, or that almost no videos were that genre. 

Upon further analysis of feature importance, we can see that with the exception of the pop viewcount and likes, no feature seems to be particularly useful when classifying these videos. This probably indicates that we have a poor feature set, and thus is not ideal for classifying music videos by genre.

Now that we have a predictive model, we can start classifying our videos by genre. As we can see here, Pixal gives us the generated openCV image, and most importantly, the predicted genre. Pixal has successfully classified Rebecca Black's pop-country hit "Friday", and provides the user the opportunity to listen to the video right there on the screen.



