''' Executing this function initiates the application of emotion
    detection to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection import emotion_detection

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_detector():
    """Processes the text passed via the 'textToAnalyze' query parameter,
    performs emotion detection using the emotion_detection module,
    and returns a formatted string summarizing the emotion scores and dominant emotion.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detection.emotion_detector(text_to_analyze)
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']
    if dominant_emotion is None:
        return "Invalid text! Please try again!."
    return (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
