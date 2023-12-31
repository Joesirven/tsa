import React from 'react';
import Card from 'react-bootstrap/Card';
import Button from 'react-bootstrap/Button';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import './App.css'
import { NavLink } from 'react-router-dom';
import { FaChevronLeft, FaChevronRight } from "react-icons/fa";

const HomePage = () => {

  const destinations = [
  {
    title: "Yellowstone National Park",
    imgSrc: "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/1c/cf/f9/eb/caption.jpg?w=1400&h=-1&s=1&cx=941&cy=299&chk=v1_18cfa51ea9b832b15689",
    description: "Bison roam, geysers mist, and hundreds of hot springs explode in America's first National Park",
    tripAdvisorLink: "https://www.tripadvisor.com/Tourism-g60999-Yellowstone_National_Park_Wyoming-Vacations.html"
  },
  {
    title: "Punta Cana, Dominican Republic",
    imgSrc: "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/1c/c2/7b/93/caption.jpg?w=1400&h=-1&s=1",
    description: "Picture-perfect beaches and pampering all-inclusives are only part of Punta Cana’s allure",
    tripAdvisorLink: "https://www.tripadvisor.com/Tourism-g147293-Punta_Cana_La_Altagracia_Province_Dominican_Republic-Vacations.html"
  },
  {
    title: "Orlando, FL",
    imgSrc: "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/29/c7/b5/3d/caption.jpg?w=600&h=300&s=1&cx=2723&cy=2127&chk=v1_c3045329cb9c8cc38fca",
    description: "Make your dreams come true in the Theme Park Capital of the World.",
    tripAdvisorLink: "https://www.tripadvisor.com/Tourism-g34515-Orlando_Florida-Vacations.html"
  },{
    title: "Sedona, AZ",
    imgSrc: "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/21/66/c1/04/caption.jpg?w=1200&h=-1&s=1&cx=1419&cy=1192&chk=v1_dfebacd25b15bec181fe",
    description: "Glowing red rocks, clear blue skies, and the most eye-popping sunsets you’ve ever seen.",
    tripAdvisorLink: "https://www.tripadvisor.com/Tourism-g31352-Sedona_Arizona-Vacations.html"
  },
  {
    title: "Cancun, Mexico",
    imgSrc: "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/1c/ae/5d/ec/caption.jpg?w=1400&h=900&s=1",
    description: "Cancun’s a pretty well-known spot for spring breakers (and spring breakers at heart)—but its fun-loving spirit, miles of resorts, and nonstop nightlife is only one small part of the story. ",
    tripAdvisorLink: "https://www.tripadvisor.com/Tourism-g150807-Cancun_Yucatan_Peninsula-Vacations.html"
  },
  {
    title: "New York City, NY",
    imgSrc: "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/1c/c5/7c/68/caption.jpg?w=1600&h=1100&s=1&cx=950&cy=1766&chk=v1_9ee2771da71f55a7ac6a",
    description: "Come for the big dreams and dazzling lights, stay for the local haunts and the world’s best pizza",
    tripAdvisorLink: "https://www.tripadvisor.com/Tourism-g60763-New_York_City_New_York-Vacations.html"
  },
  {
    title: "Las Vegas, NV",
    imgSrc: "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/2a/34/2d/28/caption.jpg?w=1600&h=-1&s=1&cx=662&cy=604&chk=v1_8984ddf3493edfb8c896",
    description: "Whatever you can dream up, Las Vegas delivers: Michelin-starred restaurants, 24-hour wedding chapels, larger-than-life scenery, slot machines, all of it.",
    tripAdvisorLink: "https://www.tripadvisor.com/Tourism-g45963-Las_Vegas_Nevada-Vacations.html"
  },
  {
    title: "Yosemite National Park",
    imgSrc: "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/1c/cf/fa/42/caption.jpg?w=1600&h=-1&s=1",
    description: "Travel from river valley to alpine peak in this wonderland for hiking, climbing, and camping",
    tripAdvisorLink: "https://www.tripadvisor.com/Tourism-g61000-Yosemite_National_Park_California-Vacations.html"
  },
  {
    title: "London, UK",
    imgSrc: "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/15/33/f5/de/london.jpg?w=1600&h=1100&s=1",
    description: "A regal city surrounded by a rush of modern life",
    tripAdvisorLink: "https://www.tripadvisor.com/Tourism-g186338-London_England-Vacations.html"
  },
  ];

  const scrollRef = React.useRef(null);

  const scrollBy = (amount) => {
    if (scrollRef.current) {
      scrollRef.current.scrollBy({ left: amount, behavior: 'smooth' });
    }
  };

  return (
    <Container>
      <Row className="hero-section">
        <Col
          className="d-flex flex-column align-items-start justify-content-center hero-overlay"
          style={{ backgroundImage: `url(https://dynamic-media-cdn.tripadvisor.com/media/photo-o/1c/ae/5d/ec/caption.jpg?w=1400&h=900&s=1)`, backgroundSize: 'cover' }}
          xs={12}
        >
          <h1 className="text-white mb-3">Plan your dream vacation</h1>
          <NavLink to="/plans/create">
            <Button className="mx-auto d-block">Get started</Button>
          </NavLink>
        </Col>
      </Row>

      <Row className="mt-5">
        <Col xs={12} lg={12} className="carousel-with-nav">
          <FaChevronLeft className="carousel-nav-icon left" onClick={() => scrollBy(-300)} />
          <div className="carousel-container" ref={scrollRef}>
            {destinations.map((destination, index) => (
              <div key={index} className="carousel-card">
                <Card>
                  <Card.Img className="carousel-card-img" variant="top" src={destination.imgSrc} />
                  <Card.Body>
                    <Card.Title>{destination.title}</Card.Title>
                    <Card.Text>
                      {destination.description}
                    </Card.Text>
                    <Button variant="primary" href={destination.tripAdvisorLink} target="_blank" rel="noopener noreferrer">Learn More</Button>
                  </Card.Body>
                </Card>
              </div>
            ))}
          </div>
          <FaChevronRight className="carousel-nav-icon right" onClick={() => scrollBy(300)} />
        </Col>
      </Row>
    </Container>
  );
};

export default HomePage;
