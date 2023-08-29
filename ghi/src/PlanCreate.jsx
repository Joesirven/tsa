import React, { useState } from "react";

const PlanCreate = () => {
    const [formData, setFormData] = useState({
        startOfBudget: "",
        endOfBudget: "",
        tripStartDate: "",
        tripEndDate: "",
        destination: "",
        monthlyBudget: "",
        // userId: userId,
    });

    const [isLoading, setIsLoading] = useState(false);

    const handleSubmit = async (e) => {
        e.preventDefault();
        setIsLoading(true);

        const url = "http://localhost:8000/plans/create";
        const fetchConfig = {
        method: "post",
        body: JSON.stringify(formData),
        headers: {
            "Content-Type": "application/json",
        },
        };

        try {
        const response = await fetch(url, fetchConfig);
        if (!response.ok) {

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
      <h1>Create a New Plan</h1>
      <form onSubmit={handleSubmit}>
        <label>Start of Budget:</label>
        <input
          type="date"
          name="startOfBudget"
          value={formData.startOfBudget}
          onChange={handleChange}
          required
        />
        <label>End of Budget:</label>
        <input
          type="date"
          name="endOfBudget"
          value={formData.endOfBudget}
          onChange={handleChange}
          required
        />
        <label>Trip Start Date:</label>
        <input
          type="date"
          name="tripStartDate"
          value={formData.tripStartDate}
          onChange={handleChange}
          required
        />
        <label>Trip End Date:</label>
        <input
          type="date"
          name="tripEndDate"
          value={formData.tripEndDate}
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
          name="monthlyBudget"
          value={formData.monthlyBudget}
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
