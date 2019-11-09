#--------------------------------------------------------------
#Imports
#--------------------------------------------------------------
import json
import pandas as pd
import math
from pandas import ExcelWriter
from pandas import ExcelFile
import tldextract
import numpy as np
from ibm_watson import ToneAnalyzerV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


#The ToneAnalyzer class from WDC

API_KEY = 'XenJKVz9AqhiQ4NuVxlTnU39oTcI4JWDcKgzs2jT3B37'
URL = 'https://gateway-lon.watsonplatform.net/tone-analyzer/api'



authenticator = IAMAuthenticator(API_KEY)
tone_analyzer = ToneAnalyzerV3(
    version='2017-09-21',
    authenticator=authenticator
)

tone_analyzer.set_service_url(URL)


def sentimentAnalyzer(excelFile):
    # comments = pd.read_excel(excel_file)

    print(excelFile)
    print('uploads/'+excelFile)
    comments = pd.read_excel('uploads/'+excelFile, header=None, skiprows=6)

    comments[6].fillna('Neutral', inplace=True)

    comments[8] = "Nil"

    xyz = comments.head()


    commentContent = comments[6]

    print('content length',len(comments))

    for i in range(len(comments)):
        text = comments[6][i]
        print(i,text)
        tone_analysis = tone_analyzer.tone(
            {'text': text},
            content_type='application/json'
        ).get_result()
        # print(json.dumps(tone_analysis, indent=2))

        toneData = json.dumps(tone_analysis, indent=2)

        json_data = json.loads(toneData)

        toneName = json_data['document_tone']['tones']

        if len(toneName) == 0:
            toneIdentified = 'Neutral'
        else:

            toneIdentified = toneName[0]['tone_name']
        print(toneIdentified)
        if toneIdentified == 'Tentative':
            toneValue = 0
        elif toneIdentified == 'Confident':
            toneValue = 1
        elif toneIdentified == 'Analytical':
            toneValue = 1
        elif toneIdentified == 'Sadness':
            toneValue = 0
        elif toneIdentified == 'Joy':
            toneValue = 1
        elif toneIdentified == 'Fear':
            toneValue = 0
        elif toneIdentified == 'Anger':
            toneValue = 0
        else:
            toneValue = 2

        comments[8][i] = toneValue

    # comments.to_excel("output.xlsx")

    writer = ExcelWriter('analyzed_data.xlsx')
    comments.to_excel(writer,'Sheet1',index=False)
    writer.save()



def displayResults():
    # comments = pd.read_excel(excel_file)
    comments = pd.read_excel('analyzed_data.xlsx')

    xyz = comments.head()
    positive = []
    negative = []
    neutral = []
    for i in range(len(comments)):
        tone = comments[8][i]

        userData = [comments[2][i],comments[6][i],comments[8][i]]

        

        if tone == 1:
            # print(i,userData)
            positive.append(userData)
        elif tone == 2:
            neutral.append(userData)
        else:
            negative.append(userData)

    print('positive',len(positive))
    print('neutral',len(neutral))
    print('negative',len(negative))
    results = [positive,neutral,negative]
    return results