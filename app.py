import os
import re
import numpy as np
import cv2
import io
import openai

from flask import Flask, render_template, request, jsonify
from keras.models import load_model
from dotenv import load_dotenv, find_dotenv

#from flask_cors import CORS

app = Flask(__name__)
#CORS(app)

# Load the model
model = load_model("corn-maize-disease-model1.h5")
target_names = ['Blight', 'Common_Rust', 'Gray_Leaf_Spot', 'Healthy']

# Configure OpenAI API
#_ = load_dotenv(find_dotenv())  # read local .env file 
#openai.api_key = os.environ['OPENAI_API_KEY']



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/predict", methods=["POST"])
def predict():
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        image_stream = io.BytesIO(uploaded_file.read())
        image_stream.seek(0)
        file_bytes = np.asarray(bytearray(image_stream.read()), dtype=np.uint8)
        img = cv2.imdecode(file_bytes, 1)
        img = cv2.resize(img, (256, 256))
        img.shape = (1, 256, 256, 3)
        predictions = model.predict(img)
        predicted_class = target_names[np.argmax(predictions[0])]
        confidence = round(100 * (np.max(predictions[0])), 2)
        return render_template("result.html", predicted_class=predicted_class, confidence=confidence)
    return render_template("error.html", error_message="No file uploaded.")

# Configure OpenAI API
def configure_openai_api():
    
    openai.api_key = "OPENAI_API_KEY"

configure_openai_api()


@app.route("/agricaid")
def agricaid():
    return render_template("chatbot.html")

@app.route("/agricaidbot", methods=["POST"])
def chatbot_interaction():
    message = request.json['message']
    response_text = get_openai_response(message)
    return jsonify({"response": response_text})


def get_openai_response(message):
    prompt = """
    ---
    You are an AI-powered Agronomist Assistant chatbot specialized in corn and maize diseases. Your expertise covers identifying and 
    analyzing diseases such as 'Blight', 'Common_Rust', 'Gray_Leaf_Spot', and situations where the crop is 'Healthy'.
    Your main responsibility is to assist farmers in interpreting disease classification results presented to you by them, 
    offering guidance on disease management strategies, treatment options, and preventive measures. 
    Your response to query should be concise and brief in not more than 2 paragraphs and 100 words.
    When presented with a disease classification or agriculture related question, your approach to providing advice should be:
    a) Disease Identification
    b) Explanation of the Disease
    c) Implications of the Disease on Crops
    d) Investigation of Potential Causes
    e) Solution and Preventive Measures Development
    ---
    """
    conversation_history = [
        {"role": "system", "content": prompt},
        {"role": "user", "content": message}
    ]
    

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation_history,
         max_tokens=1064,
        temperature=0.7,
    )
    chatbot_response = response.choices[0].message["content"]

    conversation_history.append({"role": "assistant", "content": chatbot_response})

    return chatbot_response

if __name__ == "__main__":
    app.run(debug=True)

















