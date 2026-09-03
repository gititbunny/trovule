import { Link, NavLink } from "react-router-dom";
import "../styles/Header.css";

function Header() {
  return (
    <header className="site-header">
      <div className="header-inner">
        <Link to="/" className="brand-link" aria-label="Trovule home">
          <img
            src="/assets/logo.png"
            alt="Trovule"
            className="brand-logo"
          />
        </Link>

        <nav className="main-nav" aria-label="Main navigation">
          <NavLink to="/">Home</NavLink>

          <Link to="/#how-it-works">
            How It Works
          </Link>

          <Link to="/#technology">
            Technology
          </Link>

          <Link to="/planner" className="planner-link">
            Plan Your Trip
          </Link>
        </nav>
      </div>
    </header>
  );
}

export default Header;