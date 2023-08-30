import { BrowserRouter, Routes, Route } from "react-router-dom";
import "./App.css";
import { AuthProvider } from '@galvanize-inc/jwtdown-for-react'
import LoginForm from './LoginForm'
import SignupForm from './SignupForm'
import Home from "./home";
import PlanList from "./PlansList";
// import Login from "./Login";
// import Logout from "./Logout";
// import PlanDetail from "./PlanDetail";
// import PlanCreate from "./PlanCreate";
// import PlanEdit from "./PlanEdit";
// import Journal from "./Journal";
// import JournalDetail from "./JournalDetail";
// import JournalCreate from "./JournalCreate";
// import JournalEdit from "./JournalEdit";
// import ExpenseCreate from "./ExpenseCreate";

function App() {
  const baseUrl = "http://localhost:8000"

  return (
    <AuthProvider baseUrl={baseUrl}>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/Signup" element={<SignupForm />} />
          <Route path="/Login" element={<LoginForm />} />
          <Route path="/plans" element={<PlanList />} />
          {/* <Route path="/plan/{id}" element={<PlanDetail />} />
          <Route path="/plan/create" element={<PlanCreate />} />
          <Route path="/plan{id}/edit" element={<PlanEdit />} />
          <Route path="/journal" element={<Journal />} />
          <Route path="/journal/{id}" element={<JournalDetail />} />
          <Route path="/journal/create" element={<JournalCreate />} />
          <Route path="/journal/{id}/edit" element={<JournalEdit />} />
          <Route path="/expense/create" element={<ExpenseCreate />} /> */}
        </Routes>
      </BrowserRouter>
    </AuthProvider>
  );
}

export default App;


// import './App.css'
// import { AuthProvider } from '@galvanize-inc/jwtdown-for-react'
// import LoginForm from './LoginForm'
// import SignupForm from './SignupForm'
// import { Sign } from "crypto";

// function App() {
//   const baseUrl = "http://localhost:8000"

//   return (
//     <>
//       <AuthProvider baseUrl={baseUrl}>
//         <SignupForm />
//         <LoginForm />
//       </AuthProvider>
//     </>
//  )
// }

// export default App
