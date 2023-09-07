import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import "./App.css";
import { AuthProvider } from '@galvanize-inc/jwtdown-for-react';
import useToken from "@galvanize-inc/jwtdown-for-react";
// import useToken from "@galvanize-inc/jwtdown-for-react";
import NavComponent from "./Nav";
import LoginForm from './LoginForm';
import SignupForm from './SignupForm';
import HomePage from "./HomePage";
import PlanList from "./PlansList";
// import PlanDetail from "./PlanDetail";
import PlanCreate from "./PlanCreate";
import PlanEdit from "./PlanEdit";
import JournalList from "./JournalList";
import JournalDetail from "./JournalDetail";
import JournalCreate from "./JournalCreate";
// import ExpenseCreate from "./ExpenseCreate";


function App() {
  const baseUrl = "http://localhost:8000"
  function ProtectedRoute({ children }) {
    const { token } = useToken();
    if (!token) {
      return <Navigate to="/Login" replace />;
    }
    return <>{children}</>;
  };

  return (
    <div className="container">
      <BrowserRouter>
        <AuthProvider baseUrl={baseUrl}>
          <NavComponent />
          <Routes>
            <Route path="/" element={<HomePage />}></Route>
            <Route path="/Signup" element={<SignupForm />}></Route>
            <Route path="/Login" element={<LoginForm />}></Route>
            <Route path="/plans">
              <Route index element={<ProtectedRoute><PlanList /></ProtectedRoute>} />
              <Route path="create" element={<ProtectedRoute><PlanCreate /></ProtectedRoute>} />
              <Route path=":id/edit" element={<ProtectedRoute><PlanEdit /></ProtectedRoute>} />
              {/* <Route path=":id" element={<ProtectedRoute><PlanDetail /></ProtectedRoute>} /> */}
            </Route>
            {/* <Route path="/expense">
              <Route path="create" element={<ProtectedRoute><ExpenseCreate /></ProtectedRoute>} />
            </Route>*/}
            <Route path="journal">
              <Route index element={<ProtectedRoute><JournalList /></ProtectedRoute>} />
              <Route path=":id" element={<ProtectedRoute><JournalDetail /></ProtectedRoute>} />
              <Route path="create" element={<ProtectedRoute><JournalCreate /></ProtectedRoute>} />
              {/* <Route path=":id/edit" element={<ProtectedRoute><JournalEdit /></ProtectedRoute>} /> */}
            </Route> 
          </Routes>
        </AuthProvider>
      </BrowserRouter>
    </div>
  );
}

export default App;
