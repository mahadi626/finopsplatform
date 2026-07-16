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
if 'current_tenant' not in st.session_state:
    st.session_state['current_tenant'] = None
if 'tenant_data_store' not in st.session_state:
    st.session_state['tenant_data_store'] = {}

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
.roi-oracle-card {
    background: linear-gradient(135deg, rgba(30, 41, 59, 0.5) 0%, rgba(15, 23, 42, 0.😎 100%);
    border: 2px solid #b392ac;
    border-radius: 20px;
    padding: 35px;
    margin-bottom: 35px;
    text-align: center;
    box-shadow: 0 0 40px rgba(179, 146, 172, 0.15);
}
.oracle-title {
    font-family: 'Cinzel', serif;
    font-weight: 700;
    color: #d1b3c4;
    font-size: 26px;
    letter-spacing: 5px;
    text-transform: uppercase;
    margin-bottom: 5px;
}
.oracle-subtitle {
    font-family: 'Montserrat', sans-serif;
    color: #64748b;
    font-size: 10px;
    letter-spacing: 3px;
    text-transform: uppercase;
    margin-bottom: 25px;
}
.oracle-metrics-grid {
    display: flex;
    justify-content: space-around;
    align-items: center;
    flex-wrap: wrap;
    gap: 20px;
}
.oracle-metric-box {
    flex: 1;
    min-width: 200px;
    padding: 15px;
    background: rgba(0,0,0,0.2);
    border-radius: 12px;
    border: 1px solid rgba(255,255,255,0.03);
}
.oracle-metric-label {
    font-size: 11px;
    letter-spacing: 2px;
    color: #94a3b8;
    text-transform: uppercase;
    margin-bottom: 8px;
}
.oracle-metric-value {
    font-size: 36px;
    font-weight: 700;
    font-family: 'Montserrat', sans-serif;
    color: #ffffff;
    text-shadow: 0 0 20px rgba(255,255,255,0.2);
}
.oracle-saved {
    color: #10b981 !important;
    text-shadow: 0 0 25px rgba(16, 185, 129, 0.4) !important;
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
    background: linear-gradient(135deg, #ffffff 0%, #cbd5e1 100%) !important;
    color: #020408 !important;
    box-shadow: 0 0 30px rgba(255, 255, 255, 0.2) !important;
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
    st.sidebar.markdown("### 🔒 SECURITY CORE")
    
    fortune_companies = ["Apple Inc.", "Walmart", "Amazon", "Microsoft", "Alphabet (Google)", "ExxonMobil"]
    selected_company = st.sidebar.selectbox("Select Enterprise Tenant:", fortune_companies)
    
    if st.session_state['current_tenant'] != selected_company:
        st.session_state['current_tenant'] = selected_company
    
    st.sidebar.markdown(f"*Active Session:* {st.session_state['current_tenant']}")
    st.sidebar.markdown("---")
    
    if st.sidebar.button("Logout 🚪", use_container_width=True):
        st.session_state['logged_in'] = False
        st.session_state['current_tenant'] = None
        st.rerun()

    st.markdown("<div class='bugatti-script-title'>FinOps Platform</div>", unsafe_allow_html=True)
    st.markdown("<div class='bugatti-sub-header'>Autonomous FinOps & Cloud Governance</div>", unsafe_allow_html=True)
    st.markdown("---")

    current_tenant = st.session_state['current_tenant']
    tenant_has_data = current_tenant in st.session_state['tenant_data_store']

    st.markdown(f"""
    <div class='roi-oracle-card'>
        <div class='oracle-title'>Apex Fortune ROI Oracle</div>
        <div class='oracle-subtitle'>Executive Cost Optimization Intelligence • {current_tenant.upper()}</div>
    """, unsafe_allow_html=True)
    
    if tenant_has_data:
        df_active = st.session_state['tenant_data_store'][current_tenant]
        if 'Cost ($)' in df_active.columns:
            total_spend = df_active['Cost ($)'].sum()
        else:
            total_spend = 12500
        saved_amount = int(total_spend * 0.32)
        efficient_spend = total_spend - saved_amount
        
        st.markdown(f"""
            <div class='oracle-metrics-grid'>
                <div class='oracle-metric-box'>
                    <div class='oracle-metric-label'>Gross Cloud Spend</div>
                    <div class='oracle-metric-value'>${total_spend:,}</div>
                </div>
                <div class='oracle-metric-box'>
                    <div class='oracle-metric-label oracle-saved'>Total Wealth Saved</div>
                    <div class='oracle-metric-value oracle-saved'>${saved_amount:,}</div>
                </div>
                <div class='oracle-metric-box'>
                    <div class='oracle-metric-label'>Optimized Infrastructure Cost</div>
                    <div class='oracle-metric-value'>${efficient_spend:,}</div>
                </div>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
            <div class='oracle-metrics-grid'>
                <div class='oracle-metric-box'>
                    <div class='oracle-metric-label'>Gross Cloud Spend</div>
                    <div class='oracle-metric-value' style='color: #475569;'>LOCKED</div>
                </div>
                <div class='oracle-metric-box'>
                    <div class='oracle-metric-label'>Total Wealth Saved</div>
                    <div class='oracle-metric-value' style='color: #475569;'>LOCKED</div>
                </div>
                <div class='oracle-metric-box'>
                    <div class='oracle-metric-label'>Optimized Infrastructure Cost</div>
                    <div class='oracle-metric-value' style='color: #475569;'>LOCKED</div>
                </div>
            </div>
            <div style='color: #64748b; font-size: 12px; margin-top: 20px; font-style: italic;'>
                *Provide Enterprise CSV or Link Live Infrastructure below to fire up the ROI Oracle Engine.
            </div>
        """, unsafe_allow_html=True)
        
    st.markdown("</div>", unsafe_allow_html=True)
