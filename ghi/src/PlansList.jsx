import React from "react";

class PlanList extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      plans: [],
    };
  }

  async componentDidMount() {
    const URL = "http://localhost:8000/plans";
    const response = await fetch(URL);
    if (response.ok) {
      const data = await response.json();
      this.setState({ plans: data });
    }
  }

  render() {
    const { plans } = this.state;

    let earliestPlan = null;
    let otherPlans = [];

    if (plans.length > 0) {
      const sortedPlans = plans.slice().sort((a, b) => a.trip_start_date.localeCompare(b.trip_start_date));
      earliestPlan = sortedPlans.shift();
      otherPlans = sortedPlans;
    }
    return (
      <div className="shadow p-4 mt-4">
        <h1
          style={{
            fontSize: "42px",
            paddingTop: "30px",
            paddingBottom: "10px",
          }}
        >
          Plans
        </h1>
        <div style={{ display: "flex" }}>
          <div style={{ flex: 1 }}>
            {earliestPlan && (
              <div className="card">
                <div className="card-body">
                  <h5 className="card-title">Current Plan</h5>
                  <p>{earliestPlan.destination}</p>
                  <p>{earliestPlan.trip_start_date}</p>
                </div>
              </div>
            )}
          </div>
          <div style={{ flex: 3, marginLeft: "20px", display: "flex", flexWrap: "wrap" }}>
            {otherPlans.map((plan) => (
              <div key={plan.id} className="card mb-2" style={{ flexBasis: "30%", margin: "0 10px"}}>
                <div className="card-body">
                  <h5 className="card-title">{plan.destination}</h5>
                  <p>{plan.trip_start_date}</p>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
    );
  }
}

export default PlanList;
