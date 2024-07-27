# Sentiment Analysis of Flipkart Product Reviews

This project focuses on sentiment analysis of Flipkart product reviews using various machine learning models. The goal is to classify reviews as either positive or negative based on their content. The analysis is supported by a web application built using Flask, which allows users to input reviews and receive real-time sentiment predictions.

## Project Overview

The sentiment analysis is carried out using multiple machine learning algorithms to determine the most effective model for classifying the sentiment of reviews. The project includes data preprocessing, model training, hyperparameter tuning, and deployment through a web interface.

## Features

- **Data Preprocessing**: 
  - Cleans the review text by removing special characters, digits, and converting text to lowercase.
  - Removes stop words and applies lemmatization to standardize the text data.

- **Model Training**:
  - Utilizes various classification algorithms, including Naive Bayes, Decision Tree, Logistic Regression, Random Forest, Support Vector Classifier (SVC), and K-Nearest Neighbors (KNN).
  - Uses GridSearchCV to tune hyperparameters and select the best model.

- **Web Interface**:
  - Built with Flask, it provides an interface where users can submit reviews and receive sentiment predictions.
  - Displays the sentiment result in a user-friendly format.

- **Model Storage**:
  - Models are saved and loaded using joblib, facilitating efficient deployment and usage in the web application.

## Algorithms Used

- **Naive Bayes**: A probabilistic classifier based on Bayes' theorem.
- **Decision Tree**: A model that splits data into subsets based on feature values.
- **Logistic Regression**: A statistical model that uses logistic functions to predict class probabilities.
- **Random Forest**: An ensemble method that combines multiple decision trees to improve performance.
- **Support Vector Classifier (SVC)**: A classifier that finds the hyperplane that best separates classes.
- **K-Nearest Neighbors (KNN)**: A non-parametric method that classifies data based on the closest training examples.

## Model Performance

- **Naive Bayes**: Achieved an F1 Score of 0.92 on test data.
- **Decision Tree**: Achieved an F1 Score of 0.92 on test data.
- **Logistic Regression**: Achieved an F1 Score of 0.92 on test data. This model was selected for deployment due to its performance and efficiency.

## Web Interface

The web application allows users to:
1. **Input Reviews**: Enter product reviews in a text area.
2. **Get Predictions**: Submit reviews to receive sentiment analysis results.
3. **View Results**: Display sentiment as either "Positive" or "Negative."

## Directory Structure
Sentiment-Analysis-of-Flipkart-Product-Reviews/

│

├── app.py # Flask application for the web interface

├── home.html # HTML template for the review submission page

├── prediction.html # HTML template for displaying prediction results

├── requirements.txt # List of Python package dependencies

├── data_badminton.csv # Dataset file containing Flipkart product reviews

├── best_models/ # Directory containing saved models

 └── logistic_regression.pkl # Trained Logistic Regression model
 
|

 └── README.md # Project overview and instructions

## Model Files

- **`logistic_regression.pkl`**: The trained Logistic Regression model used for sentiment prediction.
