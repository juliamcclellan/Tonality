import os
import json
from watson_developer_cloud import ToneAnalyzerV3
from glob import glob

tone_analyzer = ToneAnalyzerV3(
  version='2016-05-19',
  username='aa868ff9-28a0-4ec7-a7e5-d41a8a1198a0',
  password='LU0EOlno2TNq'
)

def analyze(text):
    tone = tone_analyzer.tone(text, tones='emotion', content_type='text/plain')
    #print(json.dumps(tone, indent=2))

analyze("the weather has been so dreary lately")
