import Book from './Book'
import Grid from '@mui/material/Grid';

const Library = (props) => {
  console.log('this props', props);
  return (
    <>
      <h1>Library</h1>
      <Grid sx={{ flexGrow: 1 }} container spacing={2}>
        <Grid item xs={12}>
          <Grid container justifyContent="center" spacing={8}>
            {props.books.map((value, index) => (
              <Grid key={index} item>
                <Book key={index} data={value} index={index} addToCart={props.addToCart} />
              </Grid>
            ))}
          </Grid>
        </Grid>
      </Grid>
    </>
  );
};

export default Library;
