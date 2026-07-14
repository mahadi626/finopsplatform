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

if not st.session_state['logged_in']:
    st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 50%, #020617 100%) !important;
    }
    .main-card {
        background: rgba(30, 41, 59, 0.4);
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 24px;
        padding: 40px;
        box-shadow: 0 20px 50px rgba(0, 0, 0, 0.5), inset 0 1px 0 rgba(255, 255, 255, 0.1);
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
    </style>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 1.8, 1])
    
    with col2:
        st.markdown("""
        <div class='main-card'>
            <div class='gate-title'>🔑 FORTUNE 500 SECURE GATEWAY</div>
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
        
        username_input = st.text_input("💎 Corporate Username:", placeholder="Enter corporate username")
        password_input = st.text_input("🔒 Cryptographic Password:", type="password", placeholder="Enter secure password")
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        if st.button("🚀 INITIALIZE QUANTUM DEPLOYMENT", use_container_width=True):
            if username_input == VALID_USERNAME and password_input == VALID_PASSWORD:
                st.session_state['logged_in'] = True
                with st.spinner("Decrypting Security Core & Syncing Infrastructure..."):
                    time.sleep(2)
                st.success("Access Granted! Opening Dashboard...")
                time.sleep(0.5)
                st.rerun()
            else:
                st.error("Authentication Failure! Invalid Credentials.")

else:
    if st.sidebar.button("Logout From Core 🚪"):
        st.session_state['logged_in'] = False
        st.rerun()

    if "GEMINI_API_KEY" in st.secrets:
        genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
        model = genai.GenerativeModel('gemini-1.5-flash')
    else:
        st.error("API Key not found in secrets! Please check your secrets.toml file.")

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

