import { Routes, Route } from "react-router-dom";
import Home from "./pages/Home";
import Planner from "./pages/Planner";

function App() {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/planner" element={<Planner />} />
    </Routes>
  );
}

export default App;