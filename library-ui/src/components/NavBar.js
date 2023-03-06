import React from 'react';

export default function NavBar() {
    return <nav className="nav">
        <a  href="/" className="library-app">Library</a>
        <ul>
            <li>
                <a href="/addBook">Add Book</a>
            </li>
        </ul>
    </nav>
}