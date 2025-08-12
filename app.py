# app.py — Trovule (Sunny Postcard redesign with permanent video bg + confetti)
from pathlib import Path
from datetime import datetime
import base64

import streamlit as st
import streamlit.components.v1 as components
from dotenv import load_dotenv

from services.shecodes_client import current_weather, generate_itinerary, APIError

# ---------- Setup ----------
load_dotenv()
ASSETS = Path(__file__).parent / "assets"

st.set_page_config(
    page_title="Trovule — Your Blissful Trip Buddy",
    page_icon=str(ASSETS / "icon.png"),
    layout="centered",
)

# ---------- Helpers ----------
def b64(path: Path) -> str:
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

def confetti():
    # fire canvas-confetti once; height=0 to avoid extra space
    components.html(
        """
        <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>
        <script>
          // A small burst, sunny palette
          const colors = ['#FFC857','#F25F5C','#70C1B3','#FFE066','#247BA0'];
          confetti({
            particleCount: 160,
            spread: 70,
            origin: { y: 0.2 },
            colors
          });
          // A second gentle burst
          setTimeout(() => confetti({
            particleCount: 120,
            spread: 100,
            origin: { y: 0.2 },
            colors
          }), 300);
        </script>
        """,
        height=0,
        scrolling=False,
    )

# ---------- Background video (permanent) ----------
bg_b64 = b64(ASSETS / "bg.mp4")
st.markdown(
    f"""
    <video id="trovule-bg" autoplay muted loop playsinline preload="auto">
      <source src="data:video/mp4;base64,{bg_b64}" type="video/mp4" />
    </video>
    <div class="trovule-mask"></div>
    """,
    unsafe_allow_html=True,
)

