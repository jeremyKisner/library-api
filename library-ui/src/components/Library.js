import React from 'react'
import Book from './Book'

class Library extends React.Component {
    constructor(props) {
      super(props)
      this.state = {
        books : []
      };
    }
  
    componentDidMount() {
      this.BookList()
    }
  
    BookList() {
      var req = new XMLHttpRequest()
      req.addEventListener("load", () => {
          var data = req.responseText
          data = JSON.parse(data)
          this.setState({userdata: data}, () => {
              console.log("DATA: ", data)
              this.setState({books: data})
          })
          
      })
      req.open("GET", "http://127.0.0.1:5000/books")
      req.send()
    }
  
    render() {
      return (
        <div>
            {this.state.books.map((data, index) => (
              <Book key={index} data={data} index={index} />
            ))}
        </div>
      );
    }
  }

export default Library;