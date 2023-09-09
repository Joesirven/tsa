import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { useAuthContext } from "@galvanize-inc/jwtdown-for-react";


const PlanDetail = () => {
  const { token } = useAuthContext();
  const { planId } = useParams();
  const [savings, setSavings] = useState([]);
  const [transactions, setTransactions] = useState([]);
  const [checkValues, setCheckValues] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  //console.log(planId, "this is the plan id");

  const fetchSavings = async () => {
    try {
      const URL = (`http://localhost:8000/savings`);
      const savingsResponse = await fetch(URL, {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });
      if (savingsResponse.ok) {
        //console.log("response is ok");
        const data = await savingsResponse.json();
        //console.log(data)
        const planSavings = data.filter((saving) => saving.plans_id == planId);
        setSavings(planSavings);
      }
    } catch (error) {
      console.log(error)
    }
  }

  const fetchTransactions = async () => {
    try {
    const transactionsURL = `http://localhost:8000/transactions`;
    const transactionsResponse = await fetch(transactionsURL, {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });
      if (transactionsResponse.ok) {
        const transactionsData = await transactionsResponse.json();
        const userTransactions = transactionsData.filter(
          (transaction) => transaction.savings_id == savings[0]?.id)
          .sort((a,b) => new Date(a.date) - new Date(b.date))
        const arr = userTransactions?.map(transaction => transaction.if_saved)
        setTransactions(userTransactions);
        setCheckValues(arr);
        //console.log("this is transactions", transactions)
      }
    } catch (error) {
      console.log(error)
    }
  }

  useEffect(() => {
    if (token) {
      fetchSavings();
    }
  }, [token]);

  useEffect(() => {
    savings && savings.length > 0 && fetchTransactions();
  }, [savings]);

  // useEffect(() => {
  //   let arr = transactions?.map(transaction => transaction.if_saved)
  //   setCheckValues(arr);
  // }, [transactions]);

  // const handleInputChange = (i) => {
  //   const arr = [...checkValues.slice(0,i), !checkValues[i], ...checkValues.slice(i+1)]
  //   setCheckValues(arr)
  // }

  // useEffect(() => {
  //   handleIfSaved()
  // }, [checkValues])

  const handleIfSaved = async (transaction, i) => {
    const arr = [...checkValues.slice(0,i), !checkValues[i], ...checkValues.slice(i+1)]
    setCheckValues(arr)
    const transactionId = transaction.id
    console.log("transactionID", transactionId)
    console.log("before checkValues", checkValues)
    const data = {
      amount_saved: transaction.amount_saved,
      date: transaction.date,
      if_saved: transaction.if_saved ? false : true,
      savings_id: transaction.savings_id
    }
    console.log("data", data)
    try {
      const transactionURL = `http://localhost:8000/transactions/${transactionId}`;
      const response = await fetch(transactionURL, {
        method: "put",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${token}`,
        },
        body: JSON.stringify(data),
      });
      console.log("response of handleIfSaved outside", response)
      if (response.ok) {
        console.log("response of handleIfSaved inside", response)
        fetchTransactions();
        console.log("after checkValues", checkValues)
        //console.log("old transaction before loop, state", transactions)
        // const updatedTransactions = transactions.map((transaction) => {
        //   console.log("transaction before if statement", transaction)
        //   if (transaction.id === transactionId) {
        //     let updatedTransaction =  {
        //       ...transaction,
        //       if_saved: !ifSaved,
        //     }
        //     console.log("updated transaction in loop", updatedTransaction)
        //     return updatedTransaction;
        //   }
        //   return transaction;
        // });
        // console.log("updated", updatedTransactions)
        // setTransactions(updatedTransactions);
      }
    } catch (error) {
    // Handle errors
    } finally {
        //setIsLoading(false);
      }
  };

  return (
    <div className="shadow p-3 mt-4">
      <h1 style={{ fontSize: "64px" }}>Plan Details</h1>
      <h2>Savings for Plan {planId}</h2>
      <ul>
        {savings.map((saving) => (
          <li key={saving.id}>
            Current Amount Saved: {saving.current_amount_saved}<br />
            Final Goal Amount: {saving.final_goal_amount}<br />
          </li>
        ))}
      </ul>
      <h2>Transactions for Plan {planId}</h2>
      <ul>
        {transactions?.map((transaction, i) => (
          <li key={transaction.id}>
            ID: {transaction.id}
            Amount to Save: {transaction.amount_saved}<br />
            Date: {transaction.date}<br />
            If Saved:{" "}
            <div className="form-check form-switch">
              {checkValues.length > 0 && checkValues[i] ?
                <input checked onChange={() => handleIfSaved(transaction, i)}
                className="form-check-input" value={checkValues[i]} type="checkbox" id="flexSwitchCheckDefault"/>
                :
                <input onChange={() => handleIfSaved(transaction, i)}
                className="form-check-input" value={checkValues[i]} type="checkbox" id="flexSwitchCheckDefault"/>
              }
              {/* <input onChange={() => handleIfSaved(transaction, i)}
                className="form-check-input" value={checkValues[i]} type="checkbox" id="flexSwitchCheckDefault"/> */}
              <label className="form-check-label" htmlFor="flexSwitchCheckDefault"></label>
            </div>
            <br />
          </li>
        ))}
      </ul>
    </div>
  );
};
export default PlanDetail;
