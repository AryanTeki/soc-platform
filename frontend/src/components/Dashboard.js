import React from 'react';
import GlobalThreatMap from './GlobalThreatMap';
import Analytics from './Analytics';

const Dashboard = () => {
  return (
    <div>
      <h1>SOC Dashboard</h1>
      <GlobalThreatMap />
      <Analytics />
    </div>
  );
};

export default Dashboard; 