# Bankruptcy Prevention System

Predicting company bankruptcy risk from financial indicators using supervised classification — with a Streamlit app for live predictions.

---

## The Problem

Bankruptcy doesn't happen overnight — financial data usually shows warning signs months before a company collapses. But manually reviewing financial ratios across hundreds of companies is slow and inconsistent. This project automates that early-warning process using machine learning.

---

## Dataset

Financial risk indicators for companies, with a binary label:
- `0` → At risk of bankruptcy
- `1` → Financially stable

**Features:** industrial risk, management risk, financial flexibility, credibility, competitiveness, and operating risk — all scored on a 0–1 scale.

---

## What I Built

**Notebook (`Bankruptcy Prevention.ipynb`):**
- Loaded and explored the dataset — checked class distribution, feature correlations
- Preprocessed with label encoding and StandardScaler
- Trained Logistic Regression, Decision Tree, Random Forest, and KNN
- Evaluated with accuracy, confusion matrix, and classification report
- Chose the best model based on recall — because predicting a bankrupt company as safe is much worse than the reverse

**Streamlit App (`app.py`):**
- Input sliders for each financial indicator
- Instant prediction with probability score
- Clean, simple UI anyone can use without knowing Python

---

## Results

Random Forest gave the best performance overall, with high accuracy and strong recall on the bankruptcy class.

---

## Run Locally

```bash
pip install pandas numpy scikit-learn streamlit
streamlit run app.py
```
