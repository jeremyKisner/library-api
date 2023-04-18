import Book from './Book'
import React from 'react';

const Library = (props) => {
  return (
    <div>
      {props.books.map((data, index) => (
        <Book key={index} data={data} index={index} />
      ))}
    </div>
  );
};

export default Library;