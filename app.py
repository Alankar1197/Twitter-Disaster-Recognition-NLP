from flask import Flask, render_template, request
import pickle
import re
import string

app = Flask(__name__)

# Load model
with open("disaster_model.pkl", "rb") as f:
    model = pickle.load(f)

# Load vectorizer
with open("tfidf_vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

def clean_text(text):
    text = text.lower()
    text = re.sub(r'http\S+|www\S+', '', text)
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = re.sub(r'\s+', ' ', text).strip()
    return text

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    tweet = request.form['tweet']

    cleaned_tweet = clean_text(tweet)
    vectorized_tweet = vectorizer.transform([cleaned_tweet])

    prediction = model.predict(vectorized_tweet)[0]

    if prediction == 1:
        result = "🚨 Disaster Related Tweet"
    else:
        result = "✅ Not a Disaster Tweet"

    return render_template('index.html', prediction_text=result)

if __name__ == "__main__":
    app.run
