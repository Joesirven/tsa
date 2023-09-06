import useToken from "@galvanize-inc/jwtdown-for-react";
import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import Alert from "react-bootstrap/Alert";

const LoginForm = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  // const [displayMessage, setMessage] = useState("alert alert-success d-none");
  const { login, token } = useToken();
  const navigate = useNavigate();
  const [click, setClick] = useState(false);
  const [error, setError] = useState(false);
  const [message, setMessage] = useState("");
  const [messageType, setMessageType] = useState("");

  useEffect(() => {
    if (token) {
      navigate("/plans");
      setError(false);
      setMessage("Login Successful");
      setMessageType("success");
    }
    if (!token && click) {
      setTimeout(function () {
        setError(true);
        setMessage("Password and Username do not match");
        setMessageType("danger");
      }, 2000);
    }
  }, [token, click, navigate]);

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!username || !password) {
      setError(true);
      setMessage("Password and Username cannot be blank.");
      setMessageType("danger");
      return
    }

    try {
      setClick(true);
      await login(username, password);
    } catch (error) {
      setError(true);
      setMessage("Cannot login. Try again.");
      setMessageType("danger");
    }
  };

  return (
    <div className="card text-bg-light mb-3">
      <h5 className="card-header">Login</h5>
      <div className="card-body">
        {message && <Alert variant={messageType}>{message}</Alert>}
        <form onSubmit={(e) => handleSubmit(e)}>
          <div className="mb-3">
            <label className="form-label">Email:</label>
            <input
              name="username"
              type="text"
              className="form-control"
              onChange={(e) => setUsername(e.target.value)}
            />
          </div>
          <div className="mb-3">
            <label className="form-label">Password:</label>
            <input
              name="password"
              type="password"
              className="form-control"
              onChange={(e) => setPassword(e.target.value)}
            />
          </div>
          <div>
            <input className="btn btn-primary" type="submit" value="Login" />
          </div>
        </form>
      </div>
    </div>
  );
};

export default LoginForm;
