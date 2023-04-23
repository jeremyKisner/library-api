import Book from './Book'
import React from 'react';
import Grid from '@mui/material/Grid';

const Library = (props) => {
  return (
    <Grid sx={{ flexGrow: 1 }} container spacing={2}>
      <Grid item xs={12}>
        <Grid container justifyContent="center" spacing={8}>
          {props.books.map((value, index) => (
            <Grid key={index} item>
              <Book key={index} data={value} index={index} />
            </Grid>
          ))}
        </Grid>
      </Grid>
    </Grid>
  );
};

export default Library;