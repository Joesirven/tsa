import React, { useState, useEffect } from 'react';
import { FetchWrapper } from './fetch-wrapper';

function TopDestinations() {
    const [destinations, setDestinations] = useState([]);
    const [query, setQuery] = useState('Top Destinations');

    const TripAdvisorAPI = new FetchWrapper('TRIP_ADVISOR_API_URL');
    const fetchDestinations = async () => {
        try {
            const response = await TripAdvisorAPI.get(`location/search?key=${REACT_APP_TRIP_ADVISOR_API_KEY}&searchQuery=${query}&language=en`);

            const destinationsWithImages = await Promise.all(
                response.data.map(async destination => {
                    const imgResponse = await TripAdvisorAPI.get(`location/${destination.location_id}/photos?key=${REACT_APP_TRIP_ADVISOR_API_KEY}&language=en`);
          destination.image_url = imgResponse.data[0]?.images?.thumbnail?.url || '';  // Use the thumbnail image or default to an empty string
          return destination;
        })
        } catch (error) {
            console.error(error);
        }
};

useEffect(() => {
    fetchDestinations();
}, [query]);

return (
    <div className="top-destinations">

        <div>
            <input type="text" placeholder="Search Destinations" value={query} onChange={(e) => setQuery(e.target.value)} />
        </div>
        <div>
            {destinations.map((destination) => (
            <div className="destination-card" key={destination.id}>
                <img src={destination.image_url} alt={destination.name} />
                <h3>{destination.name}</h3>
                <p>{destination.description}</p>
            </div>
            ))}
        </div>

    </div>
    );
}

export default TopDestinations;
