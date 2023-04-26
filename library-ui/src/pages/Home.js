import Library from '../components/Library'
import React, { useState, useEffect } from 'react';

const Home = (props) => {
    const [books, setBooks] = useState([]);

    useEffect(() => {
      var req = new XMLHttpRequest();
      req.addEventListener("load", () => {
        var data = req.responseText;
        data = JSON.parse(data);
        console.log("data: ", data);
        setBooks(data);
      });
      req.open("GET", "http://127.0.0.1:5000/books");
      req.send();
    }, []);

    return (
        <>
            <Library books={books} cart={props.cart} addToCart={props.addToCart}/>
        </>
    );
}

export default Home;