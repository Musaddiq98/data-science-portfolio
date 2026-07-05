# Book Recommendation System

A recommendation-system project that suggests books to users based on interaction data. The project demonstrates collaborative filtering, popularity-based recommendations, and a user-facing Streamlit application.

## Project Overview

This project turns user-book ratings into recommendation outputs that can help readers discover relevant books.

## Business Problem

Book platforms need personalized recommendations to improve discovery and engagement. A recommendation engine can help users find relevant books faster while increasing interaction with the catalog.

## Recommendation Approach

- Cleaned and processed book, user, and ratings data
- Built popularity-based recommendations for broad discovery
- Used collaborative filtering to recommend books from similar user behavior
- Served recommendations through a Streamlit interface

## Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Pickle

## How to Run

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Interview Highlights

- Explained recommendation logic from raw ratings to ranked outputs
- Addressed the cold-start problem with popularity-based recommendations
- Built a simple interactive app for non-technical users
- Organized the project around a practical product use case
