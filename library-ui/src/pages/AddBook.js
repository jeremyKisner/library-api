import React, { useState } from "react";

export default function AddBook() {
    const [inputs, setInputs] = useState({});

    const handleChange = (event) => {
      const name = event.target.name;
      const value = event.target.value;
      console.log('values: ', value)
      setInputs(values => ({...values, [name]: value}))
    }
  
    const handleSubmit = (event) => {
      event.preventDefault();
      console.log("here");
      console.log(inputs);
      fetch('http://127.0.0.1:5000/books/add', {
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
        <label>Book Name:
        <input 
            type="text" 
            id="name" 
            name="name"
            value={inputs.name || ""}
            onChange={handleChange}
        />
        </label>
        <label>Author Name:
          <input 
            type="text" 
            name="author" 
            value={inputs.author || ""} 
            onChange={handleChange}
          />
          </label>
          <label>Publisher:
          <input 
            type="text" 
            name="publisher" 
            value={inputs.publisher || ""} 
            onChange={handleChange}
          />
          </label>
          <br/><br/>
          <label>Year Published:
          <input
            type="text" 
            name="published" 
            value={inputs.published || ""} 
            onChange={handleChange}
          />
          <br/>
          </label>
          <label>ISBN-13:
          <input
            type="text" 
            name="isbn_13" 
            value={inputs.isbn_13 || ""} 
            onChange={handleChange}
          />
          <br/>
          </label>
          <label>ISBN-10:
          <input
            type="text" 
            name="isbn_10" 
            value={inputs.isbn_10 || ""} 
            onChange={handleChange}
          />
          </label>
          <br/><br/>
          <label>Book Type:
            <select 
                name="type" 
                id="type"
                value={inputs.type || ""}
                onChange={handleChange}
            >
                <option 
                    value="fiction" 
                    onChange={handleChange}>Fiction
                </option>
                <option 
                    value="non-fiction" 
                    onChange={handleChange}>Non-Fiction
                </option>
            </select>
            <br/><br/>
          </label>
          <input type="submit" />
      </form>
    )
}
