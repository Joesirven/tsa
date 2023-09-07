import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import { useAuthContext } from "@galvanize-inc/jwtdown-for-react";

const PlanList = () => {
  const { token } = useAuthContext();
  const [plans, setPlans] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const [errorMessage, setErrorMessage] = useState(null);

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
    const fetchPlans = async () => {
      setIsLoading(true);
      const user_id = getUserIdFromToken(token);
      try {
        const URL = "http://localhost:8000/plans";
        const response = await fetch(URL, {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        });
        if (response.ok) {
          const data = await response.json();

          const filteredPlans = data.filter((plan) => plan.users_id === user_id);

          setPlans(filteredPlans);
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
      fetchPlans();
    }
  }, [token]);


  let earliestPlan = null;
  let otherPlans = [];

  if (plans.length > 0) {
    const sortedPlans = plans
      .slice()
      .sort((a, b) => a.trip_start_date.localeCompare(b.trip_start_date));
    earliestPlan = sortedPlans.shift();
    otherPlans = sortedPlans;
  }
  return (
    <div className="shadow p-3 mt-4">
      <h1
        style={{
          fontSize: "64px",
        }}
      >
        Plans
      </h1>
      {errorMessage && <div className="alert alert-danger">{errorMessage}</div>}
      {isLoading && <div className="loading-indicator">Loading...</div>}
      <div style={{ display: "flex" }}>
        <div style={{ flex: 2, minWidth: "250px" }}>
          {earliestPlan && (
            <div className="card">
              <div className="card-body">
                <h5 className="card-title">Current Plan</h5>
                <div>
                  Destination: <div>{earliestPlan.destination}</div>
                </div>
                <div>
                  Budget start: <div>{earliestPlan.start_of_budget}</div>
                </div>
                <div>
                  Budget end: <div>{earliestPlan.end_of_budget}</div>
                </div>
                <div>
                  Trip Start: <div>{earliestPlan.trip_start_date}</div>
                </div>
              </div>
              <Link
                to={`/plans/${earliestPlan.id}`}
                className="btn btn-primary"
              >
                Details
              </Link>
            </div>
          )}
        </div>
        <div
          style={{
            flex: 3,
            marginLeft: "20px",
            display: "flex",
            flexWrap: "wrap",
          }}
        >
          {otherPlans.map((plan) => (
            <div
              key={plan.id}
              className="card mb-2"
              style={{ margin: "0 10px" }}
            >
              <div className="card-body">
                <h5 className="card-title">
                  Destination:<div>{plan.destination}</div>
                </h5>
                <div>
                  Budget start:<div>{plan.start_of_budget}</div>
                </div>
                <div>
                  Budget end:<div>{plan.end_of_budget}</div>
                </div>
                <div>
                  Trip Start:<div>{plan.trip_start_date}</div>
                </div>
                <Link to={`/plans/${plan.id}/edit`} className="btn btn-primary">
                  Edit
                </Link>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default PlanList;
