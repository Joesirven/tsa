import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import { useAuthContext } from "@galvanize-inc/jwtdown-for-react";
import { useNavigate } from "react-router-dom";


const PlanEdit = () => {
  const { token } = useAuthContext();
  const { id } = useParams();
  const navigate = useNavigate();

  const [formData, setFormData] = useState({
    start_of_budget: "",
    end_of_budget: "",
    trip_start_date: "",
    trip_end_date: "",
    destination: "",
    monthly_budget: "",
  });

  const [isLoading, setIsLoading] = useState(false);
  const [isSubmitted, setIsSubmitted] = useState(false);

  useEffect(() => {
    const fetchPlanData = async () => {
      try {
        const url = `http://localhost:8000/plans/${id}`;
        const response = await fetch(url, {
          method: "get",
          headers: {
            Authorization: `Bearer ${token}`,
          },
        });

        if (response.ok) {
          const planData = await response.json();
          setFormData(planData);
        } else {
          
        }
      } catch (error) {
        
      } finally {
        setIsLoading(false);
      }
    };

    if (token) {
      fetchPlanData();
    }
  }, [token, id]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setIsLoading(true);

    const url = `http://localhost:8000/plans/${id}`;
    const fetchConfig = {
      method: "put",
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
      } else {
        
      }
    } catch (error) {
      
    } finally {
      setIsLoading(false);
    }
  };

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prevData) => ({
      ...prevData,
      [name]: value,
    }));
  };

  return (
    <div>
      <h1>Edit Plan</h1>
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
          {isLoading ? "Updating..." : "Update"}
        </button>
      </form>
    </div>
  );
};

export default PlanEdit;
