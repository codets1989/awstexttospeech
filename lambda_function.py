import json
import boto3
import base64
def lambda_handler(event, context):
    text_payload=json.loads(event['body'])['text']
    polly = boto3.client('polly')
    s3 = boto3.client('s3')
    response = polly.synthesize_speech(Text=text_payload, VoiceId='Joanna', OutputFormat='mp3')
    filename = 'sound.mp3'
    audio_bytes = response['AudioStream'].read()
    s3.put_object(Bucket = 'texttospeechbuck',Key = filename,Body = audio_bytes)
    encoded_audio = base64.b64encode(audio_bytes).decode('utf-8')

    return {
        'statusCode': 200,
        'body': json.dumps({'audio':encoded_audio})
    }
