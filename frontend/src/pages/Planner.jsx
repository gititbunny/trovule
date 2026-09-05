import { useState } from "react";
import ReactMarkdown from "react-markdown";
import Header from "../components/Header";
import Footer from "../components/Footer";
import "../styles/Planner.css";

function Planner() {
  const [form, setForm] = useState({
    origin: "",
    destination: "",
    duration_days: 3,
  });

  const [result, setResult] = useState(null);
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  function handleChange(event) {
    const { name, value } = event.target;

    setForm((current) => ({
      ...current,
      [name]: name === "duration_days" ? Number(value) : value,
    }));
  }

  async function handleSubmit(event) {
    event.preventDefault();

    setLoading(true);
    setError("");
    setResult(null);

    try {
      const response = await fetch("/api/plan", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(form),
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.detail || "Unable to generate your trip.");
      }

      setResult(data);
    } catch (requestError) {
      setError(requestError.message);
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="planner-page">
      <Header />

      <main>
        {/* Planner Intro */}
        <section className="planner-hero">
          <div className="planner-container">
            <span className="planner-label">Trovule Trip Planner</span>

            <h1>
              Where are we
              <br />
              <span>going?</span>
            </h1>

            <p>
              Add your route and trip length. Trovule will check the weather
              and build your road-trip itinerary.
            </p>
          </div>
        </section>

        {/* Planner Form */}
        <section className="planner-workspace">
          <div className="planner-container">
            <form className="trip-form" onSubmit={handleSubmit}>
              <div className="form-heading">
                <div>
                  <span>Start here</span>
                  <h2>Plan your road trip</h2>
                </div>

                <span className="form-step">01</span>
              </div>

              <div className="form-grid">
                <div className="form-field">
                  <label htmlFor="origin">Starting point</label>

                  <input
                    id="origin"
                    name="origin"
                    type="text"
                    placeholder="e.g. Johannesburg"
                    value={form.origin}
                    onChange={handleChange}
                    required
                    minLength="2"
                    maxLength="100"
                  />
                </div>

                <div className="form-field">
                  <label htmlFor="destination">Destination</label>

                  <input
                    id="destination"
                    name="destination"
                    type="text"
                    placeholder="e.g. Durban"
                    value={form.destination}
                    onChange={handleChange}
                    required
                    minLength="2"
                    maxLength="100"
                  />
                </div>

                <div className="form-field">
                  <label htmlFor="duration_days">Trip length</label>

                  <select
                    id="duration_days"
                    name="duration_days"
                    value={form.duration_days}
                    onChange={handleChange}
                  >
                    {Array.from({ length: 14 }, (_, index) => index + 1).map(
                      (day) => (
                        <option key={day} value={day}>
                          {day} {day === 1 ? "day" : "days"}
                        </option>
                      ),
                    )}
                  </select>
                </div>
              </div>

              {error && (
                <div className="planner-error" role="alert">
                  {error}
                </div>
              )}

              <button
                type="submit"
                className="generate-button"
                disabled={loading}
              >
                {loading ? "Planning your trip..." : "Generate My Trip →"}
              </button>
            </form>

            {/* Results */}
            {loading && (
              <section className="planner-loading" aria-live="polite">
                <span className="loading-dot"></span>

                <div>
                  <strong>Building your road trip...</strong>
                  <p>Checking weather and creating your itinerary.</p>
                </div>
              </section>
            )}

            {result && (
              <section className="trip-results">
                <div className="results-heading">
                  <div>
                    <span>Your trip</span>

                    <h2>
                      {result.origin} → {result.destination}
                    </h2>
                  </div>

                  <span className="results-days">
                    {result.duration_days}{" "}
                    {result.duration_days === 1 ? "day" : "days"}
                  </span>
                </div>

                <div className="results-weather">
                  <article className="result-weather-card">
                    <span>Starting point</span>
                    <h3>{result.origin}</h3>

                    <strong>
                      {result.weather.origin.temperature}°
                    </strong>

                    <p>{result.weather.origin.condition}</p>
                  </article>

                  <article className="result-weather-card">
                    <span>Destination</span>
                    <h3>{result.destination}</h3>

                    <strong>
                      {result.weather.destination.temperature}°
                    </strong>

                    <p>{result.weather.destination.condition}</p>
                  </article>
                </div>

                <article className="itinerary-result">
                  <div className="itinerary-result-heading">
                    <div>
                      <span>Generated itinerary</span>
                      <h3>Your road trip plan</h3>
                    </div>

                    <span className="zar-label">ZAR estimates</span>
                  </div>

                  <div className="itinerary-markdown">
                    <ReactMarkdown>
                      {result.itinerary}
                    </ReactMarkdown>
                  </div>
                </article>
              </section>
            )}
          </div>
        </section>
      </main>

      <Footer />
    </div>
  );
}

export default Planner;