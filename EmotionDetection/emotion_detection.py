import requests 
import json

def emotion_detector(text_to_analyze): 
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'  
    myobj = { "raw_document": { "text": text_to_analyze } }  
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  
    response = requests.post(url, json = myobj, headers=header)  
    
    formatted_response = json.loads(response.text)

    main_emotion = formatted_response['emotionPredictions'][0]['emotion']
    anger_score = main_emotion['anger']
    disgust_score = main_emotion['disgust']
    fear_score = main_emotion['fear']
    joy_score = main_emotion['joy']
    sadness_score = main_emotion['sadness']

    # Store emotions in a dictionary
    emotions = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }
    # Find the emotion with the highest score
    max_emotion = max(emotions, key=emotions.get)

    dominant_emotion = max_emotion

    return {'anger': anger_score, 
    'disgust':disgust_score, 
    'fear': fear_score,
    'joy':joy_score, 
    'sadness':sadness_score,
    'dominant_emotion': dominant_emotion}
    