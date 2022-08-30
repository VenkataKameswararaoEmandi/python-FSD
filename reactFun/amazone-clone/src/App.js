import React from "react";
import CountNum from "./counter";
import DispSqu from "./squares";

function App() {
  return (
    <div className="App">
      <Person name="Venkata" price="21" />
      <Person name="Kamesh" price="21" />
    </div>
  );
}

function Person(props) {
  return (
    <div className="person">
      <h1>{props.name}</h1>
      <p>price: {props.price}</p>
    </div>
  );
}

export default App;
