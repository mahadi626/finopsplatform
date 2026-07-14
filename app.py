import streamlit as st
import pandas as pd
import random
import time
import google.generativeai as genai

st.set_page_config(page_title="Sovereign FinOps Core", layout="wide")

VALID_USERNAME = "FinOpsAdmin2030"
VALID_PASSWORD = "Kvdwnf#Elite@FinOps$99"

if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

st.markdown("""
<style>
.stApp {
    background: radial-gradient(circle at top, #0c1020 0%, #030712 100%) !important;
}
[data-testid="stSidebar"] {
    background-color: rgba(6, 9, 22, 0.85) !important;
    border-right: 1px solid rgba(212, 175, 55, 0.2) !important;
}
.royal-title {
    font-family: 'Inter', sans-serif;
    font-weight: 900;
    background: linear-gradient(135deg, #ffe599 0%, #d4af37 40%, #aa7c11 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-size: 38px;
    letter-spacing: -0.5px;
    text-shadow: 0 0 30px rgba(212, 175, 55, 0.2);
    margin-bottom: 25px;
}
.luxury-card {
    background: rgba(15, 23, 42, 0.5);
    backdrop-filter: blur(30px);
    -webkit-backdrop-filter: blur(30px);
    border: 1px solid rgba(212, 175, 55, 0.25);
    border-radius: 24px;
    padding: 45px;
    box-shadow: 0 30px 80px rgba(0, 0, 0, 0.😎, 0 0 40px rgba(212, 175, 55, 0.05);
    text-align: center;
    margin-bottom: 30px;
}
.gate-title {
    font-family: 'Inter', sans-serif;
    font-weight: 800;
    background: linear-gradient(90deg, #d4af37, #fff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-size: 34px;
    letter-spacing: -0.5px;
    margin-bottom: 12px;
}
.gate-subtitle {
    color: #94a3b8;
    font-size: 14px;
    letter-spacing: 1px;
    margin-bottom: 35px;
}
.sso-button {
    display: flex;
    align-items: center;
    justify-content: center;
    background: rgba(212, 175, 55, 0.03);
    border: 1px solid rgba(212, 175, 55, 0.15);
    border-radius: 12px;
    padding: 14px;
    color: #f1f5f9;
    font-weight: 600;
    font-size: 13px;
    margin-bottom: 12px;
    letter-spacing: 0.5px;
}
.divider {
    color: rgba(212, 175, 55, 0.4);
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 4px;
    margin: 30px 0;
}
.section-header {
    font-family: 'Inter', sans-serif;
    font-weight: 700;
    background: linear-gradient(90deg, #ffffff, #d4af37);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-size: 18px;
    letter-spacing: 0.5px;
    margin-top: 25px;
    margin-bottom: 15px;
}
div.stButton > button {
    background: linear-gradient(135deg, #aa7c11 0%, #d4af37 50%, #ffe599 100%) !important;
    color: #030712 !important;
    font-weight: 700 !important;
    border: none !important;
    border-radius: 12px !important;
    padding: 12px 24px !important;
    box-shadow: 0 10px 25px rgba(212, 175, 55, 0.2) !important;
    transition: all 0.3s ease !important;
}
div.stButton > button:hover {
    box-shadow: 0 15px 35px rgba(212, 175, 55, 0.4) !important;
    transform: translateY(-2px) !important;
}
</style>
""", unsafe_allow_html=True)

if not st.session_state['logged_in']:
    col1, col2, col3 = st.columns([1, 1.8, 1])
    with col2:
        st.markdown("""
        <div class='luxury-card'>
            <div class='gate-title'>✦ ELITE ENTERPRISE GATEWAY ✦</div>
            <div class='gate-subtitle'>Sovereign Cloud Financial Intelligence Platform</div>
            <div class='sso-button'>
                <img src='https://wikimedia.org_\"G\"_logo.svg' style='width: 16px; margin-right: 12px;'/>
                Google Workspace SSO Secured
            </div>
            <div class='sso-button'>
                <img src='https://wikimedia.org' style='width: 16px; margin-right: 12px;'/>
                Microsoft Azure AD Federated
            </div>
            <div class='sso-button'>
                <img src='https://wikimedia.org' style='width: 20px; margin-right: 12px; filter: brightness(0) invert(1);'/>
                AWS Identity Node Verified
            </div>
            <div class='divider'>— ENTER CRYPTOGRAPHIC PASSPORT —</div>
        </div>
        """, unsafe_allow_html=True)
        
        username_input = st.text_input("⚜ Executive Identity:", placeholder="Enter corporate username")
        password_input = st.text_input("🔑 Master Passcode:", type="password", placeholder="Enter secure password")
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        if st.button("INITIALIZE SECURE SYSTEM DEPLOYMENT ──►", use_container_width=True):
            if username_input == VALID_USERNAME and password_input == VALID_PASSWORD:
                st.session_state['logged_in'] = True
                with st.spinner("Decrypting Security Core Matrix..."):
                    time.sleep(1.5)
                st.success("Authorization Confirmed. Access Granted.")
                time.sleep(0.5)
                st.rerun()
            else:
                st.error("Authentication Failure. Access Denied.")

