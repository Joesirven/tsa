import { BrowserRouter, Routes, Route, Navigate, Outlet, useLocation } from "react-router-dom";
import "./App.css";
import { AuthProvider } from '@galvanize-inc/jwtdown-for-react';
import useToken from "@galvanize-inc/jwtdown-for-react";
import NavComponent from "./Nav";
import LoginForm from './LoginForm';
import SignupForm from './SignupForm';
import HomePage from "./HomePage";
import PlanList from "./PlansList";
// import PlanDetail from "./PlanDetail";
import PlanCreate from "./PlanCreate";
import PlanEdit from "./PlanEdit";
import JournalList from "./JournalList";
// import JournalDetail from "./JournalDetail";
// import JournalCreate from "./JournalCreate";
// import JournalEdit from "./JournalEdit";
// import ExpenseCreate from "./ExpenseCreate";


function App() {
  const baseUrl = "http://localhost:8000"

  const ProtectedRoute = () => {
    const { token } = useToken();
    // const [loading, setLoading] = useState(true);
    const location = useLocation();
    // useEffect(() => {
    //   setLoading(false)},
    //   [token]
    // );

    if (!token) {
      return <Navigate to="/Login" replace state={{ from: location }} />;
    }
    return <Outlet />
  }

  return (
    <div className="container">
      <BrowserRouter>
        <AuthProvider baseUrl={baseUrl}>
          <NavComponent />
          <Routes>
            <Route path="/" element={<HomePage />}></Route>
            <Route path="/Signup" element={<SignupForm />}></Route>
            <Route path="/Login" element={<LoginForm />}></Route>
            <Route path="/plans" element={<ProtectedRoute />}>
              <Route index element={<PlanList />} />
              <Route path="create" element={<PlanCreate />} />
              <Route path=":id/edit" element={<PlanEdit />} />
              {/* <Route path=":id" element={<PlanDetail />} /> */}
            </Route>
            {/* <Route path="/expense" element={<ProtectedRoute />}>
              <Route path="create" element={<ExpenseCreate />} />
            </Route> */}
            <Route path="journal" element={<ProtectedRoute />}>
              <Route index element={<JournalList />} />
              {/* <Route path=":id" element={<JournalDetail />} />
              <Route path="create" element={<JournalCreate />} />
              <Route path=":id/edit" element={<JournalEdit />} /> */}
            </Route>
          </Routes>
        </AuthProvider>
      </BrowserRouter>
    </div>
  );
}

export default App;
