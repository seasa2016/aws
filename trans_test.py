import time
import boto3
import json
import requests

transcribe = boto3.client('transcribe')
job_name = "test3"
job_uri = "https://s3-us-west-2.amazonaws.com/project-desk/rec_4s.mp3"
transcribe.start_transcription_job(
    TranscriptionJobName=job_name,
    Media={'MediaFileUri': job_uri},
    MediaFormat='mp3',
    LanguageCode='en-US'
)
while True:
    status = transcribe.get_transcription_job(TranscriptionJobName=job_name)
    if status['TranscriptionJob']['TranscriptionJobStatus'] in ['COMPLETED', 'FAILED']:
        break
    print("Not ready yet...")
    time.sleep(5)

start  = status.find("'TranscriptFileUri': '")
end = status.find("'",start+len("'TranscriptFileUri': '"))
url = status[start+len("'TranscriptFileUri': '"):end]



r = requests.get(url)
print(r.content)
r = requests.get(url)
print(r.content)