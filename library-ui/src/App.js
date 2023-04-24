import './App.css';
import React from 'react'
import Navbar from './components/NavBar';
import AddBook from './pages/AddBook';
import Cart from './pages/Cart';
import DeleteBook from './pages/DeleteBook';
import Home from './pages/Home';


const App = () => {
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
      case "/cart":
        component = <Cart />
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
