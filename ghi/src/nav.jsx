import React from 'react';
import { NavLink } from 'react-router-dom';
import useToken from '@galvanize-inc/jwtdown-for-react';
import { Navbar, Nav, NavDropdown } from 'react-bootstrap';
import { useNavigate } from 'react-router-dom';

function NavComponent() {
  const { token, logout, } = useToken();
  // const navigate = useNavigate();

  function handleLogout() {
    logout();
    // navigate("/");
  }

  return (
    <Navbar bg="success" expand="lg">
      <Navbar.Brand as={NavLink} to="/">TSA</Navbar.Brand>
      <Navbar.Toggle aria-controls="basic-navbar-nav" />
      <Navbar.Collapse id="basic-navbar-nav">
        <Nav className="me-auto">
          {token ? (
            <>
              <Nav.Link as={NavLink} to="/" exact>Home</Nav.Link>
              <NavDropdown title="Travel Plans" id="basic-nav-dropdown">
                <NavDropdown.Item as={NavLink} to="/plans">My Plans</NavDropdown.Item>
                <NavDropdown.Item as={NavLink} to="/plan/create">New Plan</NavDropdown.Item>
                <NavDropdown.Item as={NavLink} to="/expense/create">New Expense</NavDropdown.Item>
              </NavDropdown>
              <NavDropdown title="Travel Journals" id="basic-nav-dropdown">
                <NavDropdown.Item as={NavLink} to="/journal">My Journals</NavDropdown.Item>
                <NavDropdown.Item as={NavLink} to="/journal/create">New Entry</NavDropdown.Item>
              </NavDropdown>
              <Nav.Link as={NavLink} onClick={handleLogout}>Log Out</Nav.Link>
            </>
          ) : (
            <>
              <Nav.Link as={NavLink} to="/Login">Login</Nav.Link>
              <Nav.Link as={NavLink} to="/Signup">Sign Up</Nav.Link>
            </>
          )}
        </Nav>
      </Navbar.Collapse>
    </Navbar>
  );
}

export default NavComponent;
