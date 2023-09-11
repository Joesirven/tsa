import React from "react";
// import { Link } from "react-router-dom";
// import TopDestinations from "./TopDestinations";
import Carousel from 'react-bootstrap/Carousel';
import Card from 'react-bootstrap/Card';
import Button from 'react-bootstrap/Button';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import './App.css'


const HomePage = () => {
    return (
        <Container fluid>
            <Row className="hero-section">
                <Col
                    className="d-flex justify-content-center align-items-start hero-overlay"
                    style={{ backgroundImage: `url(YOUR_LARGE_IMAGE_URL)`, backgroundSize: 'cover' }}
                    xs={12}
                >
                    <h1 className="text-center">Plan your dream vacation</h1>
                    <Button className="mx-auto d-block">Create a Plan</Button>
                </Col>
            </Row>

            <Row className="mt-5">
                <Col xs={12}>
                    <Carousel className="destination-carousel">
                        {/* Example card, repeat this structure for each destination */}
                        {[...Array(10)].map((_, index) => (
                            <Carousel.Item key={index}>
                                <Card className="mx-auto" style={{ width: '18rem' }}>
                                    <Card.Img variant="top" src="YOUR_DESTINATION_IMAGE_URL" />
                                    <Card.Body>
                                        <Card.Title>Destination Title</Card.Title>
                                        <Card.Text>
                                            Brief description for the destination.
                                        </Card.Text>
                                        <Button variant="info" href="TRIPADVISOR_URL">View on TripAdvisor</Button>
                                    </Card.Body>
                                </Card>
                            </Carousel.Item>
                        ))}
                    </Carousel>
                </Col>
            </Row>
        </Container>
    );
};

export default HomePage;


// function HomePage() {
//   return (
//     <div className="home-page">
//       <h1>Travel Saver App</h1>
//       <h2>Yes, you can take that trip you've always dreamed of.</h2>
//       <TopDestinations />
//       <Link to="plans">Plan List</Link>
//     </div>
//   );
// }

// export default HomePage;
