import json

temp = """{'TranscriptionJob': {'TranscriptionJobName': 'test1', 'TranscriptionJobStatus': 'COMPLETED', 'LanguageCode': 'en-US', 'MediaSampleRateHertz': 44100, 'MediaFormat': 'mp3', 'Media': {'MediaFileUri': 'https://s3-us-west-2.amazonaws.com/project-desk/rec_4s.mp3'}, 'Transcript': {'TranscriptFileUri': 'https://s3.us-west-2.amazonaws.com/aws-transcribe-us-west-2-prod/680330329314/test1/3fceee31-c2e2-4e74-bc10-fa2bed5d6fe3/asrOutput.json?X-Amz-Security-Token=FQoGZXIvYXdzEOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaDFPnwYnl1ky0wx9ISiK3AyzBTk%2BkgiiQVvlBmn3EEm4dxR2iVpR%2FCv94NWSh4ecxknX0icxL%2BQzmjIu1Od06j%2BF18JhFWnenffE0nYceXPE2FKUghC%2BBAkOXB3jSiAs%2FFBgMhljGzF1mzQJDMGxoynlfAiPAVOdAGxczgiPk8o2xgdpcWs5v2y86wy9%2BDAXpIXqlrZdLTlPKrW71NVkdsZFVlHy%2FxLnn3JaO8hcvb04auMZo1mnR9QCBwFw47%2FBc9Zj0xG0iwBceyiUJxvHBl9YhBuMicZT0%2BxGP6IB2F7D01zVzXzrlcef6hcFPqIP4x9pnUGShpOVydF%2Bk9usw6eAYY%2FosprftzTNNlr9rgnvz5BLZTtfwvLms1QFm08dNNke25vmeFI4IWr9pin3jmoEe9wVI8PQAswRR9wTB1AWWPcEWcmn6KuElkGeUEMsAsKt7s8nIWwWZ8qZc75dLlV6OrNg2P32qhBXnAiP3Ij9bL44Ae3ij%2F3nGPA0cJpOvhSz6oaj2HiDuLgP6oDW5kFYq%2BOMBf55lPpHiYkxx4pU7O%2BUl1CzemkDkjjf49LQdCAbGWbvHHhWsXYjAHZI6tvMZ6YHJulIoyaWE3gU%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20181012T230543Z&X-Amz-SignedHeaders=host&X-Amz-Expires=899&X-Amz-Credential=ASIARFLZMHCPOMSN2OE6%2F20181012%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Signature=debc681f3ddb3ad9e064b37b2f6804a5369b66e0dddbcd73830e52cfe2402929'}, 'CreationTime': datetime.datetime(2018, 10, 13, 7, 4, 41, 1000, tzinfo=tzlocal()), 'CompletionTime': datetime.datetime(2018, 10, 13, 7, 5, 42, 813000, tzinfo=tzlocal()), 'Settings': {'ChannelIdentification': False}}, 'ResponseMetadata': {'RequestId': '58814d89-ce73-11e8-b759-0b922a68999a', 'HTTPStatusCode': 200, 'HTTPHeaders': {'content-type': 'application/x-amz-json-1.1', 'date': 'Fri, 12 Oct 2018 23:05:43 GMT', 'x-amzn-requestid': '58814d89-ce73-11e8-b759-0b922a68999a', 'content-length': '1514', 'connection': 'keep-alive'}, 'RetryAttempts': 0}}"""

start  = temp.find("'TranscriptFileUri': '")
end = temp.find("'",start+len("'TranscriptFileUri': '"))

print(temp[start+len("'TranscriptFileUri': '"):end])




