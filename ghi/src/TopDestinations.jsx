import React, { useState, useEffect } from 'react';
import { FetchWrapper } from './fetch-wrapper';

const apiKey = import.meta.env.VITE_REACT_APP_TRIP_ADVISOR_API_KEY;
const apiUrl = import.meta.env.VITE_TRIP_ADVISOR_API_URL;


function TopDestinations() {
    const [destinations, setDestinations] = useState([]);
    const [query, setQuery] = useState('Top%20Destinations');

    const TripAdvisorAPI = new FetchWrapper(apiUrl);
    const fetchDestinations = async () => {
        try {

            const options = {method: 'GET', headers: {accept: 'application/json'}, mode: 'no-cors',};
            // const response = await TripAdvisorAPI.get(`location/search?key=${apiKey}&searchQuery=${query}&language=en`, options);
            const url = 'https://api.content.tripadvisor.com/api/v1/location/search?key=33C0B234F7EF4430BC66021940821F3B&searchQuery=Top%20Destinations&language=en';
            let response = {}
            fetch(url, options)
                .then(res => res.json())
                .then(json => response = json)
                .catch(err => console.error('error:' + err));
            console.log(response)
            const destinationsWithImages = await Promise.all(
                response.data.map(async destination => {
                    const imgResponse = await TripAdvisorAPI.get(`location/${destination.location_id}/photos?key=${apiKey}&language=en`);
          destination.image_url = imgResponse.data[0]?.images?.thumbnail?.url || '';
        })
        );
        setDestinations(destinationsWithImages);
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
                <p>{destination.address_obj?.address_string || ''}</p>
            </div>
            ))}
        </div>

    </div>
    );
}

export default TopDestinations;
