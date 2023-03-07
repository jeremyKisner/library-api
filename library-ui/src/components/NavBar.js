import React from 'react';

export default function NavBar() {
    return <nav className="nav">
        <a  href="/" className="library-app">Library Home</a>
        <ul>
            <li>
                <a href="/addBook">Add</a>
            </li>
        </ul>
    </nav>
}