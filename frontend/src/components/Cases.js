import React, { useEffect, useState } from 'react';
import axios from 'axios';

const Cases = () => {
  const [cases, setCases] = useState([]);

  useEffect(() => {
    const fetchCases = async () => {
      const response = await axios.get('http://localhost:5000/cases');
      setCases(response.data);
    };
    fetchCases();
  }, []);

  return (
    <div>
      <h2>Security Cases</h2>
      <ul>
        {cases.map((caseItem) => (
          <li key={caseItem.case_id}>{caseItem.description} - Status: {caseItem.status}</li>
        ))}
      </ul>
    </div>
  );
};

export default Cases;
