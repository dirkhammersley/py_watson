'''
'''

import json
import soundslib as sl
import requests

username = ''
password = ''
api_url = ''

watson_default_params = {
    'continuous': False,
    'timestamps': False,
    'word_confidence': True,
}

request_encoding = {'content-type': 'audio/wav'}

#Transcribe each WAV to Watson
fname = 'C:/Users/dmetge/Desktop/rando_sounds.wav'
sl.record_sound(fname, 5)
# Download watson's response
#tname = 'amy.json'
print "Transcribing ", fname, "..."
with open(fname, 'rb') as r:
	watson_response = requests.post(api_url, data=r, auth=(username, password), params=watson_default_params, headers=request_encoding, stream=False)
	transcript = json.loads(watson_response.text)['results'][0]['alternatives'][0]['transcript']
	for j in transcript.split():
		print j


# Print out the raw transcript and word csv
with open("transcript.txt", "w") as t:
	t.write(transcript)
