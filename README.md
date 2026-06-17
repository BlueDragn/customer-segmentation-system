# Customer Segmentation System

## Overview

Customer Segmentation System is a machine learning project that groups customers into meaningful segments based on their behavior and demographic characteristics.

The goal is to identify different customer groups that can be analyzed and targeted separately for business decision-making.

This project is part of the AI/ML Engineering roadmap and focuses on unsupervised learning using clustering techniques.

---

## Project Objectives

- Load and validate customer data
- Preprocess customer information
- Engineer useful features
- Apply clustering algorithms
- Analyze and interpret customer segments
- Build a reusable ML pipeline

---

## Dataset

Dataset: Mall Customers Dataset

Features:

- CustomerID
- Gender
- Age
- Annual Income (k$)
- Spending Score (1-100)

Target:

This is an unsupervised learning project, so there is no target variable.

---

## Planned Pipeline

```text
Customer Data
      ↓
Data Loading
      ↓
Preprocessing
      ↓
Feature Engineering
      ↓
Feature Scaling
      ↓
K-Means Clustering
      ↓
Segment Analysis
```

---

## Project Structure

```text
customer-segmentation-system/
│
├── data/
│   └── Mall_Customers.csv
│
├── src/
│   ├── data_loader.py
│   ├── preprocessor.py
│   ├── feature_engineering.py
│   ├── clustering.py
│   ├── analyzer.py
│   └── main.py
│
├── docs/
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Current Status

### Completed

- Project setup
- Folder structure
- requirements.txt
- .gitignore
- Dataset integration
- Data loading module
- Main entry point

### In Progress

- Data preprocessing
- Feature engineering
- Clustering
- Segment analysis

---

## How to Run

```bash
python src/main.py
```

---

## Current Output

The system currently:

- Loads the customer dataset
- Displays dataset information
- Verifies successful execution

---

## Future Improvements

### Version 1

- Data preprocessing
- Feature scaling
- K-Means clustering
- Cluster interpretation

### Future Versions

- Automatic cluster selection
- Advanced clustering algorithms
- Customer profiling reports
- Business recommendations

---

## Learning Goals

This project focuses on learning:

- Unsupervised Machine Learning
- Clustering
- Feature Scaling
- Customer Analytics
- Data Preparation for ML
- Pipeline Design

---

## Author

Built as part of the AI/ML Engineering learning roadmap.
