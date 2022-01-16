import React from "react";
import './App.css';
class page0 extends React.Component {

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
        const { DetailsLoaded, items } = this.state;
        if (!DetailsLoaded) return <div>
            <h1> Загрузка... </h1> </div> ;

        return (
            <div className = "App">
                <h1>Перечень фильмов</h1>  {
                items.map((item) => (
                    <ol key = { item.pk } >
                       {item.name}
                    </ol>
                ))
            }
            </div>
        );
    }
}

export default page0;