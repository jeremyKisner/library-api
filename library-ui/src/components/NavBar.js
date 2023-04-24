import React from 'react';

const NavBar = () => {
    return <nav className="nav">
        <a  href="/" className="library-app">Home</a>
        <ul>
            <li>
                <a href="/addBook">Add Book</a>
            </li>
            <li>
                <a href="/deleteBook">Delete Book</a>
            </li>
            <li>
                <a href="/cart">Cart</a>
            </li>
        </ul>
    </nav>
}

export default NavBar;
