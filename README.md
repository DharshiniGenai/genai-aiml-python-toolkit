# 🚀 Gen AI and AI/ML Fundamentals with Python Basics

## 🌟 Project Vision

This project is a real-world inspired AI/ML mini pipeline system developed completely using Python fundamentals without relying on external machine learning libraries. The main objective of this project is to demonstrate how raw and unstructured data can be transformed into meaningful business insights through different stages of data processing and analysis.

The workflow simulates how real AI/ML systems operate in industry-level environments. The project begins with messy input data containing missing values, duplicates, incorrect data types, and inconsistent records. The system then cleans the data, generates useful features, performs rule-based prediction, analyzes customer feedback sentiment, and finally produces structured output reports.

This project showcases the complete journey:

**Raw Data → Data Cleaning → Feature Engineering → Prediction → Text Analytics → Final Reports**

The project is designed in a modular and reusable way to imitate early-stage machine learning pipelines and data engineering systems used in real organizations.

---

# 🧠 What This Project Demonstrates

This project demonstrates several important AI/ML and Python programming concepts including:

* Data Cleaning and Preprocessing
* Feature Engineering
* Dictionary-Based Mini Feature Store
* Rule-Based Classification Logic
* Basic Natural Language Processing (NLP)
* Sentiment Analysis
* Evaluation Metrics Calculation
* JSON and CSV File Handling
* Modular Programming
* CLI-Based Interactive Application Design
* End-to-End AI/ML Workflow Simulation

---

# 📂 Project Structure

```text
Project1/
│
├── main.py
├── loader.py
├── cleaner.py
├── features.py
├── predictor.py
├── text_analytics.py
├── report.py
│
├── input/
│   ├── raw_data.csv
│   └── feedback.txt
│
├── outputs/
│   ├── clean_data.csv
│   ├── summary_report.txt
│   ├── feature_store.json
│   ├── predictions.csv
│   ├── evaluation.txt
│   ├── feedback_scores.csv
│   └── insights_report.txt
│
└── README.md
```

---

# ⚙️ How to Run This Project

## 1️⃣ Install Python

Download and install Python from the official website:

https://www.python.org/

Make sure Python is added to system PATH during installation.

---

## 2️⃣ Open the Project Folder

Open terminal or command prompt inside the project directory.

Example:

```bash
cd Project1
```

---

## 3️⃣ Run the Application

Execute the following command:

```bash
python main.py
```

---

## 4️⃣ Choose CLI Menu Options

The program provides an interactive command-line menu:

```text
1 → Run Full Pipeline
2 → Exit
```

Selecting the full pipeline automatically performs all assignments sequentially.

---

# 🔍 Module Breakdown

## 🧹 1. Data Cleaning & Preprocessing Pipeline

The cleaning module transforms messy and inconsistent raw data into a clean structured dataset suitable for analytics and ML-style processing.

The dataset intentionally contains:

* Missing values
* Invalid numeric inputs
* Duplicate user IDs
* Incorrect formats
* Outliers
* Mixed data types

### ✔ Cleaning Operations Performed

* Standardization of missing values
* Type conversion for age and income
* Removal of invalid records
* Outlier handling
* Duplicate removal using latest signup date
* Missing value imputation using median/default values
* Boolean normalization for purchased column
* Whitespace cleanup and formatting

### ✔ Derived Features Created

* `income_bucket`

  * Low
  * Mid
  * High

* `is_adult`

  * True
  * False

### 📌 Outputs Generated

* `clean_data.csv`
* `summary_report.txt`

---

## 🧩 2. Feature Store (Mini ML Engineering System)

This module simulates a simplified feature engineering system similar to real-world machine learning feature stores.

User-level behavioral features are generated and stored using dictionary-based structures.

### ✔ Features Generated

* total_events
* views_count
* cart_count
* purchase_count
* avg_price_viewed
* most_viewed_product
* conversion_flag

The module demonstrates aggregation logic, reusable functions, and structured JSON feature storage.

### 📌 Output Generated

* `feature_store.json`

---

## 🤖 3. Rule-Based Classifier

This module implements a basic machine learning-style prediction system using Python logic instead of ML libraries.

A score is calculated based on predefined business rules. Depending on the score threshold, users are classified into categories.

### ✔ Rules Used

* High income → +2 points
* Adult user → +1 point

### ✔ Prediction Logic

* Score ≥ 2 → Prediction = 1
* Score < 2 → Prediction = 0

The system also tracks:

* Triggered rules
* Prediction scores
* Evaluation statistics

### 📊 Evaluation Metrics Calculated

* Accuracy
* Precision
* Recall

### 📌 Outputs Generated

* `predictions.csv`
* `evaluation.txt`

---

# 💬 4. Text Analytics & Sentiment Analysis Engine

This module performs basic Natural Language Processing (NLP) using Python string operations and keyword matching.

Customer feedback text is analyzed to determine sentiment polarity.

### ✔ NLP Operations Performed

* Text tokenization
* Positive word counting
* Negative word counting
* Sentiment score calculation
* Positive/Negative classification
* Frequent word extraction

### ✔ Positive Keywords Used

* great
* easy
* love
* excellent

### ✔ Negative Keywords Used

* bad
* slow
* hard
* expensive

### 📌 Outputs Generated

* `feedback_scores.csv`
* `insights_report.txt`

---

# 🔄 5. End-to-End Pipeline Workflow

The complete pipeline integrates all modules into a single execution workflow.

The execution order is:

```text
Data Loading
   ↓
Data Cleaning
   ↓
Feature Engineering
   ↓
Rule-Based Prediction
   ↓
Text Analytics
   ↓
Report Generation
```

This simulates a simplified real-world AI/ML production workflow pipeline.

---

# 🧠 Key Concepts Used

This project applies several core Python and AI/ML foundational concepts including:

* CSV and JSON File Handling
* Functions and Modular Programming
* Loops and Conditional Logic
* Dictionaries and Data Structures
* Data Cleaning Techniques
* Feature Engineering
* Rule-Based Prediction Systems
* Basic NLP and Sentiment Analysis
* Evaluation Metric Computation
* Command Line Interface Design

---

# ⚠️ Assumptions Made

Some assumptions were used to simplify the implementation while maintaining realistic workflow behavior.

* Rule-based logic is used instead of ML models
* Missing numeric values are replaced using median/default values
* Unknown city names are replaced with `"Unknown"`
* Synthetic behavior generation is used for feature engineering
* Keyword-based sentiment analysis is used instead of advanced NLP models

---

# 🚨 Edge Cases Handled

The system is designed to handle multiple real-world data quality issues.

### ✔ Handled Cases

* Missing or null values
* Invalid numeric data
* Duplicate records
* Outlier values
* Incorrect boolean formats
* Mixed data types
* Extra whitespace issues
* Empty feedback inputs
* Invalid age and income values

---

# 📌 Final Outcome

This project demonstrates how Python fundamentals alone can be used to design a mini AI/ML workflow system without external machine learning frameworks. It provides practical understanding of preprocessing, feature engineering, prediction logic, text analytics, modular software structure, and end-to-end pipeline execution.

The project is designed to reflect interview-style AI/ML engineering tasks and foundational industry workflows.

---

# 👨‍💻 Author

**Dharshini A**
