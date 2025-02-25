import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import InvestorTable from './pages/InvestorTable';
import Commitments from './pages/Commitments';

const App: React.FC = () => {
  return (
    <BrowserRouter>
      <div className="App">
        <Routes>
          {/* Main page route */}
          <Route path="/" element={<InvestorTable />} />

          {/* Details page route with dynamic `id` parameter */}
          <Route path="/details" element={<Commitments />} />
        </Routes>
      </div>
    </BrowserRouter>
  );
};

export default App;