import { BrowserRouter, Routes, Route } from "react-router-dom";
import "./App.css";
import { AuthProvider } from "@galvanize-inc/jwtdown-for-react";
import LoginForm from "./LoginForm";
import SignupForm from "./SignupForm";
import HomePage from "./HomePage";
import PlanList from "./PlansList";
// import Login from "./Login";
// import Logout from "./Logout";
// import PlanDetail from "./PlanDetail";
import PlanCreate from "./PlanCreate";
import PlanEdit from "./PlanEdit";
import Journal from "./Journal";
import JournalDetail from "./JournalDetail";
import JournalCreate from "./JournalCreate";
// import JournalEdit from "./JournalEdit";
// import ExpenseCreate from "./ExpenseCreate";

function App() {
  const baseUrl = "http://localhost:8000";

  return (
    <div className="container">
      <BrowserRouter>
        <AuthProvider baseUrl={baseUrl}>
          <Routes>
            <Route path="/" element={<HomePage />}></Route>
            <Route path="/Signup" element={<SignupForm />}></Route>
            <Route path="/Login" element={<LoginForm />}></Route>
            <Route path="/plans" element={<PlanList />}></Route>
            {/* <Route path="/plan/{id}" element={<PlanDetail />}></Route> */}
            <Route path="/plan/create" element={<PlanCreate />}></Route>
            <Route path="/plan{id}/edit" element={<PlanEdit />}></Route>
            <Route path="/journal" element={<Journal />}></Route>
            <Route path="/journal/{id}" element={<JournalDetail />}></Route>
            <Route path="/journal/create" element={<JournalCreate />}></Route>
            {/* <Route path="/journal/{id}/edit" element={<JournalEdit />}></Route> */}
            {/* <Route path="/expense/create" element={<ExpenseCreate />}></Route> */}
          </Routes>
        </AuthProvider>
      </BrowserRouter>
    </div>
  );
}

export default App;
