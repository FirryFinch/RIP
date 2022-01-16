import React from "react";
import './page1.css';
import {Button, Card, Col, Row} from "react-bootstrap";
class Page2 extends React.Component {

    // Constructor
    numb;
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
        this.numb = localStorage.getItem("key");
        console.log("Внимание", this.numb);
        const { DetailsLoaded, items } = this.state;
        if (!DetailsLoaded) return <div>
            <h1> Загрузка... </h1> </div> ;

        return (
            <div className = "App">
                <h1>Информация о фильме</h1>  {
                <Row xs={4} md={4} className="g-4">
                    {items.map((item, index)=>{
                        if(item.pk==this.numb)
                        return<Col >
                            <Card key={index} className="card">
                                <Card.Img className="cardImage" variant="top" src={item.pic} width={200} height={300}  />
                                <Card.Body>
                                    <div className="textStyle">
                                        <Card.Title>{item.name}</Card.Title>
                                    </div>
                                    <div  className="textStyle">
                                        <Card.Text>
                                            {item.description},
                                        </Card.Text>
                                        <Card.Text> 
                                            Рейтинг: {item.rating}
                                        </Card.Text>
                                    </div>
                                </Card.Body>
                            </Card>
                        </Col>
                    })}
                </Row>
            }
            </div>
        );
    }
}

export default Page2;