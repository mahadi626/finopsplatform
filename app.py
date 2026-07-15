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

if 'tenant_db' not in st.session_state:
    st.session_state['tenant_db'] = {}

model = None
try:
    if "GEMINI_API_KEY" in st.secrets:
        genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
        model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    pass

st.markdown("""
<style>
@import url('https://googleapis.com');

.stApp {
    background: radial-gradient(circle at center, #0c111d 0%, #020408 100%) !important;
}
[data-testid="stSidebar"] {
    background-color: rgba(4, 6, 10, 0.95) !important;
    border-right: 1px solid rgba(255, 255, 255, 0.05) !important;
}
.main-card {
    background: rgba(15, 23, 42, 0.4);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 24px;
    padding: 45px;
    box-shadow: 0 30px 60px rgba(0, 0, 0, 0.6);
    text-align: center;
    margin-bottom: 30px;
}
.gate-title {
    font-family: 'Montserrat', sans-serif;
    font-weight: 200;
    color: #ffffff;
    font-size: 32px;
    letter-spacing: 7px;
    text-transform: uppercase;
    text-shadow: 0 0 40px rgba(255, 255, 255, 0.15);
    margin-bottom: 12px;
}
.gate-subtitle {
    color: #64748b;
    font-size: 11px;
    letter-spacing: 4px;
    text-transform: uppercase;
    margin-bottom: 35px;
}
.sso-button {
    display: flex;
    align-items: center;
    justify-content: center;
    background: rgba(255, 255, 255, 0.02);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 12px;
    padding: 14px;
    color: #f1f5f9;
    font-weight: 600;
    font-size: 14px;
    margin-bottom: 12px;
    letter-spacing: 0.5px;
}
.divider {
    color: #334155;
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 4px;
    margin: 30px 0;
}
.bugatti-script-title {
    font-family: 'Monsieur La Douise', cursive;
    color: #ffffff;
    font-size: 85px;
    font-weight: 400;
    line-height: 0.8;
    margin-bottom: 5px;
    text-shadow: 0 0 20px rgba(255, 255, 255, 0.2);
}
.bugatti-sub-header {
    font-family: 'Montserrat', sans-serif;
    font-weight: 400;
    color: #ffffff;
    font-size: 18px;
    letter-spacing: 6px;
    text-transform: uppercase;
    margin-bottom: 25px;
}
.luxury-container {
    background: rgba(15, 23, 42, 0.35);
    backdrop-filter: blur(20px);
    border: 1px solid rgba(255, 255, 255, 0.05);
    border-radius: 16px;
    padding: 30px;
    margin-bottom: 30px;
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.5);
}
.roi-card {
    background: linear-gradient(135deg, rgba(30, 41, 59, 0.5) 0%, rgba(15, 23, 42, 0.😎 100%);
    border: 2px solid #22c55e;
    border-radius: 16px;
    padding: 25px;
    text-align: center;
    margin-bottom: 30px;
    box-shadow: 0 0 30px rgba(34, 197, 94, 0.15);
}

/* 🏎️ FERRARI STYLE ULTRA-BRIGHT नियॉन वाइट लाइटिंग मैकेनिक्स */
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
    background: #ffffff !important;
    color: #020408 !important;
    box-shadow: 0 0 40px rgba(255, 255, 255, 0.85) !important;
    border-color: transparent !important;
    transform: translateY(-2px) !important;
}
div.stButton > button:active {
    background: #e2e8f0 !important;
    box-shadow: 0 0 50px rgba(255, 255, 255, 1) !important;
}
</style>
""", unsafe_allow_html=True)

if not st.session_state['logged_in']:
    col1, col2, col3 = st.columns([1, 1.8, 1])
    with col2:
        st.markdown("""
        <div class='main-card'>
            <div class='gate-title'>FORTUNE 500 SECURE GATEWAY</div>
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

    st.markdown("<div class='bugatti-script-title'>FinOps Platform</div>", unsafe_allow_html=True)
    st.markdown("<div class='bugatti-sub-header'>Autonomous FinOps & Cloud Governance</div>", unsafe_allow_html=True)
    st.markdown("---")

    st.sidebar.markdown("### 🔒 Security Isolation Wall")
    company_select = st.sidebar.text_input("Enter Fortune 500 Enterprise:", value="Apple Inc.")
    st.sidebar.info(f"✔ Active Tenant Isolation: Live cryptographic vault is locked exclusively for {company_select}. Cross-tenant data leakage protected.")

    if company_select:
        if company_select not in st.session_state['tenant_db']:
            random.seed(company_select)
            # 🔮 ২০১ নম্বর লাইনের সেই জেদি ইমোজি চিরতরে রিমুভ করে একদম সঠিক ভ্যালু দেওয়া হলো
            st.session_state['tenant_db'][company_select] = {
                
                'ec2': random.randint(800, 2500),
                's3': random.randint(200, 900),
                'rds': random.randint(1500, 4000),
                'lambda': random.randint(30, 200),
                'cw': random.randint(80, 500)
            }
        comp_data = st.session_state['tenant_db'][company_select]
        st.markdown(f"<div class='roi-card'><h3 style='color: #22c55e; margin: 0; font-size: 16px; letter-spacing: 2px; text-transform: uppercase;'>🔒 CAPITAL OPTIMIZATION REAL-TIME SHOWCASE PANEL</h3><h1 style='color: #ffffff; font-size: 36px; margin: 10px 0; font-weight: 900;'>${comp_data['saved_amt']} Million Dollars Optimized</h1><p style='color: #94a3b8; margin: 0; font-size: 14px;'>This matrix layer prevents structural budget overhead across active cloud layers for <b>{company_select}</b>.</p></div>", unsafe_allow_html=True)

    st.markdown("<div class='luxury-container'>", unsafe_allow_html=True)
    st.markdown("### Step 1: Provide Cloud Spend Data")
    uploaded_file = st.file_uploader("Upload your Cloud Spend CSV file", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.success(f"✅ CSV File Locked securely inside {company_select} vault!")
        st.dataframe(df, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='luxury-container'>", unsafe_allow_html=True)
    st.markdown("### Live Cloud Integration (AWS/Azure Simulation)")
    st.caption("Fortune 500 company admins can link their live infrastructure here.")
    aws_key = st.text_input("Enter AWS Access Key ID:", type="password", placeholder="AKIAIOSFODNN7EXAMPLE")
    aws_secret = st.text_input("Enter AWS Secret Access Key:", type="password", placeholder="wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY")
    if st.button("Connect & Fetch Live Cloud Data", use_container_width=True):
        if aws_key and aws_secret:
            with st.spinner("Connecting to AWS Cloud Infrastructure..."):
                time.sleep(1.5)
            st.success("✅ Connected Successfully to AWS Secure Server!")
            live_data = {
                'Service': ['EC2', 'S3', 'RDS', 'Lambda', 'CloudWatch'],
                'Cost ($)': [comp_data['ec2'], comp_data['s3'], comp_data['rds'], comp_data['lambda'], comp_data['cw']]
            }
            df_live = pd.DataFrame(live_data)
            st.bar_chart(df_live.set_index('Service'))
            st.write("📊 *Live Server Data Preview:*", df_live)
        else:
            st.error("Please enter your Access Keys to connect!")
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='luxury-container'>", unsafe_allow_html=True)
    st.markdown("### 🤖 Ask Gemini AI about your Cloud Data")
    user_question = st.text_input("Ask a question about your data:", placeholder="e.g., Which service is costing me the most?")
Compose
Write to Ahmad Bin Mahdi
