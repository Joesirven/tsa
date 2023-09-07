import { useState, useEffect } from "react";
import useToken from "@galvanize-inc/jwtdown-for-react";
import { useNavigate } from "react-router-dom";
import Alert from 'react-bootstrap/Alert';

const SignupForm = () => {
//   const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [first, setFirst] = useState("");
  const [last, setLast] = useState("");
  const [email, setEmail] = useState("");
  const { register } = useToken();
  const navigate = useNavigate();
  const [message, setMessage] = useState("");
  const [messageType, setMessageType] = useState("danger");
  const [click, setClick] = useState(false);
  const [error, setError] = useState(false);
  const { login, token } = useToken();

  useEffect(() => {
    if (token) {
      navigate("/plans");
    }
    if (!token && click) {
      setTimeout(function () {
        setError(true);
      }, 2000);
    }
  }, [token, click, navigate]);

  const handleRegistration = async (e) => {
    e.preventDefault();
    const accountData = {
      email: email,
      username: email,
      password: password,
      first_name: first,
      last_name: last,
    };
    try {
      setClick(true);
      await register(
      accountData,
      `${process.env.VITE_REACT_APP_API_HOST}/user/sign-up`
      );
      if (!token) {
        setMessage("You already have an account. Try logging in.");
        setMessageType("danger");
      } else {
        e.target.reset();
        setMessage("Account created successfully");
        setMessageType("success");
      }
    } catch (error) {
      setMessage("You already have an account. Try logging in.");
      setMessageType("danger");
    }
  };

  return (
    <div className="card text-bg-light mb-3">
      <h5 className="card-header">Signup</h5>
      <div className="card-body">
        {message && <Alert variant={messageType}>{message}</Alert>}
        <form onSubmit={(e) => handleRegistration(e)}>
          <div className="mb-3">
            <label className="form-label">First Name</label>
            <input
              name="first_name"
              type="text"
              className="form-control"
              onChange={(e) => {
                setFirst(e.target.value);
              }}
            />
          </div>
          <div className="mb-3">
            <label className="form-label">Last Name</label>
            <input
              name="last_name"
              type="text"
              className="form-control"
              onChange={(e) => {
                setLast(e.target.value);
              }}
            />
          </div>
          {/* <div className="mb-3">
            <label className="form-label">username</label>
            <input
              name="username"
              type="text"
              className="form-control"
              onChange={(e) => {
                setUsername(e.target.value);
              }}
            />
          </div> */}
          <div className="mb-3">
            <label className="form-label">Email</label>
            <input
              name="email"
              type="text"
              className="form-control"
              onChange={(e) => {
                setEmail(e.target.value);
              }}
            />
          </div>
          <div className="mb-3">
            <label className="form-label">Password</label>
            <input
              name="password"
              type="password"
              className="form-control"
              onChange={(e) => {
                setPassword(e.target.value);
              }}
            />
          </div>
          <div>
            <input className="btn btn-primary" type="submit" value="Register" />
          </div>
        </form>
      </div>
    </div>
  );
};

export default SignupForm;