# ---------- Global styles & Streamlit overrides ----------
logo_b64 = b64(ASSETS / "logo.png")
st.markdown(
    f"""
    <style>
      /* Keep video always visible */
      #trovule-bg {{
        position: fixed;
        inset: 0;
        width: 100%;
        height: 100%;
        object-fit: cover;
        z-index: -3;
        filter: brightness(0.98) saturate(1.06);
      }}
      /* Gradient veil for contrast on text */
      .trovule-mask {{
        position: fixed;
        inset: 0;
        z-index: -2;
        background: linear-gradient(180deg,
          rgba(255,255,255,.55) 0%,
          rgba(255,255,255,.70) 38%,
          rgba(255,255,255,.82) 100%);
        pointer-events: none;
      }}

      /* Make Streamlit fully transparent where needed */
      html, body, [data-testid="stAppViewContainer"], .stApp, .main, [data-testid="block-container"] {{
        background: transparent !important; color: #000000 !important;
      }}
      [data-testid="stToolbar"] {{ backdrop-filter: blur(6px); }}
      @media (min-width: 900px) {{
        .block-container {{ max-width: 860px !important; }}
      }}

      /* Sunny Postcard theme */
      .trovule-header {{
        display:flex; flex-direction:column; align-items:center; gap:8px;
        text-align:center; margin: 18px auto 8px auto;
      }}
      .trovule-logo {{ width: 96px; height:auto; filter: drop-shadow(0 6px 14px rgba(0,0,0,.12)); }}
      .trovule-title {{ font-size: 32px; font-weight: 800; letter-spacing:.3px; color: #ADCB00; }}
      .trovule-sub {{
        font-size: 14px; opacity:.9; margin-top:-2px;
        background: linear-gradient(90deg,#FFECB3,#FFF); padding: 4px 10px; border-radius: 999px;
        border: 1px dashed rgba(0,0,0,.06);
      }}

      .trovule-card {{
        background: rgba(255,255,255,0.9);
        border: 1px solid rgba(0,0,0,.06);
        border-radius: 18px;
        padding: 22px;
        box-shadow: 0 12px 30px rgba(0,0,0,.08);
        backdrop-filter: blur(8px);
      }}

      .trovule-badge {{
        display:inline-block; padding:6px 12px; border-radius:999px;
        background:#FFF6D9; border:1px solid #FFE3A3; color:#9A5A00; font-weight:700; font-size:12px;
      }}

      .trovule-section-title {{ font-weight:700; font-size:16px; margin: 12px 0 6px 0; }}

      /* Inputs & button polish */
      label {{ font-weight: 600; }}
      .stTextInput>div>div>input, .stNumberInput input {{
        border-radius: 12px !important;
        border: 1px solid rgba(0,0,0,.12) !important;
        padding: 10px 12px !important;
        background: #fff !important;
      }}
      .stButton>button {{
        border-radius: 999px !important;
        padding: 10px 16px !important;
        font-weight: 700 !important;
        border: 0 !important;
        box-shadow: 0 6px 18px rgba(36,123,160,.18);
        background: linear-gradient(90deg,#FFD166,#FF9F1C);
        color:#1b1b1b;
      }}
      .stButton>button:hover {{ transform: translateY(-1px); }}

      /* Weather pills with dotted route */
      .trovule-pill {{
        background:#FFFFFF; border:1px solid rgba(0,0,0,.06); border-radius:16px;
        padding:14px; box-shadow:0 6px 18px rgba(0,0,0,.06);
      }}
      .trovule-pill .name {{ font-weight:700; margin:2px 0 6px 0; }}
      .trovule-row {{ display:flex; align-items:center; gap:10px; }}
      .trovule-route {{
        flex:0 0 50px; height:2px; background-image: linear-gradient(90deg, #247BA0 33%, rgba(36,123,160,0) 0%);
        background-size: 10px 2px; background-repeat: repeat-x; opacity:.6; margin-top: 34px;
      }}
      .trovule-emoji {{ font-size: 20px; margin-right:6px; }}

      .trovule-itinerary {{ line-height:1.6; }}
      .footer {{ text-align:center; margin-top:24px; opacity:.85; font-size:12px; }}
    </style>

    <!-- Header (logo → title → subtitle) -->
    <div class="trovule-header">
      <img src="data:image/png;base64,{logo_b64}" class="trovule-logo" alt="Trovule logo" />
      <div class="trovule-title">Trovule</div>
      <div class="trovule-sub">Happy, playful, and blissfully simple road trip planning, made just for you.</div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ---------- Main Card (form + results) ----------
with st.container():
    st.markdown('<div class="trovule-card">', unsafe_allow_html=True)

    with st.form("trip_form", clear_on_submit=False):
        st.markdown('<span class="trovule-badge">Let’s plan your road trip</span>', unsafe_allow_html=True)
        st.markdown("")
        origin = st.text_input("Start city (origin)", placeholder="e.g., Johannesburg")
        destination = st.text_input("Destination city", placeholder="e.g., Durban")
        duration = st.number_input("Trip length (days)", min_value=1, max_value=60, value=5, step=1)
        submitted = st.form_submit_button("Generate my itinerary ✨")

    if submitted:
        if not origin.strip() or not destination.strip():
            st.warning("Please enter both origin and destination.")
        else:
            with st.spinner("Gathering sunshine, checking skies, and plotting delight..."):
                try:
                    weather_o = current_weather(origin.strip())
                    weather_d = current_weather(destination.strip())

                
                    st.success("Weather checked! Now crafting your itinerary…")
                    confetti()  

                    md = generate_itinerary(origin.strip(), destination.strip(), int(duration))

                    # Weather “pills” with dotted route
                    st.markdown("")
                    st.markdown('<div class="trovule-section-title">Quick weather peek</div>', unsafe_allow_html=True)
                    col1, col2, col3 = st.columns([1, 0.3, 1])

                    with col1:
                        st.markdown(
                            f"""
                            <div class="trovule-pill">
                              <div class="trovule-small">Origin</div>
                              <div class="name">{origin.strip().title()}</div>
                              <div><span class="trovule-emoji">🌡️</span>{weather_o['temperature']}°C</div>
                              <div><span class="trovule-emoji">🌤️</span>{weather_o['condition'].title()}</div>
                            </div>
                            """, unsafe_allow_html=True
                        )
                    with col2:
                        st.markdown('<div class="trovule-route"></div>', unsafe_allow_html=True)
                    with col3:
                        st.markdown(
                            f"""
                            <div class="trovule-pill">
                              <div class="trovule-small">Destination</div>
                              <div class="name">{destination.strip().title()}</div>
                              <div><span class="trovule-emoji">🌡️</span>{weather_d['temperature']}°C</div>
                              <div><span class="trovule-emoji">🌤️</span>{weather_d['condition'].title()}</div>
                            </div>
                            """, unsafe_allow_html=True
                        )

                    # Itinerary card
                    st.markdown("")
                    st.markdown('<div class="trovule-section-title">Your blissful road trip plan</div>', unsafe_allow_html=True)
                    st.markdown('<div class="trovule-card trovule-itinerary">', unsafe_allow_html=True)
                    st.markdown(md)  # Markdown from API
                    st.markdown('</div>', unsafe_allow_html=True)

                    st.caption("Psst… prices are ZAR estimates and activities are suggestions—make it yours! 🧡")

                except APIError as e:
                    st.error(str(e))
                except Exception as e:
                    st.error(f"Unexpected error: {e}")
    else:
        st.info("Tell me where you’re going and how long, and I’ll craft a short, road trip plan with daily ZAR estimates.")

    st.markdown('</div>', unsafe_allow_html=True)

# ---------- Footer ----------
year = datetime.now().year
st.markdown(
    f"""
    <div class="footer">
      Created with love 💗 for travelers 🚗🗺.<br/>
      © {year} All rights reserved. Built by
      <a href="https://www.linkedin.com/in/ninankhwashu/" target="_blank" rel="noopener">Nina Nkhwashu</a>.
    </div>
    """,
    unsafe_allow_html=True
)
