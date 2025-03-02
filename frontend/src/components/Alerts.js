import React, { useEffect, useState } from 'react';
import axios from 'axios';

const Alerts = () => {
  const [alerts, setAlerts] = useState([]);

  useEffect(() => {
    const fetchAlerts = async () => {
      const response = await axios.get('http://localhost:5000/alerts');
      setAlerts(response.data);
    };
    fetchAlerts();
  }, []);

  return (
    <div>
      <h2>Security Alerts</h2>
      <ul>
        {alerts.map((alert) => (
          <li key={alert.alert_id}>{alert.message} - Severity: {alert.severity}</li>
        ))}
      </ul>
    </div>
  );
};

export default Alerts;
