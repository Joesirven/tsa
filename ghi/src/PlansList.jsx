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
    // const sortedPlans = this.state.plans.slice().sort((a, b) => a.trip_start_date.localeCompare(b.trip_start_date));
    // const earliestPlan = sortedPlans.shift();
    // const otherPlans = sortedPlans;
    // console.log("Sorted Plans:", sortedPlans);
    // console.log("Earliest Plan:", earliestPlan);
    // console.log("Other Plans:", otherPlans);

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
        {/* <div style={{ display: "flex" }}>
          <div style={{ flex: 1 }}>
            <div className="card">
              <div className="card-body">
                <h5 className="card-title">Earliest Plan</h5>
                <p>{earliestPlan.destination}</p>
                <p>{earliestPlan.trip_start_date}</p>
              </div>
            </div>
          </div>
          <div style={{ flex: 1, marginLeft: "20px" }}>
            {otherPlans.map((plan) => (
              <div key={plan.id} className="card mb-3">
                <div className="card-body">
                  <h5 className="card-title">{plan.destination}</h5>
                  <p>{plan.trip_start_date}</p>
                </div>
              </div>
            ))}
          </div>
        </div> */}
        <table className="table table-striped">
          <thead>
            <tr>
              <th
                style={{ borderBottom: "1px solid black", textAlign: "left" }}
              >
                start_of_budget
              </th>
              <th
                style={{ borderBottom: "1px solid black", textAlign: "left" }}
              >
                end_of_budget
              </th>
              <th
                style={{ borderBottom: "1px solid black", textAlign: "left" }}
              >
                trip_start_date
              </th>
              <th
                style={{ borderBottom: "1px solid black", textAlign: "left" }}
              >
                trip_end_date
              </th>
              <th
                style={{ borderBottom: "1px solid black", textAlign: "left" }}
              >
                destination
              </th>
              <th
                style={{ borderBottom: "1px solid black", textAlign: "left" }}
              >
                monthly_budget
              </th>
            </tr>
          </thead>
          <tbody>
            {this.state.plans.map((plans) => {
              console.log("Fetched Data:", plans);
              return (
                <tr key={plans.id}>
                  <td>{plans.start_of_budget}</td>
                  <td>{plans.end_of_budget}</td>
                  <td>{plans.trip_start_date}</td>
                  <td>{plans.trip_end_date}</td>
                  <td>{plans.destination}</td>
                  <td>{plans.monthly_budget}</td>
                </tr>
              );
            })}
          </tbody>
        </table>
      </div>
    );
  }
}

export default PlanList;
