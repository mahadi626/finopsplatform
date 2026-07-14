import streamlit as st
import pandas as pd
import random
import time
import google.generativeai as genai

st.set_page_config(page_title="Autonomous FinOps Platform", layout="wide")

if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    model = genai.GenerativeModel('gemini-1.5-flash')
else:
    st.error("API Key not found in secrets!")

st.title("💼 Autonomous FinOps & Cloud Governance Platform")

st.subheader("📁 Step 1: Provide Cloud Spend Data")

uploaded_file = st.file_uploader("Upload your Cloud Spend CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.session_state['cloud_data'] = df
    st.success("✅ CSV File Uploaded Successfully!")
    st.dataframe(df)

st.markdown("---")

st.subheader("🔗 Live Cloud Integration (AWS/Azure Simulation)")
st.caption("Fortune 500 company admins can link their live infrastructure here.")

aws_key = st.text_input("Enter AWS Access Key ID:", type="password", placeholder="AKIAIOSFODNN7EXAMPLE")
aws_secret = st.text_input("Enter AWS Secret Access Key:", type="password", placeholder="wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY")

if st.button("Connect & Fetch Live Cloud Data"):
    if aws_key and aws_secret:
        with st.spinner("Connecting to AWS Cloud Infrastructure..."):
            time.sleep(2)
            
        st.success("✅ Connected Successfully to AWS Secure Server!")
        
        live_data = {
            'Service': ['EC2', 'S3', 'RDS', 'Lambda', 'CloudWatch'],
            'Cost ($)': [random.randint(1000, 2000), random.randint(300, 800), 
                         random.randint(2000, 3500), random.randint(50, 150), 
                         random.randint(100, 400)]
        }
        df_live = pd.DataFrame(live_data)
        st.session_state['cloud_data'] = df_live
        
        st.bar_chart(df_live.set_index('Service'))
        st.write("Live Server Data Preview:", df_live)
    else:
        st.error("Please enter your Access Keys to connect!")

st.markdown("---")

st.subheader("🤖 Ask Gemini AI about your Cloud Data")
user_question = st.text_input("Ask a question about your data:", placeholder="e.g., Which service is costing me the most?")

if st.button("Analyze & Optimize"):
    if user_question:
        if 'cloud_data' in st.session_state:
            data_to_send = st.session_state['cloud_data'].to_string()
            
            with st.spinner("Gemini AI is analyzing your data..."):
                try:
                    full_prompt = f"""
                    You are an expert Cloud FinOps Consultant. 
                    Analyze this cloud spending data and provide cost optimization tips based on the user's question:
                    {data_to_send}
                    
                    User Question: {user_question}
                    """
                    response = model.generate_content(full_prompt)
                    st.markdown("### 💡 Gemini AI Insights:")
                    st.write(response.text)
                except Exception as e:
                    st.error(f"Error calling Gemini API: {e}")
        else:
            st.error("Please upload a CSV file or connect to Live Cloud first to generate data!")
    else:
        st.warning("Please enter a question first!")
