# app.py
import base64
from pathlib import Path
from datetime import datetime

import streamlit as st
from dotenv import load_dotenv

from services.shecodes_client import current_weather, generate_itinerary, APIError

# --- Setup ---
load_dotenv()
ASSETS = Path(__file__).parent / "assets"

st.set_page_config(
    page_title="Trovule — Your Blissful Trip Buddy",
    page_icon=str(ASSETS / "icon.png"),
    layout="centered",
)

# --- Helpers ---
def get_base64(path: Path) -> str:
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

# --- Background video ---
bg_b64 = get_base64(ASSETS / "bg.mp4")
st.markdown(
    f"""
    <video id="trovule-bg" autoplay muted loop playsinline>
      <source src="data:video/mp4;base64,{bg_b64}" type="video/mp4" />
    </video>
    <div class="trovule-mask"></div>
    """,
    unsafe_allow_html=True,
)

# --- Styles ---
st.markdown(
    """
    <style>
      /* Full-page background video */
      #trovule-bg{
        position: fixed;
        right: 0;
        bottom: 0;
        min-width: 100%;
        min-height: 100%;
        width: auto;
        height: auto;
        z-index: -2;
        object-fit: cover;
        filter: brightness(0.96) saturate(1.08);
      }
      /* Soft gradient mask over the video for contrast */
      .trovule-mask{
        position: fixed;
        inset: 0;
        z-index: -1;
        background: linear-gradient(180deg, rgba(255,255,255,.55) 0%, rgba(255,255,255,.75) 40%, rgba(255,255,255,.85) 100%);
        pointer-events: none;
      }
      @media (min-width: 900px) {
        .block-container { max-width: 820px !important; }
      }
      .trovule-card{
        background: rgba(255,255,255,0.86);
        border: 1px solid rgba(0,0,0,.06);
        border-radius: 16px;
        padding: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,.08);
        backdrop-filter: blur(6px);
      }
      .trovule-header{
        display: flex; flex-direction: column; align-items: center; gap: 8px;
        margin: 16px auto 10px auto;
        text-align: center;
      }
      .trovule-logo{ width: 84px; height: auto; }
      .trovule-title{ font-size: 30px; font-weight: 800; letter-spacing: .4px; }
      .trovule-sub{ font-size: 14px; opacity: .85; margin-top: -2px; }
      .trovule-badge{
        display:inline-block; padding:6px 12px; border-radius:999px;
        background:#FFF6D9; border:1px solid #FFE6A3; color:#A35A00; font-weight:700; font-size:12px;
      }
      .trovule-form { margin-top: 12px; }
      .trovule-section-title{ font-weight: 700; font-size: 16px; margin: 10px 0 6px 0; }
      .trovule-small{ font-size:12px; opacity:.75; }
      .trovule-itinerary{ line-height: 1.6; }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Header (logo → title → subtitle) ---
logo_b64 = get_base64(ASSETS / "logo.png")
st.markdown(
    f"""
    <div class="trovule-header">
      <img src="data:image/png;base64,{logo_b64}" class="trovule-logo" alt="Trovule logo" />
      <div class="trovule-title">Trovule</div>
      <div class="trovule-sub">Happy, playful, and blissfully simple road trip planning — made just for you.</div>
    </div>
    """,
    unsafe_allow_html=True
)

# ---------- Input form ----------
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

                    st.success("Weather checked! Now crafting your itinerary...")

                    md = generate_itinerary(origin.strip(), destination.strip(), int(duration))
                    st.balloons()

                    # ---------- Output: Weather cards ----------
                    st.markdown("")
                    st.markdown('<div class="trovule-section-title">Quick weather peek</div>', unsafe_allow_html=True)
                    c1, c2 = st.columns(2)
                    with c1:
                        st.markdown(
                            f"""
                            <div class="trovule-card">
                              <div class="trovule-small">Origin</div>
                              <div style="font-weight:700; margin:2px 0 6px 0;">{origin.strip().title()}</div>
                              <div><span class="trovule-emoji">🌡️</span> {weather_o['temperature']}°C</div>
                              <div><span class="trovule-emoji">🌤️</span> {weather_o['condition'].title()}</div>
                            </div>
                            """,
                            unsafe_allow_html=True
                        )
                    with c2:
                        st.markdown(
                            f"""
                            <div class="trovule-card">
                              <div class="trovule-small">Destination</div>
                              <div style="font-weight:700; margin:2px 0 6px 0;">{destination.strip().title()}</div>
                              <div><span class="trovule-emoji">🌡️</span> {weather_d['temperature']}°C</div>
                              <div><span class="trovule-emoji">🌤️</span> {weather_d['condition'].title()}</div>
                            </div>
                            """,
                            unsafe_allow_html=True
                        )

                    # ---------- Output: Itinerary ----------
                    st.markdown("")
                    st.markdown('<div class="trovule-section-title">Your blissful road trip plan</div>', unsafe_allow_html=True)
                    st.markdown('<div class="trovule-card trovule-itinerary">', unsafe_allow_html=True)
                    st.markdown(md)  # Itinerary text (Markdown)
                    st.markdown('</div>', unsafe_allow_html=True)

                    st.caption("Psst… prices are estimates in ZAR and activities are suggestions—make it yours! 🧡")

                except APIError as e:
                    st.error(str(e))
                except Exception as e:
                    st.error(f"Unexpected error: {e}")
    else:
        st.info("Tell me where you’re going and how long, and I’ll craft a short, emoji-sprinkled plan with daily ZAR estimates.")

    st.markdown('</div>', unsafe_allow_html=True)

# ---------- Footer ----------
year = datetime.now().year
st.markdown(
    f"""
    <div class="footer" style="text-align:center; margin-top:2rem; opacity:.8;">
      Created with love 💗 for travelers 🚗🗺.<br/>
      © {year} All rights reserved. Built by
      <a href="https://www.linkedin.com/in/ninankhwashu/" target="_blank" rel="noopener">Nina Nkhwashu</a>.
    </div>
    """,
    unsafe_allow_html=True
)
