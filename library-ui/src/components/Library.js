import { useState } from "react";
import Book from './Book'
import Grid from '@mui/material/Grid';

const Library = (props) => {
  const [cart, updateCart] = useState([]);

  const addToCart = (item) => {
    console.log("Adding to cart!");
    updateCart(item);
    console.log("cart: ", cart);
  };

  return (
    <Grid sx={{ flexGrow: 1 }} container spacing={2}>
      <Grid item xs={12}>
        <Grid container justifyContent="center" spacing={8}>
          {props.books.map((value, index) => (
            <Grid key={index} item>
              <Book key={index} data={value} index={index} addToCart={addToCart}/>
            </Grid>
          ))}
        </Grid>
      </Grid>
    </Grid>
  );
};

export default Library;
