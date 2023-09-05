import React from 'react';
import { NavLink } from 'react-router-dom';
import useToken from '@galvanize-inc/jwtdown-for-react';
import { Navbar, Nav, NavDropdown } from 'react-bootstrap';

function NavComponent() {
  const { token, logout, fetchWithToken } = useToken();

  function handleLogout() {
    logout();
    fetchWithToken('/logout');
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
                <NavDropdown.Item as={NavLink} to="/plans">Your Plans</NavDropdown.Item>
                <NavDropdown.Item as={NavLink} to="/plan/create">New Plan</NavDropdown.Item>
                <NavDropdown.Item as={NavLink} to="/expense/create">New Expense</NavDropdown.Item>
              </NavDropdown>
              <NavDropdown title="Journal" id="basic-nav-dropdown">
                <NavDropdown.Item as={NavLink} to="/journal">My Journal</NavDropdown.Item>
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



// function Nav() {
//   const { token } = useToken();

//   return (
//     <nav className="navbar navbar-expand-lg navbar-dark bg-success">
//       <div className="container-fluid">
//         <NavLink className="navbar-brand" to="/">TSA</NavLink>
//         <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
//           <span className="navbar-toggler-icon"></span>
//         </button>
//         <div className="collapse navbar-collapse" id="navbarSupportedContent">
//           <ul className="navbar-nav me-auto mb-2 mb-lg-0">
//             {token ? (
//               <>
//                 <li className="nav-item">
//                   <NavLink className="nav-link" aria-current="page" to="/" exact>Home</NavLink>
//                 </li>
//                 <li className="nav-item dropdown">
//                   <a className="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
//                     Travel Plans
//                   </a>
//                   <ul className="dropdown-menu" aria-labelledby="navbarDropdown">
//                     <li><NavLink className="dropdown-item" to="/plans">Your Plans</NavLink></li>
//                     <li><NavLink className="dropdown-item" to="/plan/create">New Plan</NavLink></li>
//                     <li><NavLink className="dropdown-item" to="/expense/create">New Expense</NavLink></li>
//                   </ul>
//                 </li>
//                 <li className="nav-item dropdown">
//                   <a className="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
//                     Journal
//                   </a>
//                   <ul className="dropdown-menu" aria-labelledby="navbarDropdown">
//                     <li><NavLink className="dropdown-item" to="/journal">My Journal</NavLink></li>
//                     <li><NavLink className="dropdown-item" to="/journal/create">Add Manufacturer</NavLink></li>
//                   </ul>
//                 </li>
//                 <li className="nav-item">
//                   <NavLink className="nav-link" to="/logout">Log Out</NavLink>
//                 </li>
//               </>
//             ) : (
//               <>
//                 <li className="nav-item">
//                   <NavLink className="nav-link" to="/Login">Login</NavLink>
//                 </li>
//                 <li className="nav-item">
//                   <NavLink className="nav-link" to="/Signup">Sign Up</NavLink>
//                 </li>
//               </>
//             )}
//           </ul>
//         </div>
//       </div>
//     </nav>
//   );
// }

export default NavComponent;
