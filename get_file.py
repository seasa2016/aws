import requests
import json

url = """https://s3.us-west-2.amazonaws.com/aws-transcribe-us-west-2-prod/680330329314/test/6170df8d-d303-4108-946a-2274e15d9a90/asrOutput.json?X-Amz-Security-Token=FQoGZXIvYXdzEOj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaDG4a9y7EtnLT2IMkqiK3AzG2586cxtxgmz%2BEh5VIdB9m1y1FJzc%2B7n5ZyyGMgm8G%2FlmBhJDUGYSLWCz2sTmzpFqlDE4RJH8KObExqX%2BaeMu36hb9iTIM%2FfYuPglEHw1m3Mg3Qs8yJIMhelhFKHGfGvW0L7%2FqS2D3Ia%2FQGtS%2BrJbkaQW1sDjqwfv5%2BktPnCZ%2BG3795ElgXn%2FItxu0ZO5O9DHIxP4kqn68lAJ7MilbihIFiaQrsZukpLzz9G1GYRrj%2FnfGWn7RdIZMSORLDVNPryPOfaOW%2Bq5sCssJqFxZxIAnNp4ZZZEAQxp5OLfu6ciytZKMw4OTRYP6qtQTnE9SeJIRPBQGxK%2BhgcVcvIz3E%2BWCl99jW33I%2BqQefybhX4guKsqhC2zJMqvKgKSDZ85c%2FOe5S5M3znZzgQVlhKNQe9Zyp7WViNh18CuGzvKa44ObCeVop5s%2BC6lR0iw3dKbysuLfcoWiBjCGf16zXrCIjS%2FVdfoQV0YSQTc2CJQNCAFaVbZFSRJHEg%2FPVfa8PBixhWiGlXImfjmNNN%2FhOQakvY%2Fk9TQhsrE%2BCwgu8RWUr6yUgRvhYN4q6tY5%2FhIsaEI0ufLk8VeiND8oxM%2BE3gU%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20181012T234546Z&X-Amz-SignedHeaders=host&X-Amz-Expires=900&X-Amz-Credential=ASIARFLZMHCPJWJ3BFI7%2F20181012%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Signature=ef986d1751c2213219b130d1328b9767a85c0dac0e699f7de3538cd599ca1a5e"""


r = requests.get(url)
#print(r.content)

out = json.loads(r.content)
print(out['results']['transcripts'][0]['transcript'])