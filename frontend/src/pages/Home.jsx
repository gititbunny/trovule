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

        {/* How It Works */}
        <section className="how-it-works" id="how-it-works">
          <div className="how-container">
            <div className="section-heading">
              <span className="section-label">How it works</span>

              <h2>
                From idea to road trip
                <br />
                in <span>three simple steps.</span>
              </h2>

              <p>
                Tell Trovule where you are going and how long you have. It
                handles the planning from there.
              </p>
            </div>

            <div className="how-grid">
              <article className="how-card how-card-lime">
                <div className="how-number">01</div>

                <div>
                  <span className="how-kicker">Choose your route</span>
                  <h3>Where are you heading?</h3>
                  <p>
                    Enter your starting point, destination and the number of
                    days you want to travel.
                  </p>
                </div>

                <div className="mini-route">
                  <span>JHB</span>
                  <div className="mini-route-line"></div>
                  <span>DBN</span>
                </div>
              </article>

              <article className="how-card how-card-light">
                <div className="how-number">02</div>

                <div>
                  <span className="how-kicker">Check the weather</span>
                  <h3>Know what to expect.</h3>
                  <p>
                    Trovule checks current conditions for your route so the
                    trip starts with useful context.
                  </p>
                </div>

                <div className="weather-chip-row">
                  <span className="weather-chip">☀ 24° JHB</span>
                  <span className="weather-chip">☀ 27° DBN</span>
                </div>
              </article>

              <article className="how-card how-card-dark">
                <div className="how-number">03</div>

                <div>
                  <span className="how-kicker">Generate your plan</span>
                  <h3>Get your day-by-day trip.</h3>
                  <p>
                    Receive itinerary ideas and estimated costs in South
                    African Rand, ready for you to explore.
                  </p>
                </div>

                <Link to="/planner" className="how-card-link">
                  Start planning →
                </Link>
              </article>
            </div>
          </div>
        </section>

        {/* Core Features */}
        <section className="features-section">
          <div className="features-container">
            <div className="features-heading">
              <span className="section-label">Built for the road</span>

              <h2>
                The useful stuff,
                <br />
                <span>all in one trip plan.</span>
              </h2>
            </div>

            <div className="features-layout">
              <article className="feature-card feature-weather">
                <div className="feature-card-copy">
                  <span className="feature-tag">Weather</span>

                  <h3>Start with the conditions.</h3>

                  <p>
                    Check current weather for your starting point and
                    destination before building the rest of your trip.
                  </p>
                </div>

                <div className="feature-weather-visual">
                  <div className="feature-weather-main">
                    <span>Durban</span>
                    <strong>27°</strong>
                    <small>Warm & sunny</small>
                  </div>

                  <div className="feature-sun">☀</div>
                </div>
              </article>

              <article className="feature-card feature-itinerary">
                <div className="feature-card-copy">
                  <span className="feature-tag">AI itinerary</span>

                  <h3>A plan for every day.</h3>

                  <p>
                    Trovule generates a simple day-by-day itinerary based on
                    your route and trip duration.
                  </p>
                </div>

                <div className="feature-days">
                  <div className="feature-day">
                    <span>01</span>
                    <div>
                      <strong>Departure</strong>
                      <small>Start the journey</small>
                    </div>
                  </div>

                  <div className="feature-day">
                    <span>02</span>
                    <div>
                      <strong>Explore</strong>
                      <small>Stops & activities</small>
                    </div>
                  </div>

                  <div className="feature-day">
                    <span>03</span>
                    <div>
                      <strong>Destination</strong>
                      <small>Arrive & discover</small>
                    </div>
                  </div>
                </div>
              </article>

              <article className="feature-card feature-budget">
                <div className="feature-card-copy">
                  <span className="feature-tag">ZAR estimates</span>

                  <h3>Plan with local costs in mind.</h3>

                  <p>
                    Trip suggestions include estimated daily costs in South
                    African Rand, keeping the plan relevant for local travel.
                  </p>
                </div>

                <div className="budget-visual">
                  <div>
                    <span>Estimated day</span>
                    <strong>R1,250</strong>
                  </div>

                  <span className="budget-badge">ZAR</span>
                </div>
              </article>
            </div>
          </div>
        </section>
      </main>
    </div>
  );
}

export default Home;