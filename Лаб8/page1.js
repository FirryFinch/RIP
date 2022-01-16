import React from "react";
import './page1.css';
import {Button, Card, Col, Row} from "react-bootstrap";
import BrowserRouter from "react-router-dom/es/BrowserRouter";


class Page1 extends React.Component {
    numb;
    Open(numb) {
        localStorage.setItem("key", 8)
        window.open("/detail", "_blank")
    }

    // Constructor
    constructor(props) {
        super(props);

        this.state = {
            items: [],
            DetailsLoaded: false
        };
    }
    // ComponentDidMount is used to
    // execute the code
    componentDidMount() {
        fetch(
            "http://127.0.0.1:8000/movies/")
            .then((res) => res.json())
            .then((json) => {
                this.setState({
                    items: json,
                    DetailsLoaded: true
                });
            })
    }

    render() {
        const {DetailsLoaded, items} = this.state;
        if (!DetailsLoaded) return <div>
            <h1> Загрузка... </h1></div>;

        return (
            <BrowserRouter basename="/cat">

                <div className="App">
                    <h1> Каталог фильмов</h1>  {
                    <Row xs={4} md={4} className="g-4">
                        {items.map((item, index) => {
                            return <Col>
                                <Card key={index} className="card">
                                    <Card.Img className="cardImage" variant="top" src={item.pic} width={150} height={200}/>
                                    <Card.Body>
                                        <div className="textStyle">
                                            <Card.Title>{item.name}</Card.Title>
                                        </div>
                                        <Button className="cardButton" onClick={() => this.handleRegionClick(item.pk)}>Открыть</Button>
                                    </Card.Body>
                                </Card>
                            </Col>
                        })}
                    </Row>
                }
                </div>
            </BrowserRouter>
        );
    }


    handleRegionClick(id) {
        localStorage.setItem("key", id)
        window.open("/detail", "_blank")
    }
}

export default Page1;