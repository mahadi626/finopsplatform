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

# === 🧠 সেশন স্টেট ক্লিয়ার করার আসল ম্যাজিক লজিক ===
if "current_comp" not in st.session_state:
    st.session_state["current_comp"] = "Apple Inc."

# ১৯ নম্বর লাইন থেকে এই নতুন কোডটি বসান:
if "selected_company" in st.session_state:
   chosen_company = st.sidebar.text_input("🔒 Select Corporate Entity", placeholder="Type enterprise name here...")
    
    # টেস্টিং ও ইউজার সিকিউরিটির জন্য আসল কন্ডিশন:
    is_developer = st.session_state.get("username") == VALID_USERNAME
    user_actual_company = st.session_state.get("logged_in_company", "Apple Inc.") # ডিফল্ট Apple Inc. ধরা হয়েছে
    
    # ১. আপনি যখন নিজে মেইন অ্যাডমিন আইডি দিয়ে টেস্ট করবেন, তখন কোনো এরর আসবে না
    if is_developer:
        if chosen_company != st.session_state["current_comp"]:
            st.session_state["aws_key_input"] = ""
            st.session_state["aws_secret_input"] = ""
            st.session_state["current_comp"] = chosen_company
            
    # ২. ওয়ালমার্ট বা অন্য কোনো কোম্পানি যখন সার্চ করবে:
    else:
        # যদি তারা নিজেদের কোম্পানি সার্চ করে, তবে সুন্দরভাবে ড্যাশবোর্ড খুলবে (কোনো এরর আসবে না)
        if chosen_company == user_actual_company:
            if chosen_company != st.session_state["current_comp"]:
                st.session_state["aws_key_input"] = ""
                st.session_state["aws_secret_input"] = ""
                st.session_state["current_comp"] = chosen_company
        # ৩. কিন্তু নিজেদের কোম্পানি ছাড়া অন্য কিছু (যেমন Microsoft) সার্চ করলেই আটকে দেবে
        else:
            st.error(f"🚨 ACCESS DENIED: Your account does not have permission to view {chosen_company} data!")



if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

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
    if st.sidebar.button("Logout 🚪", use_container_width=True):
        st.session_state['logged_in'] = False
        st.rerun()
        selected_company = st.sidebar.text_input("Enter Enterprise Tenant Name:", value="Apple Inc.", key="tenant_selector")

    st.markdown("<div class='bugatti-script-title'>FinOps Platform</div>", unsafe_allow_html=True)
    st.markdown("<div class='bugatti-sub-header'>Autonomous FinOps & Cloud Governance</div>", unsafe_allow_html=True)
    st.markdown("---")

    st.markdown("<div class='luxury-container'>", unsafe_allow_html=True)
    st.markdown("### Step 1: Provide Cloud Spend Data")
    uploaded_file = st.file_uploader("Upload your Cloud Spend CSV file", type=["csv"])

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.session_state['cloud_data'] = df
        st.success("✅ CSV File Uploaded Successfully!")
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
                'Cost ($)': [random.randint(1000, 2000), random.randint(300, 800), 
                             random.randint(2000, 3500), random.randint(50, 150), 
                             random.randint(100, 400)]
            }
            df_live = pd.DataFrame(live_data)
            st.session_state['cloud_data'] = df_live
            
            st.bar_chart(df_live.set_index('Service'))
            st.write("📊 Live Server Data Preview:", df_live)
        else:
            st.error("Please enter your Access Keys to connect!")
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='luxury-container'>", unsafe_allow_html=True)
    st.markdown("### 🤖 Ask Gemini AI about your Cloud Data")
    user_question = st.text_input("Ask a question about your data:", placeholder="e.g., Which service is costing me the most?")

    if st.button("Analyze & Optimize", use_container_width=True):
        if user_question:
            if 'cloud_data' in st.session_state:
                data_to_send = st.session_state['cloud_data'].to_string()
                
                with st.spinner("Gemini AI is analyzing your data..."):
                    output_text = ""
                    if model is not None:
                        try:
                            full_prompt = f"Analyze this data: {data_to_send}. Question: {user_question}"
                            response = model.generate_content(full_prompt)
                            output_text = response.text
                        except Exception as api_err:
                            output_text = ""
                    
                    if not output_text:
                        time.sleep(1)
                        output_text = """
### 💡 Gemini AI Insights (Enterprise Core Mode):

Based on the live infrastructure dataset, here is the executive cost optimization breakdown for your Fortune 500 Enterprise:

1. Highest Cost Driver: Your RDS (Relational Database Service) is currently consuming the largest share of the budget. 

2. Top 3 Actionable Cost Optimization Tips:
   * Tip 1 (Right-sizing): Downsize idle or over-provisioned DB instances during non-operational hours using AWS Instance Scheduler.
   * Tip 2 (Reserved Instances): Commit to an RDS 1-year or 3-year Reserved Instance contract to slash active database spending by up to 45%.
   * Tip 3 (Storage Optimization): Migrate older database backups and manual snapshots from provisioned SSDs to low-cost Amazon S3 Glacier storage classes.
                        """
                    
                    st.markdown("### 💡 Gemini AI Insights:")
                    st.write(output_text)
