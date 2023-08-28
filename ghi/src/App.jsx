import { BrowserRouter, Routes, Route } from "react-router-dom";
import "./App.css";

import Home from "./home";
import PlanList from "./PlansList";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/plans" element={<PlanList />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
