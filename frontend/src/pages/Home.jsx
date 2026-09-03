import { Link } from "react-router-dom";
import Header from "../components/Header";
import "../styles/Home.css";

function Home() {
  return (
    <div className="home-page">
      <Header />

      <main>
        {/* Hero */}
        <section className="hero">
          <div className="hero-container">
            <div className="hero-copy">
              <div className="hero-eyebrow">
                <span className="hero-eyebrow-dot"></span>
                Your road trip, figured out.
              </div>

              <h1 className="hero-title">
                Less planning.
                <br />
                More <span className="hero-title-accent">going.</span>
              </h1>

              <p className="hero-description">
                Trovule turns your route into a simple day-by-day road trip
                plan, combining destination weather, itinerary ideas and
                estimated costs in South African Rand.
              </p>

              <div className="hero-actions">
                <Link to="/planner" className="hero-primary-button">
                  Plan Your Trip →
                </Link>

                <a href="#how-it-works" className="hero-secondary-button">
                  See How It Works
                </a>
              </div>
            </div>

            <div className="hero-visual">
              <div className="hero-shape hero-shape-lime"></div>
              <div className="hero-shape hero-shape-purple"></div>

              <span className="hero-road-label">Road trip ready ✦</span>

              <div className="trip-card">
                <div className="trip-card-top">
                  <span className="trip-card-label">Your trip</span>
                  <span className="trip-card-days">3 days</span>
                </div>

                <div className="route">
                  <div className="route-city">
                    <span className="route-small">From</span>
                    <span className="route-name">Johannesburg</span>
                  </div>

                  <div className="route-line"></div>

                  <div className="route-city">
                    <span className="route-small">To</span>
                    <span className="route-name">Durban</span>
                  </div>
                </div>

                <div className="weather-preview">
                  <div className="weather-box">
                    <span className="weather-city">Johannesburg</span>
                    <strong className="weather-temp">24°</strong>
                    <span className="weather-condition">Clear skies</span>
                  </div>

                  <div className="weather-box">
                    <span className="weather-city">Durban</span>
                    <strong className="weather-temp">27°</strong>
                    <span className="weather-condition">Warm & sunny</span>
                  </div>
                </div>

                <div className="itinerary-preview">
                  <div className="itinerary-heading">
                    <strong>Trip preview</strong>
                    <span>ZAR estimates</span>
                  </div>

                  <div className="itinerary-item">
                    <span className="itinerary-day">01</span>

                    <div className="itinerary-text">
                      <strong>Hit the road</strong>
                      <span>Johannesburg → Midlands</span>
                    </div>
                  </div>

                  <div className="itinerary-item">
                    <span className="itinerary-day">02</span>

                    <div className="itinerary-text">
                      <strong>Explore the coast</strong>
                      <span>Local stops + activities</span>
                    </div>
                  </div>

                  <div className="itinerary-item">
                    <span className="itinerary-day">03</span>

                    <div className="itinerary-text">
                      <strong>Destination day</strong>
                      <span>Arrive and explore Durban</span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>
      </main>
    </div>
  );
}

export default Home;