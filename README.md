# Data Science Portfolio

Welcome to my Data Science portfolio! This repository showcases the projects and assignments I completed during my intensive Data Science certification program. It demonstrates end-to-end machine learning workflows, statistical analysis, natural language processing, deep learning, and time-series forecasting.

**Program:** ExcelR Solutions - Data Science Certification  
**Focus:** Predictive Modeling, Statistical Inference, NLP, Neural Networks, Unsupervised Learning  
**Tools:** Python, Scikit-learn, TensorFlow/Keras, Pandas, NumPy, Matplotlib, Seaborn, Streamlit

---

## Table of Contents

1. [Capstone Projects](#capstone-projects)
   - [Bankruptcy Prevention System](#1-bankruptcy-prevention-system)
   - [Book Recommendation System](#2-book-recommendation-system)
2. [Assignments by Topic](#assignments-by-topic)
   - [Statistics & Probability](#statistics--probability)
   - [Regression Analysis](#regression-analysis)
   - [Classification](#classification)
   - [Clustering](#clustering)
   - [Natural Language Processing](#natural-language-processing)
   - [Neural Networks & Deep Learning](#neural-networks--deep-learning)
   - [Time Series Forecasting](#time-series-forecasting)
   - [Recommendation Systems](#recommendation-systems)
3. [Technical Skills](#technical-skills)
4. [How to Run](#how-to-run)
5. [Contact](#contact)

---

## Capstone Projects

### 1. Bankruptcy Prevention System

A production-ready predictive analytics solution designed to identify companies at high risk of financial distress. This project demonstrates the full ML pipeline from data exploration to deployment.

- **Problem:** Financial institutions lose billions annually due to unexpected bankruptcies. Early warning systems are critical for risk management.
- **Solution:** Built a supervised classification model (Polynomial SVM) that predicts bankruptcy probability based on financial health indicators.
- **Deployment:** Interactive Streamlit web application allowing stakeholders to input financial metrics and receive instant risk assessments.
- **Key Techniques:**
  - Feature engineering from raw financial ratios
  - Polynomial kernel SVM for non-linear decision boundaries
  - Model serialization with Pickle
  - End-to-end web deployment
- **Tech Stack:** Python, Scikit-learn, Streamlit, Pandas, NumPy
- **Folder:** `/capstone-bankruptcy-prevention/`

[View Project →](./capstone-bankruptcy-prevention/)

---

### 2. Book Recommendation System

An intelligent recommendation engine that suggests books to users based on collaborative filtering and popularity-based algorithms.

- **Problem:** Online bookstores and libraries need effective ways to suggest relevant books to users to increase engagement and sales.
- **Solution:** Implemented a hybrid recommendation system combining popularity-based filtering (for new users) and collaborative filtering (for returning users).
- **Deployment:** Streamlit web app with two modes: "Top Books" and "Personalized Recommendations".
- **Key Techniques:**
  - Collaborative filtering (user-item similarity)
  - Popularity-based ranking
  - Cosine similarity for nearest-neighbor matching
  - Data pipeline: raw ratings → user-item matrix → similarity computation
- **Tech Stack:** Python, Pandas, Scikit-learn, Streamlit
- **Folder:** `/capstone-book-recommendation/`

[View Project →](./capstone-book-recommendation/)

---

## Assignments by Topic

### Statistics & Probability

| Assignment | Key Concepts |
| :--- | :--- |
| Basic Statistics - Level 1 | Descriptive stats, measures of central tendency, dispersion |
| Basic Statistics - Level 2 | Probability distributions, z-scores, normal distribution |
| Confidence Intervals | Interval estimation, margin of error, t-distribution |
| Hypothesis Testing | t-tests, chi-square, p-values, significance testing |

**Competency Demonstrated:**
- Designing statistical experiments
- Performing hypothesis tests (t-test, chi-square, ANOVA)
- Interpreting p-values and confidence intervals
- Drawing statistically valid conclusions from data

---

### Regression Analysis

| Assignment | Type | Key Techniques |
| :--- | :--- | :--- |
| Simple Linear Regression - Delivery Time | SLR | Correlation, OLS, R-squared, residual analysis |
| Simple Linear Regression - Salary Hike | SLR | Linear relationship modeling, prediction intervals |
| Multiple Linear Regression - 50 Startups | MLR | Multi-collinearity, VIF, dummy variables |
| Multiple Linear Regression - Toyota Corolla | MLR | Feature selection, adjusted R-squared |

**Competency Demonstrated:**
- Building and validating regression models
- Detecting and addressing multi-collinearity (VIF)
- Interpreting coefficients and model diagnostics
- Transformations (log, square root) for non-linear relationships

---

### Classification

| Assignment | Algorithm | Dataset |
| :--- | :--- | :--- |
| Logistic Regression - Claimants | Logistic Regression | Insurance claim prediction |
| Logistic Regression - Bank Full | Logistic Regression | Bank marketing campaign |
| Decision Tree - Fraud Check | Decision Tree | Income-based fraud detection |
| Decision Tree - Company Data | Decision Tree | Sales segment classification |
| Decision Tree - HR Attrition | Decision Tree | Employee attrition prediction |
| SVM - Forest Fires | Support Vector Machine | Forest fire size classification |
| SVM - Salary Data | Support Vector Machine | Income level prediction |
| Naive Bayes - Salary Data | Naive Bayes | Class-conditional probability |
| Naive Bayes - Fraud Check | Naive Bayes | Fraud likelihood estimation |
| KNN - Glass Identification | K-Nearest Neighbors | Glass type classification |
| KNN - Zoo Animal Classification | K-Nearest Neighbors | Animal category prediction |

**Competency Demonstrated:**
- Training and tuning multiple classification algorithms
- Handling class imbalance
- Feature scaling for distance-based algorithms (KNN, SVM)
- Model comparison using accuracy, precision, recall, F1-score
- Cross-validation and hyperparameter tuning

---

### Clustering

| Assignment | Algorithm | Dataset |
| :--- | :--- | :--- |
| K-Means - Airlines | K-Means | Customer segmentation for airlines |
| K-Means - Universities | K-Means | University grouping by statistics |
| DBSCAN - Crime Data | DBSCAN | Crime hotspot identification |
| Hierarchical - East-West Airlines | Hierarchical | Agglomerative clustering |
| Hierarchical - Crime Data | Hierarchical | Dendrogram analysis |

**Competency Demonstrated:**
- Unsupervised pattern discovery
- Determining optimal cluster count (Elbow method, Silhouette score)
- Comparing centroid-based vs. density-based clustering
- Interpreting clusters for business segmentation

---

### Natural Language Processing

| Assignment | Task | Dataset |
| :--- | :--- | :--- |
| Sentiment Analysis | Polarity detection | Amazon/Airline reviews |
| Text Mining - Elon Musk Tweets | Text preprocessing, word clouds | Twitter data |
| NLP - Restaurant Reviews | Sentiment classification | Customer reviews |
| NLP - Spam Detection | Text classification | SMS spam dataset |

**Competency Demonstrated:**
- Text preprocessing (tokenization, stemming, lemmatization, stopword removal)
- Feature extraction (TF-IDF, Bag of Words, Word Embeddings)
- Building sentiment classifiers on unstructured text
- Named Entity Recognition (NER) basics

---

### Neural Networks & Deep Learning

| Assignment | Architecture | Dataset |
| :--- | :--- | :--- |
| Neural Network - Forest Fires | Feedforward Neural Network | Fire damage prediction |
| Neural Network - Concrete Strength | Feedforward Neural Network | Compressive strength prediction |
| Neural Network - Gas Turbines | Feedforward Neural Network | Energy output prediction |
| Neural Network - Alphabets | Feedforward Neural Network | Letter recognition |

**Competency Demonstrated:**
- Designing neural network architectures (input, hidden, output layers)
- Activation functions (ReLU, Sigmoid, Tanh)
- Backpropagation and gradient descent
- Hyperparameter tuning (learning rate, epochs, batch size)
- Model evaluation on regression and classification tasks

---

### Time Series Forecasting

| Assignment | Model | Dataset |
| :--- | :--- | :--- |
| Forecasting - Airlines | ARIMA/SARIMA | Monthly passenger counts |
| Forecasting - Coca-Cola Sales | Exponential Smoothing | Quarterly sales data |
| Forecasting - Plastic Sales | ARIMA | Monthly sales data |

**Competency Demonstrated:**
- Time series decomposition (trend, seasonality, residual)
- Stationarity testing (ADF test)
- ACF/PACF analysis for model selection
- ARIMA, SARIMA, and Exponential Smoothing models
- Forecast evaluation (RMSE, MAPE)

---

### Recommendation Systems

| Assignment | Technique | Dataset |
| :--- | :--- | :--- |
| Association Rules - Book | Apriori Algorithm | Book purchase transactions |
| Association Rules - Movies | Apriori Algorithm | Movie ratings |
| Recommendation System - Entertainment | Collaborative Filtering | User-item ratings |

**Competency Demonstrated:**
- Market basket analysis (support, confidence, lift)
- Association rule mining with Apriori algorithm
- Collaborative filtering (user-based and item-based)
- Handling sparse user-item matrices

---

## Technical Skills

### Programming & Tools
- **Python** (Pandas, NumPy, Scikit-learn, TensorFlow, Keras)
- **Jupyter Notebooks** for exploratory data analysis
- **Streamlit** for interactive web application deployment
- **Git & GitHub** for version control

### Machine Learning
- **Supervised Learning:** Linear/Logistic Regression, Decision Trees, Random Forest, SVM, KNN, Naive Bayes
- **Unsupervised Learning:** K-Means, Hierarchical Clustering, DBSCAN, PCA
- **Deep Learning:** Feedforward Neural Networks, Activation Functions, Backpropagation
- **NLP:** Text Preprocessing, TF-IDF, Sentiment Analysis, Spam Detection
- **Time Series:** ARIMA, SARIMA, Exponential Smoothing, Stationarity Testing
- **Recommendation:** Collaborative Filtering, Association Rules (Apriori)

### Statistics & Mathematics
- Descriptive & Inferential Statistics
- Hypothesis Testing (t-test, chi-square, ANOVA)
- Probability Distributions
- Linear Algebra & Calculus for ML

### Data Processing
- Data Cleaning & Preprocessing
- Feature Engineering & Selection
- Handling Missing Data & Outliers
- Feature Scaling & Normalization

### Model Evaluation
- Cross-validation, Train/Test Split
- Metrics: Accuracy, Precision, Recall, F1-Score, ROC-AUC, RMSE, MAE, R²
- Hyperparameter Tuning (Grid Search, Random Search)

---

## How to Run

### Prerequisites
```bash
pip install -r requirements.txt
```

### Running a Jupyter Notebook
```bash
cd assignments/01-statistics
jupyter notebook hypothesis_testing.ipynb
```

### Running the Streamlit Apps
```bash
# Bankruptcy Prevention
cd capstone-bankruptcy-prevention
streamlit run Bankruptcy_Prevention_app_corrected.py

# Book Recommendation
cd capstone-book-recommendation
streamlit run Book_Recommendation_app_corrected.py
```

---

## Repository Structure

```
.
├── README.md                          # This file
├── requirements.txt                   # Python dependencies
│
├── capstone-bankruptcy-prevention/    # Capstone Project 1
│   ├── README.md
│   ├── Bankruptcy_Prevention_app_corrected.py
│   ├── model_poly.pkl
│   └── data/
│
├── capstone-book-recommendation/      # Capstone Project 2
│   ├── README.md
│   ├── Book_Recommendation_app_corrected.py
│   ├── popular.pkl
│   ├── pt.pkl
│   ├── books.pkl
│   └── similarity.pkl
│
├── 01-statistics/                     # Statistics & Probability
│   ├── basic_statistics_level1.ipynb
│   ├── basic_statistics_level2.ipynb
│   ├── confidence_intervals.ipynb
│   └── hypothesis_testing.ipynb
│
├── 02-regression/                     # Regression Analysis
│   ├── simple_linear_regression/
│   └── multiple_linear_regression/
│
├── 03-classification/                 # Classification Algorithms
│   ├── logistic_regression/
│   ├── decision_tree/
│   ├── svm/
│   ├── naive_bayes/
│   └── knn/
│
├── 04-clustering/                     # Unsupervised Learning
│   ├── kmeans/
│   ├── hierarchical/
│   └── dbscan/
│
├── 05-nlp/                            # Natural Language Processing
│   ├── sentiment_analysis/
│   ├── text_mining/
│   └── spam_detection/
│
├── 06-neural-networks/                # Deep Learning
│   └── feedforward_nn/
│
├── 07-time-series/                    # Time Series Forecasting
│   ├── arima/
│   └── exponential_smoothing/
│
└── 08-recommendation-systems/         # Recommendation Engines
    ├── association_rules/
    └── collaborative_filtering/
```

---

## Contact

I am actively seeking opportunities in Data Science, Machine Learning Engineering, and Analytics. If you have a role that aligns with my skills, or if you would like to discuss any of these projects in detail, please feel free to reach out!

- **LinkedIn:** www.linkedin.com/in/musaddiqahmed99
- **Email:** musaddiqahmed99@gmail.com

---

*This portfolio represents my hands-on learning journey in Data Science. Each project reflects a commitment to writing clean, well-documented code and deriving actionable insights from data.*

