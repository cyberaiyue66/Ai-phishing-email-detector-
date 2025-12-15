# AI Phishing Email Detector

## Overview
This project detects phishing emails using Natural Language Processing (NLP) and a Naive Bayes classifier.
It analyzes email text to find suspicious patterns, such as links, keywords, or attachments, and classifies messages as phishing or legitimate.

## Features
- Detects phishing keywords: urgent, verify, password, click, login, account  
- Detects suspicious links and domains  
- Machine Learning classification (Naive Bayes)  
- Works offline 
- Command-line interface (CLI)  

## Tech Stack
- Python 3.13  
- pandas  
- scikit-learn  
- pickle (for saving the trained model)  
- Regex (for feature extraction)  
  ##Project Structure
phishing-detector/
│── data/ # CSV with phishing and legit emails
│── src/ # Python source code
│ ├── extractor.py # Feature extraction functions
│ ├── model.py # Train the ML model
│ ├── detector.py # Main detection script
│── tests/ # Test emails (optional)
│── README.md # This documentation
│── requirements.txt # Required libraries
---
## Installation
1. Clone this repository:
bash
git clone https://github.com/yourusername/phishing-email-detector-ai.git
cd phishing-email-detector-ai
Install dependencies:
pip install -r requirements.txt
##rain the model (creates model.pkl)
python src/model.py
##Run the email detector:
python src/detector.py
----
#Phishing example

Urgent! Verify your account now: http://fake-bank.com
---
##Legit example
Meeting tomorrow at 10am in classroom 203

