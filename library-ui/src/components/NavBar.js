import React from 'react';
import { Link } from "react-router-dom";

const NavBar = () => {
    return <nav className="nav">
        <a href="/" className="library-app">Home</a>
        <ul>
            <li>
                <Link to="/">Home</Link>
            </li>
            <li>
                <Link to="/addBook">Add Book</Link>
            </li>
            <li>
                <Link to="/deleteBook">Delete Book</Link>
            </li>
            <li>
                <Link to="/cart">Cart</Link>
            </li>
        </ul>
    </nav>
}

export default NavBar;
