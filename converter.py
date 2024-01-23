import requests
import config
import json
import base64
from io import BytesIO


api_gateway_url = config.api_gateway_url
def convert_audio(text):
    import pygame
    payload = {'text': text}
    response = requests.post(api_gateway_url, json=payload)
    # print(response.status_code)
    # print(response.text)
    audio = json.loads( response.text)
    print(type(audio))
    decoded_audio = base64.b64decode(audio["audio"])
    audio_stream = BytesIO(decoded_audio)
    pygame.init()
    sound = pygame.mixer.Sound(audio_stream)
    pygame.mixer.Channel(7).play(sound)
    pygame.time.wait(int(sound.get_length() * 1000))
    pygame.mixer.quit()
    pygame.quit()




