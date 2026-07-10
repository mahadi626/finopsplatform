import streamlit as st
import requests
import pandas as pd
st.title("Autonomous FinOps & Governance Platform")
user_query = st.text_input("Ask anything about cloud cost optimization:", "Give me one quick cloud cost saving tip.")
uploaded_file = st.file_uploader("Upload your cloud bill(csv file):", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, sep=",")
    st.subheader("Cloud Spend Analytics Dashboard")
    st.metric(label="Total Cloud Spend",value="$14,250", delta="+40%")
    st.bar_chart(df)
    user_query += "\nBill data: " + uploaded_file.getvalue().decode("utf-8")[:1000]
if st.button("Analyze & Optimize"):
    url = "http://localhost:11434/api/generate"
    data = {"model": "llama3", "prompt": user_query, "stream": False}
    st.info("FinOps AI Engine is analyzing... Please wait...")
    response = requests.post(url, json=data).json().get("response")
    st.success ("=== FinOps AI Recommendation ===")
    st.write (response)