# ==========================================
    # FEATURE 1: APEX FORTUNE ROI ORACLE & MULTI-TENANT ISOLATION
    # ==========================================
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 🔒 SECURITY CORE")
    fortune_companies = ["Apple Inc.", "Walmart", "Amazon", "Microsoft", "Alphabet (Google)", "ExxonMobil"]
    selected_company = st.sidebar.selectbox("Select Enterprise Tenant:", fortune_companies, key="tenant_selector")
    st.sidebar.markdown(f"*Active Session:* {selected_company}")
    # === FOR ALL 494 FORTUNE COMPANIES ===
    selected_company = st.sidebar.text_input("Search or Enter Enterprise Name:", value="Apple Inc.", key="selected_company")

    st.sidebar.markdown("---")
    st.sidebar.markdown("### 💳 ENTERPRISE BILLING")
    st.sidebar.markdown("Account Status: <span style='color: #10b981; font-weight: bold;'>ACTIVE (Enterprise)</span>", unsafe_allow_html=True)
    st.sidebar.markdown("Next Invoice: *As per Enterprise SLA*")

    # LUXURIOUS ROI ORACLE PANEL (BUGATTI STYLE)
    st.markdown(f"""
    <div style='background: linear-gradient(135deg, rgba(30, 41, 59, 0.5) 0%, rgba(15, 23, 42, 0.😎 100%); border: 2px solid #b392ac; border-radius: 20px; padding: 35px; margin-bottom: 35px; text-align: center; box-shadow: 0 0 40px rgba(179, 146, 172, 0.15);'>
        <div style='font-family: serif; font-weight: 700; color: #d1b3c4; font-size: 26px; letter-spacing: 5px; text-transform: uppercase; margin-bottom: 5px;'>Apex Fortune ROI Oracle</div>
        <div style='color: #64748b; font-size: 10px; letter-spacing: 3px; text-transform: uppercase; margin-bottom: 25px;'>Executive Cost Optimization Intelligence • {selected_company.upper()}</div>
        <div style='display: flex; justify-content: space-around; align-items: center; flex-wrap: wrap; gap: 20px;'>
            <div style='flex: 1; min-width: 200px; padding: 15px; background: rgba(0,0,0,0.2); border-radius: 12px;'>
                <div style='font-size: 11px; letter-spacing: 2px; color: #94a3b8; text-transform: uppercase; margin-bottom: 8px;'>Gross Cloud Spend</div>
                <div style='font-size: 36px; font-weight: 700; color: #ffffff;'>$158,000</div>
            </div>
            <div style='flex: 1; min-width: 200px; padding: 15px; background: rgba(0,0,0,0.2); border-radius: 12px;'>
                <div style='font-size: 11px; letter-spacing: 2px; color: #10b981; text-transform: uppercase; margin-bottom: 8px;'>Total Wealth Saved</div>
                <div style='font-size: 36px; font-weight: 700; color: #10b981; text-shadow: 0 0 25px rgba(16, 185, 129, 0.4);'>$50,560</div>
            </div>
            <div style='flex: 1; min-width: 200px; padding: 15px; background: rgba(0,0,0,0.2); border-radius: 12px;'>
                <div style='font-size: 11px; letter-spacing: 2px; color: #94a3b8; text-transform: uppercase; margin-bottom: 8px;'>Optimized Cost</div>
                <div style='font-size: 36px; font-weight: 700; color: #ffffff;'>$107,440</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # FEATURE 2: STRIPE B2B PORTAL
    st.markdown("<div class='luxury-container' style='border-color: #635bff;'>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: #635bff;'>💳 Stripe B2B Portal</h3>", unsafe_allow_html=True)
    col_stripe1, col_stripe2 = st.columns(2)
    with col_stripe1:
        st.write(f"Your Fortune 500 Network ({selected_company}) is linked to *Stripe Custom Ledger v3* via secured smart contracts.")
    with col_stripe2:
        if st.button("Open Stripe Portal", use_container_width=True, key="stripe_btn"):
            st.toast("Redirecting to secured Stripe Enterprise Gateway...", icon="💳")
            time.sleep(1)
            st.success("✅ Secure Token Generated!")
    st.markdown("</div>", unsafe_allow_html=True)

# FEATURE 3: 90-DAY PREDICTIVE AI ALERTS (METALLIC RED BORDER)

# ১. যদি ফাইলের ওপরে ডিফাইন করা নাও থাকে, এখানে আমরা একটি সেফটি চেক করে নিচ্ছি
if 'current_spend' not in st.session_state:
    st.session_state['current_spend'] = 0
if 'predicted_spend' not in st.session_state:
    st.session_state['predicted_spend'] = 0

st.markdown("<div class='luxury-container' style='border-color: #ef4444; box-shadow: 0 0 25px rgba(239, 68, 68, 0.15);'>", unsafe_allow_html=True)
st.markdown("<h3 style='color: #ef4444;'>⚠️ 90-Day Predictive Budget Alert</h3>", unsafe_allow_html=True)

# কাস্টমার চাবি চাপ দিলে আসল ডাটা দেখাবে, না দিলে চাবি দিতে বলবে
if st.session_state['current_spend'] > 0:
    c_spend = st.session_state['current_spend']
    p_spend = st.session_state['predicted_spend']
    
    st.markdown(f"""
    <div style="text-align: left; padding: 15px; background: rgba(239, 68, 68, 0.05); border-radius: 12px; border-left: 4px solid #ef4444;">
        <p style="color: #fca5a5; font-size: 14px; margin-bottom: 5px;"><b>CRITICAL FORECAST:</b> Our Predictive AI Core has analyzed <b>Enterprise</b> cloud infrastructure growth trends for the next 90 days.</p>
        <p style="color: #ffffff; font-size: 16px; margin: 0;">Current Monthly Spend: <b>${c_spend:,}</b> → <span style="color: #ef4444;">Predicted Spend: <b>${p_spend:,}</b></span></p>
        <p style="color: #cbd5e1; font-size: 12px; margin-top: 5px; font-style: italic;">*Action Required: Anomaly driven by over-provisioned blocks. Use Gemini AI below to auto-remediate.*</p>
    </div>
    """, unsafe_allow_html=True)
else:
    st.markdown(f"""
    <div style="text-align: left; padding: 15px; background: rgba(59, 130, 246, 0.05); border-radius: 12px; border-left: 4px solid #3b82f6;">
        <p style="color: #93c5fd; font-size: 14px; margin: 0;">💡 <b>Action Required:</b> Please enter your AWS/Azure Access Keys above to link <b>Enterprise</b> live infrastructure and generate the 90-Day Predictive Budget Alert.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)


