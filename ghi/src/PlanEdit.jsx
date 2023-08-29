import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";

const PlanEdit = () => {
  const { planId } = useParams();

  const [planData, setPlanData] = useState({
    startOfBudget: "",
    endOfBudget: "",
    tripStartDate: "",
    tripEndDate: "",
    destination: "",
    monthlyBudget: "",
    userId: userId,
  });

  const [isLoading, setIsLoading] = useState(false);

  useEffect(() => {
    fetchPlanData(planId);
  }, [planId]);

  const fetchPlanData = async (planId) => {
    setIsLoading(true);
    const url = `http://localhost:8000/plans/${planId}`;
    try {
      const response = await fetch(url);
      if (response.ok) {
        const data = await response.json();
        setPlanData(data);
      }
    } catch (error) {
      console.error("An error occurred:", error);
    } finally {
      setIsLoading(false);
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setIsLoading(true);

    const url = `http://localhost:8000/plans/${planId}`;
    const fetchConfig = {
      method: "put",
      body: JSON.stringify(planData),
      headers: {
        "Content-Type": "application/json",
      },
    };

    try {
      const response = await fetch(url, fetchConfig);
      if (response.ok) {
      } else {
      }
    } catch (error) {
      console.error("An error occurred:", error);
    } finally {
      setIsLoading(false);
    }
  };

  const handleChange = (e) => {
    const { name, value } = e.target;
    setPlanData((prevData) => ({
      ...prevData,
      [name]: value,
    }));
  };

  return (
    <div>
      <h1>Edit Plan</h1>
      <form onSubmit={handleSubmit}>
        {/* Input fields with initial values from planData */}
        <button type="submit" disabled={isLoading}>
          {isLoading ? "Saving..." : "Save"}
        </button>
      </form>
    </div>
  );
};

export default PlanEdit;
