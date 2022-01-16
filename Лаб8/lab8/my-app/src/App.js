import './App.css';

import { BrowserRouter, Route, Link, Switch } from "react-router-dom";

import page0 from "./page0.js";
import Page1 from "./page1.js";
import DP from "./pagedef.js";



function App() {
  return (
    <div>
      <BrowserRouter basename="/" >
        <div>
          <ul>
            <li>
              <Link to="/">Главная</Link>
            </li>
            <li>
              <Link to="/list">Перечень фильмов</Link>
            </li>
            <li>
              <Link to="/cat">Каталог фильмов</Link>
            </li>
          </ul>
          <hr />
          <Switch>
            <Route exact path='/' >
              <h1>Это главная страница.</h1>
              <h3>Для навигации воспользуйтесь ссылками сверху</h3>
            </Route>
            <Route path="/list" component={page0}/>
            <Route path="/cat" component={Page1} />
            <Route path="/detail" component={DP} />
          </Switch>
        </div>
      </BrowserRouter>
      </div>
  );
}

export default App;