"""
This module initiates the Flask application for the Emotion Detection service.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def render_index_page():
    """
    Renders the main index page of the application.
    """
    return render_template("index.html")

@app.route("/emotionDetector")
def emotion_detector_route():
    """
    Score text sentiment.
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the detector function and receive the response dictionary
    emotions = emotion_detector(text_to_analyze)

    # Extract specific emotion scores from the dictionary
    anger = emotions['anger']
    disgust = emotions['disgust']
    fear = emotions['fear']
    joy = emotions['joy']
    sadness = emotions['sadness']
    dominant_emotion = emotions['dominant_emotion']

    # Handle the case where the input text is invalid or blank
    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    # Construct the output response string
    output = (
        f"For the given statement, the system response is 'anger': {anger}, "
        f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )

    return output

if __name__ == "__main__":
    app.run(host="localhost", port=5000)
