import React, { useState, useEffect } from "react";
import { useAuthContext } from "@galvanize-inc/jwtdown-for-react";
import { useNavigate } from "react-router-dom";


const PlanCreate = () => {
  const { token } = useAuthContext();
  const navigate = useNavigate();
  const [formData, setFormData] = useState({
    start_of_budget: "",
    end_of_budget: "",
    trip_start_date: "",
    trip_end_date: "",
    destination: "",
    monthly_budget: "",
    users_id: "",
  });

  const [isLoading, setIsLoading] = useState(false);
  const [isSubmitted, setIsSubmitted] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setIsLoading(true);

    const url = "http://localhost:8000/plans/create";
    const fetchConfig = {
      method: "post",
      body: JSON.stringify(formData),
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${token}`,
      },
    };
    try {
      const response = await fetch(url, fetchConfig);
      if (response.ok) {
        setIsSubmitted(true);
        navigate("/plans");
      }
    } catch (error) {

    } finally {
    setIsLoading(false);
    }
  };

  const getUserIdFromToken = (token) => {
    const tokenParts = token.split(".");
    if (tokenParts.length === 3) {
      const payload = JSON.parse(atob(tokenParts[1]));
      const user_id = payload.account.id;
      return user_id;
    }
    
    return null;
  };

  useEffect(() => {
    if (token) {
      const user_id = getUserIdFromToken(token);
      if (user_id) {
        setFormData((prevData) => ({
          ...prevData,
          users_id: user_id,
        }));
      }
    }
  }, [token]);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prevData) => ({
      ...prevData,
      [name]: value,
    }));
  };

  return (
    <div>
      {isSubmitted && <Redirect to="/plans" />}
      <h1>Create a New Plan</h1>
      <form onSubmit={handleSubmit}>
        <label>Start of Budget:</label>
        <input
          type="date"
          name="start_of_budget"
          value={formData.start_of_budget}
          onChange={handleChange}
          required
        />
        <label>End of Budget:</label>
        <input
          type="date"
          name="end_of_budget"
          value={formData.end_of_budget}
          onChange={handleChange}
          required
        />
        <label>Trip Start Date:</label>
        <input
          type="date"
          name="trip_start_date"
          value={formData.trip_start_date}
          onChange={handleChange}
          required
        />
        <label>Trip End Date:</label>
        <input
          type="date"
          name="trip_end_date"
          value={formData.trip_end_date}
          onChange={handleChange}
          required
        />
        <label>Destination:</label>
        <input
          type="text"
          name="destination"
          value={formData.destination}
          onChange={handleChange}
          required
        />
        <label>Monthly Budget:</label>
        <input
          type="number"
          step="0.01"
          name="monthly_budget"
          value={formData.monthly_budget}
          onChange={handleChange}
          required
        />
        <button type="submit" disabled={isLoading}>
          {isLoading ? "Submitting..." : "Submit"}
        </button>
      </form>
    </div>
  );
};

export default PlanCreate;
