import requests 
import json

def emotion_detector(text_to_analyze): 
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'  
    myobj = { "raw_document": { "text": text_to_analyze } }  
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  
    response = requests.post(url, json = myobj, headers=header)  
    
    formatted_response = json.loads(response.text)
    anger = formatted_response['emotionPredictions']['anger']
    disgust = formatted_response['emotionPredictions']['disgust']
    fear = formatted_response['emotionPredictions']['fear']
    joy = formatted_response['emotionPredictions']['joy']
    sadness = formatted_response['emotionPredictions']['sadness']
    #dominant_emotion = formatted_response['emotionPredictions']['joy']

    return {'anger': anger, 'disgust':disgust, 'fear': fear,'joy':joy, 'sadness':sadness}
    