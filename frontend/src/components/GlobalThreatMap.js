import React from 'react';
import { Map, Marker, Popup, TileLayer } from 'react-leaflet';

const GlobalThreatMap = ({ threats }) => {
  return (
    <Map center={[51.505, -0.09]} zoom={2} style={{ height: '400px', width: '100%' }}>
      <TileLayer
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        attribution="&copy; <a href='https://www.openstreetmap.org/copyright'>OpenStreetMap</a> contributors"
      />
      {threats.map(threat => (
        <Marker key={threat.id} position={[threat.latitude, threat.longitude]}>
          <Popup>{threat.description}</Popup>
        </Marker>
      ))}
    </Map>
  );
};

export default GlobalThreatMap;
