import './App.css';
import { useState } from "react";
import Navbar from './components/NavBar';
import AddBook from './pages/AddBook';
import Cart from './pages/Cart';
import DeleteBook from './pages/DeleteBook';
import Home from './pages/Home';
import {
  BrowserRouter as Router,
  Routes,
  Route,
} from "react-router-dom";


const App = () => {
  const [cart, updateCart] = useState([]);

  const addToCart = (item) => {
    cart.push(item);
    updateCart(cart);
    console.log("cart: ", cart);
  };

  return (
    <Router>
        <Navbar/>
        <Routes>
          <Route exact path="/" element={<Home cart={cart} addToCart={addToCart} />}/>
          <Route exact path="/addBook" element={<AddBook />}/>
          <Route exact path="/deleteBook" element={<DeleteBook />}/>
          <Route exact path="/cart" element={<Cart cart={cart} />}/>
          <Route path="*" element={<Home cart={cart} addToCart={addToCart} />}/>
        </Routes>
    </Router>
  )
}

export default App;