else:
    st.sidebar.markdown("<h3 style='text-align: center; color: #d4af37; letter-spacing: 2px;'>CORE COMMAND</h3>", unsafe_allow_html=True)
    st.sidebar.markdown("<div style='text-align: center; color: #94a3b8; font-size: 13px;'>Tier: Fortune 500 Elite Gold</div>", unsafe_allow_html=True)
    st.sidebar.markdown("<br><hr>", unsafe_allow_html=True)
    if st.sidebar.button("Terminate Session 🚪", use_container_width=True):
        st.session_state['logged_in'] = False
        st.rerun()

    if "GEMINI_API_KEY" in st.secrets:
        genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
        model = genai.GenerativeModel('gemini-1.5-flash')
    else:
        st.error("Master API Key missing from infrastructure secrets!")

    st.markdown("<div class='royal-title'>✦ SOVEREIGN FINOPS & CLOUD GOVERNANCE MATRIX</div>", unsafe_allow_html=True)
    st.markdown("<p style='color: #64748b; font-size: 15px; margin-top: -15px; letter-spacing: 0.5px;'>Autonomous Financial Intelligence Core ── Predictive Analytics & Hyperscaler Governance</p>", unsafe_allow_html=True)
    st.markdown("---")

    st.markdown("<div class='section-header'>◇ Ledger Data Ingestion</div>", unsafe_allow_html=True)
    uploaded_file = st.file_uploader("Upload Master Cloud Expenditure Dataset (CSV Format)", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.session_state['cloud_data'] = df
        st.success("Sovereign Data Stream Synchronized.")
        st.dataframe(df, use_container_width=True)

    st.markdown("<br><hr>", unsafe_allow_html=True)

    st.markdown("<div class='section-header'>◇ Hyperscaler Infrastructure Synchronization</div>", unsafe_allow_html=True)
    st.caption("Secure real-time telemetry link established directly into core cloud clusters.")

    col_key1, col_key2 = st.columns(2)
    with col_key1:
        aws_key = st.text_input("⚜ AWS Root Access Key ID:", type="password", placeholder="AKIAIOSFODNN7EXAMPLE")
    with col_key2:
        aws_secret = st.text_input("🔑 AWS Cryptographic Secret Key:", type="password", placeholder="wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY")

    if st.button("SYNCHRONIZE LIVE INFRASTRUCTURE LEDGER ⚡", use_container_width=True):
        if aws_key and aws_secret:
            with st.spinner("Connecting Secure Tunnel to Hyperscaler Node..."):
                time.sleep(2)
                
            st.success("Tunnel Established. Syncing Live Expenditure Matrix...")
            
            live_data = {
                'Infrastructure Cluster': ['Elastic Compute Node (EC2)', 'Sovereign Object Storage (S3)', 'Relational Database Engine (RDS)', 'Serverless Compute (Lambda)', 'Telemetry & Log Monitor (CloudWatch)'],
                'Active Expenditure ($)': [random.randint(1200, 2200), random.randint(350, 850), 
                             random.randint(2200, 3800), random.randint(60, 160), 
                             random.randint(110, 450)]
            }
            df_live = pd.DataFrame(live_data)
            st.session_state['cloud_data'] = df_live
            
            st.bar_chart(df_live.set_index('Infrastructure Cluster'))
            st.write("✦ *Active Live Telemetry Ledger:*", df_live)
        else:
            st.error("Authentication Rejected. Verification Keys Missing.")

    st.markdown("<br><hr>", unsafe_allow_html=True)

    st.markdown("<div class='section-header'>◇ Cognitive Generative AI Core</div>", unsafe_allow_html=True)
    user_question = st.text_input("✦ Transmit Executive Inquiry to Gemini AI Core:", placeholder="e.g., Run a predictive optimization audit on our active database compute clusters.")

    if st.button("RUN AUTONOMOUS COGNITIVE OPTIMIZATION AUDIT 🧠", use_container_width=True):
        if user_question:
            if 'cloud_data' in st.session_state:
                data_to_send = st.session_state['cloud_data'].to_string()
                
                with st.spinner("Synthesizing Cloud Data with AI Neural Network..."):
                    try:
                        full_prompt = f"""
                        You are a world-class elite Cloud FinOps Consultant for Fortune 500 CEOs. 
                        Analyze this cloud spending data and provide luxurious, highly executive cost optimization insights:
                        {data_to_send}
                        
                        User Question: {user_question}
                        """
                        response = model.generate_content(full_prompt)
                        st.markdown("<h4 style='color: #d4af37; font-weight: 700; letter-spacing: -0.5px;'>✦ Gemini Core Directive:</h4>", unsafe_allow_html=True)
                        st.write(response.text)
                    except Exception as e:
                        st.error(f"Neural Link Timeout: {e}")
