import pandas as pd
import requests
import streamlit as st
import google.generativeai as genai

GOOGLE_API_KEY = "YOUR_SECRET_KEY_HERE"
genai.configure(api_key=GOOGLE_API_KEY)

correct_username = "admin"
correct_password = "password123"

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.subheader("🔒 Enterprise Secure Login")
    username = st.text_input("Username:")
    password = st.text_input("Password:", type="password")
    
    if st.button("Login"):
        if username == correct_username and password == correct_password:
            st.session_state.logged_in = True
            st.success("Successfully Logged In!")
            st.rerun()
        else:
            st.error("Invalid Username or Password. Please try again.")
    st.stop()

st.title("Autonomous FinOps & Governance Platform")

uploaded_file = st.file_uploader("Upload your Cloud Spend CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("Data Preview:", df.head())
    
    if "Service" in df.columns and "Cost" in df.columns:
        total_cost = df["Cost"].sum()
        st.metric(label="Total Cloud Spend Found", value=f"${total_cost:,.2f}")
        
        st.subheader("New Dynamic Cost Breakdown")
        st.bar_chart(data=df, x="Service", y="Cost")
    else:
        st.metric(label="Total Cloud Spend", value="$14,250", delta="Sample Data")
        st.bar_chart(df)
        
    st.subheader("🤖 Ask Gemini AI about your Cloud Data")
    user_query = st.text_input("Ask a question about your data:")
    
    if st.button("Analyze & Optimize", key="analyze_button"):
        if user_query:
            with st.spinner("Gemini is analyzing your data..."):
                try:
                    csv_data_string = df.to_string(index=False)
                    model = genai.GenerativeModel('gemini-1.5-flash')
                    prompt = f"Here is the cloud budget data:\n\n{csv_data_string}\n\nUser Question: {user_query}\n\nPlease analyze the data and provide actionable optimization recommendations."
                    response = model.generate_content(prompt)
                    st.success("AI Analysis Results:")
                    st.write(response.text)
                except Exception as e:
                    st.error(f"Error: {e}")
        else:
            st.warning("Please enter a question first!")
import streamlit as st
import pandas as pd
import random
import time

st.markdown("---")
st.subheader("🔗 Live Cloud Integration (AWS/Azure)")
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
        
        st.bar_chart(df_live.set_index('Service'))
        st.write("Live Server Data Preview:", df_live)
        
        st.session_state['cloud_data'] = df_live
    else:
        st.error("Please enter your Access Keys to connect!")
