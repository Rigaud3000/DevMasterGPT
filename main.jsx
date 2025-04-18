import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';

const App = () => (
  <div className="h-screen flex items-center justify-center bg-black text-white">
    <div className="text-center">
      <h1 className="text-4xl font-bold text-[#E5E4E2]">DevMasterGPT</h1>
      <p className="mt-4 text-gray-400">Full-stack AI Coding Assistant</p>
      <a href="/api" className="mt-6 inline-block px-4 py-2 border border-[#E5E4E2] text-[#E5E4E2] hover:bg-[#E5E4E2] hover:text-black rounded">Try AI</a>
    </div>
  </div>
);

ReactDOM.createRoot(document.getElementById('root')).render(<App />);
