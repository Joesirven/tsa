import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { useAuthContext } from "@galvanize-inc/jwtdown-for-react";


const PlanDetails = () => {
  const { token } = useAuthContext();
  const { planId } = useParams();
  const [savings, setSavings] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
console.log(planId, "this is the plan id");

  useEffect(() => {
    // Fetch the specific plan details using userId and planId
    const fetchSavings = async () => {
      setIsLoading(true);
      try {
        const URL = (`http://localhost:8000/savings`);
        const response = await fetch(URL, {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        });
        if (response.ok) {
          console.log("response is ok");
          const data = await response.json();
          //console.log(data)
          const planSavings = data.filter((saving) => saving.plans_id == planId);
          setSavings(planSavings);
          console.log("this is savings", savings)
        }
      } catch (error) {
        // Handle errors
      } finally {
        setIsLoading(false);
      }
    };

    if (token) {
      fetchSavings();
    }
  }, [token, planId]);

  if (!savings) {
    return <div>Loading...</div>;
  }

  return (
    <div className="shadow p-3 mt-4">
      <h1 style={{ fontSize: "64px" }}>Plan Details</h1>
      {/* Render plan details here */}
      <h2>Savings for Plan {planId}</h2>
      <ul>
        {savings.map((saving) => (
          <li key={saving.id}>
            Current Amount Saved: {saving.current_amount_saved}<br />
            Final Goal Amount: {saving.final_goal_amount}<br />
            If Saved: {saving.if_saved ? "Yes" : "No"}<br />
          </li>
        ))}
      </ul>
    </div>
  );

};

export default PlanDetails;
