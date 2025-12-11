🧠 Smart Email Classifier — An AI-Powered Email Categorization System

An AI-powered system designed to clean, categorize, and prepare email datasets for intelligent spam detection and enterprise-level email classification.

This repository contains Milestone 1, focusing on data cleaning, preprocessing, merging, and creation of the final ML-ready dataset.

📁 Project Structure
Smart-Email-Classifier/
│
├── data/
│   ├── raw/        # Original datasets
│   └── clean/      # Cleaned & processed datasets
│
├── src/            # All Python scripts
│   ├── combine.py
│   ├── category.py
│   ├── final_dataset.py
│   ├── priority.py
│   └── spam_email.py
│
├── README.md
└── .gitignore

🎯 Milestone 1 — Summary (Completed)

Cleaned raw email datasets

Merged multiple datasets

Added spam/general labels

Assigned categories

Performed text preprocessing

Added engineered features

Created final_dataset.csv for training

Output file: 📌 data/clean/final_dataset.csv

🛠 Scripts Overview
Script	Purpose
combine.py -	Merge raw datasets
category.py	- Clean text + assign categories
final_dataset.py	- Generate final ML-ready dataset
priority.py -	Assign priority levels to emails
spam_email.py	- Initial spam email processing
🚀 How to Run
Step 1 — Go to src folder: cd src

Step 2 — Generate final dataset: python final_dataset.py

Dataset will be saved in: data/clean/final_dataset.csv

📌 Upcoming Milestone 2

TF-IDF vectorization

Logistic Regression & SVM models

Model evaluation (Accuracy, Precision, Recall, F1)

Confusion matrix visualization

Save trained model

👨‍💻 Author

Sai Keerthi Ambati
AI & Machine Learning Enthusiast
