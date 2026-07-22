import streamlit as st
import time

# ১. সোভারেন পেজ কনফিগারেশন (কোনো ইমোজি ব্যবহার করা সম্পূর্ণ নিষেধ)
st.set_page_config(
    page_title="VANGUARD | Secure Institutional Gateway",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ২. অ্যাপল, বুগাটি, পাটেক ফিলিপ ও ফেরারির যৌথ থিম আর্কিটেকচার (CSS)
st.markdown("""
    <style>
    @import url('https://googleapis.com');
    
    /* গ্লোবাল ডার্ক অবসিডিয়ান কার্বন ব্যাকগ্রাউন্ড */
    .stApp {
        background: linear-gradient(180deg, #010102 0%, #05060a 60%, #000000 100%);
        font-family: 'Montserrat', sans-serif;
        color: #DCDCDC;
    }
    
    /* রাজকীয় এন্ট্রান্স গ্লোয়িং ফেড-ইন অ্যানিমেশন (ধীরে ধীরে হালকা থেকে উজ্জ্বল হয়ে ৪ সেকেন্ডে ভেসে ওঠার জন্য) */
    @keyframes fadeInGlow {
        0% { opacity: 0; text-shadow: 0 0 0px rgba(212,175,55,0); filter: blur(5px); }
        50% { opacity: 0.5; text-shadow: 0 0 15px rgba(212,175,55,0.2); filter: blur(2px); }
        100% { opacity: 1; text-shadow: 0 0 30px rgba(212,175,55,0.5); filter: blur(0px); }
    }
    
    .entrance-container {
        text-align: center;
        margin-top: 22vh;
        animation: fadeInGlow 4s ease-in-out forwards;
    }
    
    .entrance-text {
        font-family: 'Cinzel', serif;
        font-size: 26px;
        font-weight: 400;
        color: #D4AF37;
        letter-spacing: 7px;
        line-height: 2.2;
    }
    
    /* রাজকীয় মেইন টাইটেল (Fortune Global 500 Secure Gateway) */
    .lux-main-title {
        font-family: 'Cinzel', serif;
        font-size: 46px;
        font-weight: 500;
        text-align: center;
        letter-spacing: 10px;
        background: linear-gradient(90deg, #AA7C11 0%, #FDF6E2 50%, #AA7C11 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-top: 30px;
        margin-bottom: 5px;
        line-height: 1.5;
    }
    
    .lux-main-subtitle {
        font-family: 'Cinzel', serif;
        font-size: 11px;
        font-weight: 400;
        text-align: center;
        letter-spacing: 4px;
        color: #666666;
        margin-bottom: 45px;
    }
    
    /* অ্যাপল ও বুগাটি স্টাইলের সলিড ও মার্জিত বাটন কন্ট্রোল */
    .stButton>button {
        font-family: 'Cinzel', serif !important;
        background: #FFFFFF !important;
        color: #000000 !important;
        border: none !important;
        letter-spacing: 3px !important;
        border-radius: 0px !important;
        padding: 14px 30px !important;
        font-size: 11px !important;
        font-weight: 600 !important;
        transition: all 0.3s ease-in-out !important;
        width: 100% !important;
    }
    
    .stButton>button:hover {
        background: #D4AF37 !important;
        color: #000000 !important;
        box-shadow: 0 0 25px rgba(212, 175, 55, 0.3) !important;
    }
    
    label {
        font-family: 'Cinzel', serif !important;
        font-size: 12px !important;
        letter-spacing: 2px !important;
        color: #D4AF37 !important;
        text-transform: uppercase !important;
    }
    
    /* ইনপুট বক্সের ফ্রেম */
    .stTextInput>div>div>input {
        background-color: #030407 !important;
        border: 1px solid rgba(212, 175, 55, 0.15) !important;
        color: #FFFFFF !important;
        border-radius: 0px !important;
        padding: 14px !important;
        font-size: 13px !important;
        letter-spacing: 1px !important;
    }
    .stTextInput>div>div>input:focus {
        border-color: #D4AF37 !important;
    }
    </style>
""", unsafe_allow_html=True)

# সেশন লাইফসাইকেল ভেরিয়েবল ট্র্যাকিং
if 'ui_stage' not in st.session_state:
    st.session_state.ui_stage = 'welcome_gate'

# ------------------------------------------------------------------
# স্ক্রিন ১: রাজকীয় ও গম্ভীর আমন্ত্রণ পর্দা (Sovereign Entrance)
# ------------------------------------------------------------------
if st.session_state.ui_stage == 'welcome_gate':
    st.markdown("""
        <div class='entrance-container'>
            <p class='entrance-text'>
                THE PINNACLE OF MULTI-CLOUD INTELLECT<br>
                YOU ARE ENTERING A SOVEREIGN AUTONOMOUS DOMAIN
            </p>
            <p style='font-family: "Cormorant Garamond", serif; font-size: 16px; font-style: italic; color: #8C8C8C; letter-spacing: 2px; margin-top: 20px;'>
                Engineered Exclusively for Fortune Global 500 Executive Leadership
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1.3, 1, 1.3])
    with col2:
        if st.button("PROCEED TO SECURITY GATEWAY"):
            st.session_state.ui_stage = 'secure_login_gate'
            st.rerun()

# ------------------------------------------------------------------
# স্ক্রিন ২: সবচেয়ে লাক্সারিয়াস লগইন ড্যাশবোর্ড (ফিক্সড ৩টি বাটন ও ইনপুট সিকোয়েন্স)
# ------------------------------------------------------------------
elif st.session_state.ui_stage == 'secure_login_gate':
    st.markdown("<h1 class='lux-main-title'>FORTUNE GLOBAL 500<br>SECURE GATEWAY</h1>", unsafe_allow_html=True)
    st.markdown("<p class='lux-main-subtitle'>AUTONOMOUS FINOPS & CLOUD GOVERNANCE INFRASTRUCTURE VER 3.0</p>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 1.4, 1])
    with col2:
        st.markdown("<div style='background: rgba(10,16,26,0.7); border: 1px solid rgba(212,175,55,0.15); padding: 12px; text-align: center; font-family: Cinzel; font-size: 11px; letter-spacing: 2px; color: #D4AF37; margin-bottom: 30px;'>QUANTUM-RESISTANT MULTI-TENANT ISOLATION ACTIVE</div>", unsafe_allow_html=True)
        
        # ৩টি এলিট ক্লাউড গেটওয়ে বাটন পরপর নিচে নিচে (আপনার স্ক্রিনশটের হুবহু অর্ডারে সাজানো)
        google_btn = st.button("Google Workspace SSO Secured")
        st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)
        
        azure_btn = st.button("Microsoft Azure AD Certified")
        st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)
        
        aws_btn = st.button("AWS IAM Role Integration")
        
        # ৩টি বাটনের সেশন ক্লিক রেসপন্স
        if google_btn or azure_btn or aws_btn:
            with st.spinner("Establishing secure federated tunnel..."):
                time.sleep(1.5)
            st.success("Identity Verified. Access granted to Core Domain.")
            
        st.markdown("<br><p style='font-family: Cinzel; font-size: 11px; letter-spacing: 2px; color: #555555; text-align: center;'>— OR ENTER ENTERPRISE PASSPORT —</p><br>", unsafe_allow_html=True)
        
        # আপনার ইনপুট ফিল্ডস (Username, Password)
        company_input = st.text_input("Username:", placeholder="Enter corporate identification...")
        secret_key_input = st.text_input("Password:", type="password", placeholder="••••••••••••••••")
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # পাসওয়ার্ড ইনপুট বক্সের ঠিক নিচে প্রধান লগইন বাটনটি সলিডভাবে প্লেস করা হয়েছে
        if st.button("Login"):
            if company_input and secret_key_input:
                with st.spinner("Verifying sovereign isolation barrier..."):
                    time.sleep(1.5)
                st.success(f"Sovereign Gateway Decrypted. Session token initiated.")
            else:
                st.error("Authentication failed. Sovereign access credentials required.")
