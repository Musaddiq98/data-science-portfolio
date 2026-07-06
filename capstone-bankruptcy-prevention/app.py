
import pickle
import streamlit as st
import numpy as np

st.set_page_config(
    page_title="Bankruptcy Prevention System",
    page_icon="📊",
    layout="centered"
)

@st.cache_resource
def load_model():
    with open("model_poly.pkl", "rb") as file:
        model = pickle.load(file)
    return model

model = load_model()

st.markdown(
    '''
    <div style="background-color:#6a4c93;padding:15px;border-radius:10px">
        <h2 style="color:white;text-align:center;">
            Bankruptcy Prevention System
        </h2>
        <p style="color:white;text-align:center;">
            Predict company bankruptcy risk using Machine Learning
        </p>
    </div>
    ''',
    unsafe_allow_html=True
)

st.sidebar.header("📌 About")
st.sidebar.write(
    '''
    This app predicts whether a company is at risk of bankruptcy
    based on six financial and operational risk factors.
    '''
)

risk_levels = {
    "Low (0)": 0,
    "Medium (0.5)": 0.5,
    "High (1)": 1
}

st.subheader("🔢 Select Risk Factors")

industrial_risk = st.selectbox("Industrial Risk", risk_levels.keys())
management_risk = st.selectbox("Management Risk", risk_levels.keys())
financial_flexibility = st.selectbox("Financial Flexibility", risk_levels.keys())
credibility = st.selectbox("Credibility", risk_levels.keys())
competitiveness = st.selectbox("Competitiveness", risk_levels.keys())
operating_risk = st.selectbox("Operating Risk", risk_levels.keys())

features = np.array([[
    risk_levels[industrial_risk],
    risk_levels[management_risk],
    risk_levels[financial_flexibility],
    risk_levels[credibility],
    risk_levels[competitiveness],
    risk_levels[operating_risk]
]])

if st.button("🔍 Predict"):
    prediction = model.predict(features)[0]
    if prediction == 0:
        st.error("⚠️ High Risk: The company is likely to go bankrupt.")
    else:
        st.success("✅ Low Risk: The company is financially stable.")

with st.expander("📘 Model Explanation"):
    st.write(
        '''
        The model evaluates six business risk indicators.
        Each indicator is categorized as Low, Medium, or High.
        Based on historical data, the model predicts bankruptcy risk.
        '''
    )
