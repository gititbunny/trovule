import { Link } from "react-router-dom";
import "../styles/Footer.css";

function Footer() {
  const currentYear = new Date().getFullYear();

  return (
    <footer className="site-footer">
      <div className="footer-container">
        <div className="footer-brand">
          <Link to="/" aria-label="Trovule home">
            <img
              src="/assets/logo.png"
              alt="Trovule"
              className="footer-logo"
            />
          </Link>

          <p>
            Weather-aware road trip planning with simple day-by-day
            itineraries and ZAR estimates.
          </p>
        </div>

        <div className="footer-links">
          <a href="/#how-it-works">How It Works</a>
          <a href="/#technology">Technology</a>
          <Link to="/planner">Plan Your Trip</Link>
        </div>
      </div>

      <div className="footer-bottom">
        <p>
          © {currentYear} Trovule. All rights reserved.
        </p>

        <p className="footer-credit">
          Designed & developed by <strong>Git It Bunny</strong>
        </p>

        <p>React + Python</p>
      </div>
    </footer>
  );
}

export default Footer;