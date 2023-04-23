import { Typography } from "@mui/material";
import Button from '@mui/material/Button';
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import { useState } from "react";


const sendCheckout = async (book) => {
  await fetch(`http://127.0.0.1:5000/books/checkout`, {
    method: `POST`,
    headers: { "Content-Type": `application/json` },
    body: JSON.stringify(book)
  });
};

const Book = (book) => {
  const [numOfCopies, setCopies] = useState(book.data.copies);
  const onclick = () => {
    sendCheckout(book.data.library_id);
    var target = numOfCopies - 1;
    if (target < 0) {
      target = 0;
    }
    setCopies(target);
  };
  return (
    <Card
      sx={{
        height: 250,
        width: 250,
        backgroundColor: (theme) =>
          theme.palette.mode === 'dark' ? '#1A2027' : '#fff',
      }}
    >
      <CardContent >
        <Typography>
          {book.data.name}
        </Typography>
        <Typography>
          {book.data.author}
        </Typography>
        <Typography>
          Copies Left: {numOfCopies}
        </Typography>
        <CardActions>
          <Button size="small" onClick={onclick}>Checkout</Button>
        </CardActions>
      </CardContent>
    </Card>
  )
}


export default Book;
