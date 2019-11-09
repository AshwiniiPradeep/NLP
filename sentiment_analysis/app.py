import os
import analyzer
from flask import Flask, request, render_template, url_for, redirect

app = Flask(__name__)

@app.route("/")
def fileFrontPage():
    return render_template('upload.html')

@app.route("/commentStatus")
def commentStatus():
	results = analyzer.displayResults()
	positive = results[0]
	neutral = results[1]
	negative = results[2]
	return render_template('results.html', positive=positive,neutral=neutral, negative=negative)

@app.route("/handleUpload", methods=['POST'])
def handleFileUpload():
    if 'social_media_comment' in request.files:
        socialMediaComment = request.files['social_media_comment']

        print(socialMediaComment)
        if socialMediaComment.filename != '':            
            socialMediaComment.save(os.path.join('uploads/', socialMediaComment.filename))
        excel_file = socialMediaComment.filename
        print(excel_file)
        analyzer.sentimentAnalyzer(excelFile = excel_file)
    return redirect(url_for('commentStatus'))

if __name__ == '__main__':
    app.run()     