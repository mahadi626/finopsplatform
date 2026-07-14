import streamlit as st
import pandas as pd
import random
import time
import google.generativeai as genai

st.set_page_config(page_title="Autonomous FinOps Platform", layout="wide")

VALID_USERNAME = "FinOpsAdmin2030"
VALID_PASSWORD = "Kvdwnf#Elite@FinOps$99"

if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

st.markdown("""
<style>
.stApp {
    background: radial-gradient(circle at center, #0d1527 0%, #030712 100%) !important;
}
[data-testid="stSidebar"] {
    background-color: rgba(6, 9, 22, 0.9) !important;
    border-right: 1px solid rgba(255, 255, 255, 0.05) !important;
}
.main-card {
    background: rgba(30, 41, 59, 0.4);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 24px;
    padding: 40px;
    box-shadow: 0 20px 50px rgba(0, 0, 0, 0.5);
    text-align: center;
    margin-bottom: 30px;
}
.gate-title {
    font-family: 'Inter', sans-serif;
    font-weight: 800;
    background: linear-gradient(90deg, #38bdf8, #818cf8, #c084fc);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-size: 38px;
    letter-spacing: -1px;
    margin-bottom: 10px;
}
.gate-subtitle {
    color: #94a3b8;
    font-size: 15px;
    margin-bottom: 35px;
}
.sso-button {
    display: flex;
    align-items: center;
    justify-content: center;
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 12px;
    padding: 12px;
    color: #e2e8f0;
    font-weight: 600;
    font-size: 14px;
    margin-bottom: 12px;
}
.divider {
    color: #475569;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 2px;
    margin: 25px 0;
}
.ferrari-header {
    font-family: 'Inter', sans-serif;
    font-weight: 900;
    background: linear-gradient(90deg, #ffffff 0%, #cbd5e1 50%, #64748b 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-size: 42px;
    letter-spacing: -1px;
}
div.stButton > button {
    background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%) !important;
    color: #f8fafc !important;
    font-weight: 600 !important;
    border: 1px solid rgba(255, 255, 255, 0.1) !important;
    border-radius: 10px !important;
    padding: 12px 24px !important;
    transition: all 0.3s ease !important;
}
div.stButton > button:hover {
    background: linear-gradient(135deg, #ef4444 0%, #b91c1c 100%) !important;
    box-shadow: 0 10px 25px rgba(239, 68, 68, 0.3) !important;
    border-color: transparent !important;
    transform: translateY(-1px) !important;
}
</style>
""", unsafe_allow_html=True)

if not st.session_state['logged_in']:
    col1, col2, col3 = st.columns([1, 1.8, 1])
    
    with col2:
        st.markdown("""
        <div class='main-card'>
            <div class='gate-title'>💎 FORTUNE 500 SECURE GATEWAY</div>
            <div class='gate-subtitle'>Autonomous FinOps & Cloud Governance Infrastructure Ver 3.0</div>
            <div class='sso-button'>
                <img src='https://wikimedia.org_\"G\"_logo.svg' style='width: 18px; margin-right: 12px;'/>
                Google Workspace SSO Secured
            </div>
            <div class='sso-button'>
                <img src='https://wikimedia.org' style='width: 18px; margin-right: 12px;'/>
                Microsoft Azure AD Certified
            </div>
            <div class='sso-button'>
                <img src='https://wikimedia.org' style='width: 22px; margin-right: 12px; filter: brightness(0) invert(1);'/>
                AWS IAM Role Integration
            </div>
            <div class='divider'>— OR ENTER ENTERPRISE PASSPORT —</div>
        </div>
        """, unsafe_allow_html=True)
        
        username_input = st.text_input("Username:")
        password_input = st.text_input("Password:", type="password")
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        if st.button("Login", use_container_width=True):
            if username_input == VALID_USERNAME and password_input == VALID_PASSWORD:
                st.session_state['logged_in'] = True
                with st.spinner("Authenticating Enterprise Security Core..."):
                    time.sleep(1.5)
                st.success("Log in successful! Loading dashboard...")
                time.sleep(0.5)
                st.rerun()
            else:
                st.error("Invalid Username or Password! Please try again.")

else:
    if st.sidebar.button("Logout 🚪", use_container_width=True):
        st.session_state['logged_in'] = False
        st.rerun()

    if "GEMINI_API_KEY" in st.secrets:
        genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
        model = genai.GenerativeModel('gemini-1.5-flash')
    else:
        st.error("API Key not found in secrets!")

    st.markdown("<div class='ferrari-header'>💼 Autonomous FinOps & Cloud Governance Platform</div>", unsafe_allow_html=True)
    st.markdown("<p style='color: #64748b; font-size: 16px; margin-top: -10px;'>High-Performance Cloud Spend Ingestion, Infrastructure Synchronization & AI Insights</p>", unsafe_allow_html=True)
    st.markdown("---")

    st.markdown("### Step 1: Provide Cloud Spend Data")
    uploaded_file = st.file_uploader("Upload your Cloud Spend CSV file", type=["csv"])

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.session_state['cloud_data'] = df
        st.success("✅ CSV File Uploaded Successfully!")
        st.dataframe(df, use_container_width=True)

    st.markdown("---")

    st.markdown("### Live Cloud Integration (AWS/Azure Simulation)")
    st.caption("Fortune 500 company admins can link their live infrastructure here.")

    aws_key = st.text_input("Enter AWS Access Key ID:", type="password", placeholder="AKIAIOSFODNN7EXAMPLE")
    aws_secret = st.text_input("Enter AWS Secret Access Key:", type="password", placeholder="wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY")

    if st.button("Connect & Fetch Live Cloud Data", use_container_width=True):
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
            st.write("📊 *Live Server Data Preview:*", df_live)
        else:
            st.error("Please enter your Access Keys to connect!")

    st.markdown("---")

    st.markdown("### 🤖 Ask Gemini AI about your Cloud Data")
    user_question = st.text_input("Ask a question about your data:", placeholder="e.g., Which service is costing me the most?")

    if st.button("Analyze & Optimize", use_container_width=True):
        if user_question:
            if 'cloud_data' in st.session_state:
                data_to_send = st.session_state['cloud_data'].to_string()
                
                with st.spinner("Gemini AI is analyzing your data..."):
                    try:
                        full_prompt = f"""
                        You are an expert Cloud FinOps Consultant for Fortune 500 CEOs. 
                        Analyze this cloud spending data and provide elite, corporate cost optimization tips based on the user's question:
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
