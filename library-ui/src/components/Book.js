const Book = (data, index) => {
    return (
      <div className="book" key={index}>
        {data.data.name} <br/>
        {data.data.author} <br/>
        {data.data.published} <br/><br/>
        Copies Left: {data.data.copies} <br/>
      </div>
    )
  }

export default Book;
