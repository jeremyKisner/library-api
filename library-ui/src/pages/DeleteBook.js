import React, { useState } from "react";


const DeleteBook = (props) => {
  const [inputs, setInputs] = useState({});

  const handleChange = (event) => {
    const name = event.target.name;
    const value = event.target.value;
    console.log('values: ', value);
    setInputs(values => ({ ...values, [name]: value }))
  }

  const handleSubmit = (event) => {
    event.preventDefault();
    console.log(inputs);
    fetch('http://127.0.0.1:5000/books/delete', {
      method: 'POST',
      mode: 'cors',
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(inputs)
    })
  }

  return (
    <form onSubmit={handleSubmit}>
      <label>ISBN-13:
        <input
          type="text"
          name="isbn_13"
          value={inputs.isbn_13 || ""}
          onChange={handleChange}
        />
        <br />
      </label>
      <input type="submit" />
    </form>
  )
}

export default DeleteBook;
