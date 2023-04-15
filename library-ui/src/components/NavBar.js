import React from 'react';

export default function NavBar() {
    return <nav className="nav">
        <a  href="/" className="library-app">Home</a>
        <ul>
            <li>
                <a href="/addBook">Add Book</a>
            </li>
            <li>
                <a href="/deleteBook">Delete Book</a>
            </li>
        </ul>
    </nav>
}