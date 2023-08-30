import React from "react";
import { Link } from "react-router-dom";
import TopDestinations from "./TopDestinations";

function HomePage() {
  return (
    <div className="home-page">
      <h1>Travel Saver App</h1>
      <h2>Yes, you can take that trip you've always dreamed of.</h2>
      <TopDestinations />
      <Link to="plans">Plan List</Link>
    </div>
  );
}

export default HomePage;
