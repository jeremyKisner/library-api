import './App.css';
import { useState } from "react";
import Navbar from './components/NavBar';
import AddBook from './pages/AddBook';
import Cart from './pages/Cart';
import DeleteBook from './pages/DeleteBook';
import Home from './pages/Home';


const App = () => {
  const [cart, updateCart] = useState([]);

  const addToCart = (item) => {
    cart.push(item);
    updateCart(cart);
    console.log("cart: ", cart);
  };

  let component
  switch (window.location.pathname) {
    case "/":
      component = <Home cart={cart} addToCart={addToCart} />
      break
    case "/addBook":
      component = <AddBook />
      break
    case "/deleteBook":
      component = <DeleteBook />
      break
      case "/cart":
        component = <Cart cart={cart} />
        break
    default:
      component = <Home cart={cart} addToCart={addToCart} />
  }
  return (
    <>
      <Navbar />
      {component}
    </>
  )
}

export default App;
