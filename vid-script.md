## Pixal Script

**Intro Montage** [00:00]

*tires screech*

This is Freddy. Freddy has spent his morning watching various music videos on his tube television, but can't seem to figure out just what 
genre of video he's watching. You see how puzzled he is? Something needs to be done.

Of course, music of different genres sounds different, but we were curious whether or not the music videos that accompanied them had any quantifiable visual differences.
We looked at the most commonly appearing colors in music videos and tried to predict their genres based on the distribution of these colors throughout the videos as well as metadata features such as likes, dislikes, and views.

**High-Level Results**

**Overview and Motivation**

**Related Work**

**Initial Questions**

**Data Explanation**

**Future Improvements

* How did we get the data?
  * To collect our data we scraped the urls of 

**Analysis Explanation**

* Ordinal Genres
  * Here we make the genres ordinal to fit in the random forest classifiers. We add a new column to our dataframe to do so, write a function to populate it, and run it across the dataframe. We add in some boolean genre classifiers to make our analysis more fine-grained. Rather than saying "we predict this video is country with 50% confidence", we could say "this video is not edm with 90% confidence" and so on. 
* Test and Train Sets
  * We create our training and test sets by splitting the genres and making half of each genre train and half test. We aggregate by genre to make our full train and full test sets, each containing 405 records of various genres.
* Generating Random Forests
  * We start generating our random forests, and output a relative accuracy and a confusion matrix. In this first one, we simply factor in non-color variables (rating, likes, dislikes, length and viewcount), and run it across all records to predict an ordinal genre value.
  * As shown above, this method yields relatively poor results. This is because there's no distinct clusters being created by our random forest, and simple viewer statistics tell us nothing about what kind of video we're watching. However, we see that country, rap and pop are initially somewhat distinct (diagonal is the highest value), and rock and edm are getting mistaken for one another. Let's see if we can't make something of this.

* Random Forest Only Color
  * Below, we do the same random forest as above, but going strictly off of average frame color for the video.
We found the most commonly appearing color in each frame and called it the 'frame mode'. We then took all of the frame modes and found the 10 most common of them. Those became the 'color data' we use to analyze videos.
  * This actually yields worse results than just the viewer statistics, because the color of a video by itself does not determine the genre. If rappers only had red in their videos and rockers only had black this might be somewhat accurate, but that's just not the case. But, what if we pair these findings with our initial viewer statistics?
* Singling Out Pop and Rap
  * Scores are expectedly low. It seems as if we're trying to make the classifier do way too much work, and are giving it very mediocre data to go off of. Recall that we're actually trying to determine WHICH genre a video is by the above code, not whether or not a video is of ONE specific genre. This brings back the binary classifiers that we created above, let's put those to use to see if we can improve these scores.
We try pop and rap first, since they seem to be the most distinct by what we've gathered above.
  * What we're seeing here is a confusion matrix that, based on our training data, predicts whether or not a video in the test set is a pop video or not. In the "predicted" row, 0 means it predicts it's not a pop video, and that the 1 is. Likewise with the actual, 0 shows that the video actually wasn't a pop video, and the 1 shows that it was.
  * The confusion matrix above is our first effort at utilizing these binary classifiers. Most of our videos aren't pop videos (40 aren't, 10 are), and the model did a good job of picking out those that aren't pop. However, we could use some improvement in the realm of "false negatives", where the model classified a video as not pop when it actually was.
We recreated the tests above with each genre, and the results are below:
  * We ran the above test with all genres, and as shown in above analysis, our country and edm typically have very low accuracy. We've seen above that edm and rock videos are getting mixed up with one another, so we assume that something is characteristic of these 2 genres that's not of everything else. We take out the edm values from our training and test datasets, hoping to improve accuracy.

**In-Depth Conclusions/Results**

**Outro**
