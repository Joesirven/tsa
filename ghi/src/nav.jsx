import { NavLink } from 'react-router-dom';

function Nav() {
  return (
    <nav className="navbar navbar-expand-lg navbar-dark bg-success">
      <div className="container-fluid">
        <NavLink className="navbar-brand" to="/">CarCar</NavLink>
        <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span className="navbar-toggler-icon"></span>
        </button>
        <div className="collapse navbar-collapse" id="navbarSupportedContent">
        <ul className="navbar-nav me-auto mb-2 mb-lg-0">
            <li className="nav-item">
              <NavLink className="nav-link" aria-current="page" to="/" end>Home</NavLink>
            </li>

            <li className="nav-item dropdown">
                <a className="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                    Inventory
                </a>
                <ul className="dropdown-menu">
                    <li><NavLink className="dropdown-item" to="/manufacturers" end>View Manufacturers</NavLink></li>
                    <li><NavLink className="dropdown-item" to="/manufacturers/create" end>Add Manufacturer</NavLink></li>
                    <li><NavLink className="dropdown-item" to="/automobiles" end>View Automobiles</NavLink></li>
                    <li><NavLink className="dropdown-item" to="/automobiles/create" end>Add Automobiles</NavLink></li>
                    <li><NavLink className="dropdown-item" to="/vehicles" end>View Models</NavLink></li>
                    <li><NavLink className="dropdown-item" to="/vehicles/create" end>Add Models</NavLink></li>
                </ul>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  )
}

export default Nav;
