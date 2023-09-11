import React from "react";

export default function HomePage() {
  return (
    <div className="home-page">
      <header className="header">
        <h1>Welcome to Our Travel Saver App</h1>
      </header>
      <div className="container">
        <section className="features">
          <div className="feature">
            <i className="fas fa-database"></i>
            <h2>Plan a Trip</h2>
            <p>Come up the perfect trip using TSA!</p>
          </div>
          <div className="feature">
            <i className="fas fa-chart-line"></i>
            <h2>Set a Budget</h2>
            <p>
              Set up the best budget for your travel needs!
            </p>
          </div>
          <div className="feature">
            <i className="fas fa-users"></i>
            <h2>Log your Memories</h2>
            <p>Log your adventures using TSA!!</p>
          </div>
        </section>
      </div>
    </div>
  );
}
