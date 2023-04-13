import './App.css';
import React from 'react'
import Navbar from './components/NavBar';
import AddBook from './pages/AddBook';
import DeleteBook from './pages/DeleteBook';
import Home from './pages/Home';


function App() {
  let component
  switch (window.location.pathname) {
    case "/":
      component = <Home />
      break
    case "/addBook":
      component = <AddBook />
      break
    case "/deleteBook":
      component = <DeleteBook />
      break
    default:
      component = <Home />
  }
  return (
    <>
      <Navbar />
      {component}
    </>
  )
}

export default App;
