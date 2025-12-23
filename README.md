# Twitter-Disaster-Recognition-NLP
Project Overview-
This project focuses on classifying tweets to determine whether they are related to real disaster events or not.
Using Natural Language Processing (NLP) and Machine Learning, the model learns patterns from tweet text and predicts disaster-related tweets accurately.

This project follows a complete ML lifecycle:
Data analysis
Text preprocessing
Feature engineering
Model training & evaluation
Model deployment using Flask
Generating predictions for unseen test data

Problem Statement-
Given a tweet’s text, predict:
1 → Disaster-related tweet
0 → Not a disaster tweet

Dataset Description-
The project uses three CSV files:
1️⃣ train.csv
Contains labeled tweets used for training.
id – Tweet ID
keyword – Disaster-related keyword (optional)
location – Tweet location (optional)
text – Tweet content
target – Label (0 or 1)

2️⃣ test.csv
Contains tweets without labels.
Used for final predictions.

3️⃣ sample_submission.csv
Shows the required format for submission.

Exploratory Data Analysis (EDA)-
Checked dataset size and structure
Identified missing values in keyword and location
Observed slight class imbalance between disaster and non-disaster tweets
Visualized target distribution using count plots

Text Preprocessing-
Each tweet was cleaned using:
Lowercasing text
Removing URLs
Removing punctuation
Removing extra spaces

Feature Engineering-
Multiple features were created:
TF-IDF vectors (max 5000 features)
Tokenized text
Sentiment score using VADER
Tweet length
Hashtag count
Mention count
TF-IDF features were used for final modeling.

Models Trained-
Two machine learning models were trained and compared:
1️⃣ Logistic Regression
Simple and effective for text classification
Performed best overall

2️⃣ Random Forest
Tree-based ensemble model
Slightly lower performance than Logistic Regression

Model Evaluation-
Evaluation was done using:
Accuracy
Precision
Recall
F1-score
Confusion Matrix
ROC Curve
Precision-Recall Curve

Final Performance (Logistic Regression)-
Accuracy: ~81.8%
ROC-AUC: ~0.86
Better balance between precision and recall

Logistic Regression was selected as the final model

Overfitting Check-
Training Accuracy: ~86.9%
Testing Accuracy: ~81.8%
The small gap indicates no major overfitting and good generalization.

Model Serialization-
The trained components were saved using pickle:
disaster_model.pkl → Trained Logistic Regression model
tfidf_vectorizer.pkl → TF-IDF vectorizer
These files are used during deployment.

Web Application (Flask)
A simple Flask web app was created:
Users can enter tweet text
Model predicts whether it is disaster-related
Clear and user-friendly output shown on the webpage

Routes:
/ → Home page
/predict → Prediction endpoint

Test Data Prediction-
Test tweets were cleaned using the same preprocessing steps
TF-IDF vectorizer transformed the text
Model predicted the target values
Predictions were saved as my_submission.csv

Output File-
my_submission.csv

Contains:
id
target (predicted label)
