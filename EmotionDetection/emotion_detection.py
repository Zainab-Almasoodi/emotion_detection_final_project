import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    inputjson = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = inputjson, headers=header)

    formatted_response = json.loads(response.text)
    all_emotion = formatted_response['emotionPredictions'][0]['emotion']

    emotion_score = {
        'anger': all_emotion['anger'],
        'disgust': all_emotion['disgust'],
        'fear': all_emotion['fear'],
        'joy': all_emotion['joy'],
        'sadness': all_emotion['sadness'],
        'dominant_emotion': max(all_emotion, key=all_emotion.get)
    }
    return emotion_score