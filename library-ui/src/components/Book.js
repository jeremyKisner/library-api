import { Typography } from "@mui/material";
import Button from '@mui/material/Button';
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';


const sendCheckout = async (book) => {
  console.log("sending request")
  await fetch(`http://127.0.0.1:5000/books/checkout`, {
    method: `POST`,
    headers: { "Content-Type": `application/json` },
    body: JSON.stringify(book)
  });
};

const Book = (book) => {
  onclick = () => {
    sendCheckout(book.data.library_id);
  };
  return (
    <Card
      sx={{
        height: 150,
        width: 150,
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
          Copies Left: {book.data.copies}
        </Typography>
        <CardActions>
          <Button size="small" onClick={onclick}>Checkout</Button>
        </CardActions>
      </CardContent>
    </Card>
  )
}


export default Book;
