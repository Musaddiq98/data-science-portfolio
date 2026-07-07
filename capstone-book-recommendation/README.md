# Book Recommendation System

A user-based collaborative filtering engine that recommends books based on the reading patterns of similar users — deployed as a Streamlit web app.

---

## The Problem

Book platforms have enormous catalogues. Without good recommendations, users either miss books they'd enjoy or spend too long searching. This project builds a system that learns from rating patterns to surface relevant books for each user automatically.

---

## Dataset

The **Book-Crossing dataset** — one of the most widely used public datasets for recommendation research:
- ~278,000 users
- ~271,000 unique books (by ISBN)
- ~1.1 million ratings on a 1–10 scale

The raw data is very sparse, so the first step is filtering it down to users and books with enough interactions to make similarity calculations reliable.

---

## What I Built

**Notebook (`Book recommendation system user-user.ipynb`):**
- Loaded the Books, Users, and Ratings CSVs and merged them
- Filtered to users with ≥200 ratings and books with ≥50 ratings to reduce sparsity
- Built a user–book pivot matrix (rows = users, columns = books, values = ratings)
- Computed cosine similarity between users to identify nearest neighbours
- For a target user, aggregated neighbour ratings, removed already-read books, ranked the rest
- Validated recommendations with manual inspection across multiple test users

**Streamlit App (`app.py`):**
- Enter a User ID to get personalised book recommendations
- Displays book titles ranked by predicted rating
- Fast inference using the precomputed similarity matrix

---

## Run Locally

```bash
pip install pandas numpy scikit-learn streamlit
streamlit run app.py
```
