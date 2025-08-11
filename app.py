from pathlib import Path
import streamlit as st
from dotenv import load_dotenv
from services.shecodes_client import current_weather, generate_itinerary, APIError


load_dotenv()

ASSETS = Path(__file__).parent / "assets"

st.set_page_config(
    page_title="Trovule — Your Blissful Trip Buddy",
    page_icon=str(ASSETS / "icon.png"),
    layout="centered",
)

# ---------- Theming / playful styling ----------
st.markdown(
    """
    <style>
      /* Global */
      .trovule-hero {
        display:flex; gap:14px; align-items:center; justify-content:center; margin: 10px 0 4px 0;
      }
      .trovule-title {
        font-size: 28px; font-weight: 800; letter-spacing:.5px;
      }
      .trovule-sub {
        font-size: 14px; opacity:.8; margin-top:-6px;
      }
      .trovule-card {
        background: #ffffff;
        border: 1px solid rgba(0,0,0,.06);
        border-radius: 14px;
        padding: 16px 16px;
        box-shadow: 0 8px 24px rgba(0,0,0,.05);
      }
      .trovule-badge {
        display:inline-block; padding:4px 10px; border-radius:999px;
        background: #F0F7FF; border:1px solid #D9EAFF; font-size:12px; font-weight:600; color:#2563EB;
      }
      .trovule-emoji {
        font-size: 22px; margin-right:6px;
      }
      .trovule-section-title {
        font-weight:700; margin-bottom: 8px; font-size:16px;
      }
      .trovule-small {
        font-size:12px; opacity:.75;
      }
      .trovule-itinerary {
        line-height:1.55;
      }
      /* Center the main block on narrow screens nicely */
      @media (min-width: 900px) {
        .block-container { max-width: 760px !important; }
      }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------- Header ----------
col_logo, col_title = st.columns([1, 6])
with col_logo:
    st.image(str(ASSETS / "logo.png"), width=72)
with col_title:
    st.markdown('<div class="trovule-hero">🧭<div class="trovule-title">Trovule</div></div>', unsafe_allow_html=True)
    st.markdown('<div class="trovule-sub">Happy, playful, and blissfully simple road trip planning — made just for you.</div>', unsafe_allow_html=True)

st.markdown("")

# ---------- Input form ----------
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
                st.markdown(md) 
                st.markdown('</div>', unsafe_allow_html=True)

                st.caption("Psst… prices are estimates in ZAR and activities are suggestions—make it yours! 🧡")

            except APIError as e:
                st.error(str(e))
            except Exception as e:
                st.error(f"Unexpected error: {e}")
else:
    st.info("Tell me where you’re going and how long, and I’ll craft a short, emoji-sprinkled plan with daily ZAR estimates.")

# Footer
st.markdown(
    f"""
    <div class="footer" style="text-align:center; margin-top:2rem; opacity:.8;">Created with love 💗 for travelers 🚗🗺.
      <br/> Built by <a href="https://www.linkedin.com/in/ninankhwashu/" target="_blank">Nina Nkhwashu</a>.
    </div>
    """,
    unsafe_allow_html=True
)