import React from "react";
import { Link } from "react-router-dom";

export default function home() {
  return (
    <div>
      <h1>Home Page Place Holder</h1>
      <Link to="/Login">Login</Link>
      <Link to="/Signup">Signup</Link>
    </div>
  );
}
