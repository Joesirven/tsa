import { Navigate } from "react-router-dom";



function ProtectedRoute({ token, children }) {
    if (!token) {
    return <Navigate to="/Login" replace />;
  }
  return <>{children}</>;
  };


export default ProtectedRoute;
