# Bankruptcy Prevention System

A machine learning project for identifying companies that may be at risk of bankruptcy from financial indicators. The goal is to support earlier risk review by turning raw financial ratios into an interpretable classification workflow.

## Project Overview

This project demonstrates an end-to-end supervised learning workflow:

- Data cleaning and preprocessing
- Exploratory data analysis
- Feature scaling
- Classification model training
- Model evaluation with business-focused metrics

## Business Problem

Bankruptcy can create major losses for investors, creditors, employees, and other stakeholders. Traditional financial review can be slow and subjective, so an analytical early-warning system helps prioritize companies that need closer attention.

## Dataset

- Financial ratios and company performance indicators
- Binary target variable:
  - `0`: Non-bankrupt
  - `1`: Bankrupt

## Machine Learning Approach

The workflow compares multiple classification models and selects the best-performing option based on recall and F1-score, because identifying at-risk companies is more important than only maximizing accuracy.

## Evaluation Metrics

- Accuracy
- Precision
- Recall
- F1-score
- Confusion matrix

## Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Streamlit

## Interview Highlights

- Framed bankruptcy prediction as a risk-management classification problem
- Compared classification models instead of relying on a single algorithm
- Prioritized recall and F1-score to reduce missed high-risk companies
- Built toward a deployable Streamlit application