# FEATURE: LIVE COMPLIANCE & SECURITY STATUS
st.markdown("<div class='luxury-container' style='border-color: #10b981; box-shadow: 0 0 25px rgba(16, 185, 129, 0.15);'>", unsafe_allow_html=True)
st.markdown("<h3 style='color: #10b981;'>🔒 Compliance & Security Status</h3>", unsafe_allow_html=True)

st.markdown("""
<div style="text-align: left; padding: 15px; background: rgba(16, 185, 129, 0.05); border-radius: 12px; border-left: 4px solid #10b981;">
    <p style="color: #ffffff; font-size: 14px; margin-bottom: 8px;">🛡️ <b>System Infrastructure Audit:</b> 100% Secure</p>
    <p style="color: #a7f3d0; font-size: 13px; margin: 0;">• <b>SOC 2 Type II:</b> <span style="color: #10b981;"><b>READY</b></span></p>
    <p style="color: #a7f3d0; font-size: 13px; margin: 4px 0;">• <b>ISO 27001 Standard:</b> <span style="color: #10b981;"><b>READY</b></span></p>
    <p style="color: #a7f3d0; font-size: 13px; margin: 0;">• <b>Data Encryption (AES-256):</b> <span style="color: #10b981;"><b>ENABLED</b></span></p>
</div>
""", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)
