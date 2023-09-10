import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import { useAuthContext } from "@galvanize-inc/jwtdown-for-react";
import { useNavigate } from "react-router-dom";


const PlanEdit = () => {
  const { token } = useAuthContext();
  const { id } = useParams();
  const navigate = useNavigate();
  const [isLoading, setIsLoading] = useState(false);
  const [isSubmitted, setIsSubmitted] = useState(false);
  const [errorMessage, setErrorMessage] = useState("");
  
  const [formData, setFormData] = useState({
    start_of_budget: "",
    end_of_budget: "",
    trip_start_date: "",
    trip_end_date: "",
    destination: "",
    monthly_budget: "",
  });

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
          setErrorMessage("Failed to fetch data. Please try again later.");
        }
      } catch (error) {
        setErrorMessage("An error occurred while fetching data.");
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

    if (
      new Date(formData.end_of_budget) <= new Date(formData.start_of_budget) ||
      new Date(formData.trip_start_date) < new Date(formData.end_of_budget) ||
      new Date(formData.trip_end_date) < new Date(formData.trip_start_date)
    ) {
      setErrorMessage("Please check dates.");
      setIsLoading(false);
      setTimeout(() => {
        setErrorMessage("");
      }, 3000);
      return;
    }

    try {
      const response = await fetch(url, fetchConfig);
      if (response.ok) {
        setIsSubmitted(true);
        navigate("/plans");
      } else {
        setErrorMessage("Failed to update data. Please try again later.");
      }
    } catch (error) {
      setErrorMessage("An error occurred while updating data.");
    } finally {
      setIsLoading(false);
    }
  };

  const handleChange = (e) => {
    const { name, value } = e.target;
    if (name === "end_of_budget") {
      const startOfBudgetDate = new Date(formData.start_of_budget);
      const endOfBudgetDate = new Date(value);

      if (endOfBudgetDate <= startOfBudgetDate) {
        setErrorMessage("End of Budget must be after the Start of Budget");
        setTimeout(() => {
          setErrorMessage("");
        }, 3000);
        return;
      }
    } else if (name === "trip_start_date") {
      if (new Date(value) < new Date(formData.end_of_budget)) {
        setErrorMessage("Trip Start Date must be on or after End of Budget");
        setTimeout(() => {
          setErrorMessage("");
        }, 3000);
        return;
      }
    } else if (name === "trip_end_date") {
      if (new Date(value) < new Date(formData.trip_start_date)) {
        setErrorMessage("Trip End Date must be on or after Trip Start Date");
        setTimeout(() => {
          setErrorMessage("");
        }, 3000);
        return;
      }
    }
    setFormData((prevData) => ({
      ...prevData,
      [name]: value,
    }));
  };

  return (
    <div>
      {isSubmitted && <Redirect to="/plans" />}
      <h1>Edit Plan</h1>
      {errorMessage && <div className="alert alert-danger">{errorMessage}</div>}
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
          min="0.01"
        />
        <button type="submit" disabled={isLoading}>
          {isLoading ? "Updating..." : "Update"}
        </button>
      </form>
    </div>
  );
};

export default PlanEdit;
