import streamlit as st
import pickle
import pandas as pd

# --------------------------------------------------
# Page config
# --------------------------------------------------
st.set_page_config(
    page_title="Book Recommendation System",
    page_icon="📚",
    layout="centered"
)

# --------------------------------------------------
# Load artifacts
# --------------------------------------------------
@st.cache_resource
def load_artifacts():
    books = pickle.load(open("books.pkl", "rb"))
    cf_preds_df = pickle.load(open("cf_preds_df.pkl", "rb"))
    interactions_train = pickle.load(open("interactions_train_indexed_df.pkl", "rb"))
    return books, cf_preds_df, interactions_train


books, cf_preds_df, interactions_train = load_artifacts()

# --------------------------------------------------
# UI Header
# --------------------------------------------------
st.markdown(
    """
    <div style="background-color:#2a9d8f;padding:15px;border-radius:10px">
        <h2 style="color:white;text-align:center;">📚 Book Recommendation System</h2>
        <p style="color:white;text-align:center;">
            User-based Collaborative Filtering
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

st.sidebar.header("📌 About")
st.sidebar.write(
    """
    This app recommends books using **User-User Collaborative Filtering**.
    Recommendations are generated from historical user-book interactions.
    """
)

# --------------------------------------------------
# Recommender logic
# --------------------------------------------------
class CFRecommender:
    def __init__(self, predictions_df, books_df):
        self.predictions_df = predictions_df
        self.books_df = books_df

    def recommend(self, user_id, interacted_items, top_n=10):
        if user_id not in self.predictions_df.columns:
            return pd.DataFrame()

        user_preds = (
            self.predictions_df[user_id]
            .sort_values(ascending=False)
            .reset_index()
            .rename(columns={user_id: "score"})
        )

        recommendations = user_preds[
            ~user_preds["ISBN"].isin(interacted_items)
        ].head(top_n)

        recommendations = recommendations.merge(
            self.books_df, on="ISBN", how="left"
        )

        return recommendations[
            ["Book-Title", "Book-Author", "Year-Of-Publication"]
        ]


def get_user_interactions(user_id):
    if user_id not in interactions_train.index:
        return set()

    items = interactions_train.loc[user_id]["ISBN"]
    return set(items if isinstance(items, pd.Series) else [items])


# --------------------------------------------------
# User input
# --------------------------------------------------
st.subheader("👤 Select User")

user_ids = interactions_train.index.unique().tolist()
user_id = st.selectbox("Choose User ID", user_ids)

top_n = st.slider("Number of recommendations", 5, 20, 10)

if st.button("📖 Recommend Books"):
    st.write("✅ Button clicked")
    st.write("User ID:", user_id)

    recommender = CFRecommender(cf_preds_df, books)
    interacted_items = get_user_interactions(user_id)
    recommendations = recommender.recommend(user_id, interacted_items, top_n)

    st.success("Here are your personalized recommendations:")
    st.dataframe(recommendations, use_container_width=True)

