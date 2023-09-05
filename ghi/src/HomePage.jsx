import React from "react";
import { Link } from "react-router-dom";

export default function HomePage() {
  return (
    <div>
      <h1>Home Page Place Holder</h1>
      <div className="container">
        <Link to="/Login">Login</Link>
        <Link to="/Signup">Signup</Link>
        <Link to="/plans">PlanList</Link>
        <Link to="/plan/create">PlanCreate</Link>
        <Link to="/plan{id}/edit">PlanEdit</Link>
        <Link to="/journal">Journal List</Link>
        <Link to="/journal/{id}">Journal Detail</Link>
        <Link to="/journal/create">Journal Create</Link>
      </div>
    </div>
  );
}
