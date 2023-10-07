## Corn/Maize Disease Classification and AgricAid Bot

This application aids farmers in diagnosing diseases affecting corn and maize. It utilizes a Deep Learning model for disease classification and provides real-time recommendations via an AI-powered chatbot, the AgricAid bot, which uses OpenAI's GPT-3.5 API.

![App Screenshot 1](/agric-aid/screenshot/agricaid.png?raw=true "Corn/Maize Disease Classification")

![App Screenshot 2](/agric-aid/screenshot/agricaid1.png?raw=true "AgricAid Bot")  

### Features

- `Disease Classification:` Upload an image of corn or maize leaves to predict potential diseases.
- `AgricAid Bot:` An AI-powered chatbot that provides advice and recommendations based on disease classifications.

### Getting Started

#### Prerequisites

- Python 3.8+
- Docker installed on your machine
- OpenAI API key (sign up at `https://openai.com/` to obtain the key)
- Virtual environment (recommended)

### Installation

1. Clone the repository:

  -  `https://github.com/sowole-aims/agric-aid.git`

2. Navigate into the project directory and create a virtual environment:
- `cd agric-aid`
- `python -m venv venv`

3. Activate the virtual environment:
- `.\venv\Scripts\activate` (Windows)
- `source venv/bin/activate` (macOS and Linux)

4. Install the required packages:
- `pip install -r requirements.txt`

 5. Set up the OpenAI API key:
 - Open the `app.py` file and replace "YOUR_OPENAI_API_KEY" with your actual OpenAI API key.Make sure never to commit this key to public repositories.
- Save the changes.

6. Run the application:

- `python app.py`
- Navigate to `http://127.0.0.1:5000/` in your web browser to access the application.

4. Build the Docker image:

`docker build -t agricaid .`

5. Run the Docker container:

`docker run -p 5000:5000 agricaid`

6. Access the applicationS:

Open your web browser and navigate to `http://localhost:5000` to access the API.


### Usage
#### Disease Classification:
Navigate to the home page, upload an image of the corn or maize leaf, and click "Predict". The result will show the predicted disease and confidence percentage.

#### AgricAid Bot:
Navigate to the chatbot page. You can ask the bot for advice, treatment options, preventive measures, etc., based on your crop's disease classification.

### License

This project is licensed under the [MIT License](https://github.com/sowole-aims/agric-aid/blob/main/LICENSE).

### Acknowledgements
- Kaggle for Corn/Maize disease dataset
- OpenAI for GPT-3.5 models.
- The team behind OpenCV for image processing.
- Keras and TensorFlow teams for deep learning capabilities.