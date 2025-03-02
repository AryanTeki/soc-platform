import React from 'react';

const ThreatCard = ({ threat }) => {
  return (
    <div className="threat-card">
      <h3>{threat.title}</h3>
      <p>Severity: {threat.severity}</p>
      <p>Description: {threat.description}</p>
      <p>Status: {threat.status}</p>
    </div>
  );
};

export default ThreatCard;
