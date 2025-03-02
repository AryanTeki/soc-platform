import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Line } from 'react-chartjs-2';

const Analytics = () => {
  const [historicalData, setHistoricalData] = useState([]);
  const [forecastData, setForecastData] = useState([]);

  useEffect(() => {
    const fetchHistoricalData = async () => {
      const response = await axios.get('http://localhost:5000/threats');
      setHistoricalData(response.data);
    };
    fetchHistoricalData();
  }, []);

  const handleForecast = async () => {
    const response = await axios.post('http://localhost:5000/forecast', { data: historicalData });
    setForecastData(response.data);
  };

  const data = {
    labels: historicalData.map(item => item.timestamp),
    datasets: [
      {
        label: 'Historical Data',
        data: historicalData.map(item => item.value),
        borderColor: 'blue',
        borderWidth: 1,
        fill: false,
      },
      {
        label: 'Forecast Data',
        data: forecastData,
        borderColor: 'red',
        borderWidth: 1,
        fill: false,
        borderDash: [5, 5],
      },
    ],
  };

  return (
    <div>
      <h1>Analytics Page</h1>
      <button onClick={handleForecast}>Get Forecast</button>
      <Line data={data} />
    </div>
  );
};

export default Analytics; 