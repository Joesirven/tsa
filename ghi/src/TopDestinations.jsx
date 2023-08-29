import React, { useState, useEffect } from 'react';
import { FetchWrapper } from './fetch-wrapper';

function TopDestinations({ query }) {
    const [destinations, setDestinations] = useState([]);

    const TripAdvisorAPI = new FetchWrapper('TRIP_ADVISOR_API_URL');
    const fetchDestinations = async () => {
        try {
            const response = await TripAdvisorAPI.get('?query=${query}');
            setDestinations(response);
        } catch (error) {
            console.error(error);
        }
};

useEffect(() => {
    fetchDestinations();
}, [query]);

return (
    <div className="top-destinations">
        {destinations.map((destination) => (
            <div className="destination-card" key={destination.id}>
                <img src={destination.image_url} alt={destination.name} />
                <h3>{destination.name}</h3>
                <p>{destination.description}</p>
            </div>
        ))}
    </div>
    );
}

export default TopDestinations;
