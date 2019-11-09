## Social Media Sentiment Analysis using tone analyser.

Installation

1. Create a virtualenv.
   
2. Activate virtualenv and install the requirements.txt file.

   Source bin/activate
   pip install -r requirements.txt

3. Run the app.py file in the root folder.

4. Go to the default url, ie, 127.0.0.1:5000/
   Go through the instructions. 

   Use Export Comments link https://exportcomments.com/ to download comments from facebook, twitter and instagram.
   
Sample links are given below

	        https://www.facebook.com/apple/photos/a.1182756961816907/2672305722862016/?type=3&__tn__=HH-R   for Facebook Post

    		https://www.instagram.com/p/B1sh-jKActQ/?utm_source=ig_web_copy_link&comment_id=17998383688251173 for Instagram Post

    		https://twitter.com/i/status/1001867140549394432 for Twitter Post 

or you can upload comments from the comments folder.


5. Then the process take each comments through th IBM tone analyzer and based on the 7 tones the texts are classified using natural language processing.

6. Tones such as Joy, Confident and Analytical are considered as Positive.
   Sadness,Fear,Anger comes under Negative feedback.
   Comments which are tentative,not clear or used in another language or black fields comes under Neutral category.

7. Takes a total count of all feedbacks are taken and it is displayed with Username,ProfileID,comments and feedback-status are displayed.


Technology Used:
Python
IBM watson tone analyzer.
NLP