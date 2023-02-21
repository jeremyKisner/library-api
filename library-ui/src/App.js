import logo from './logo.svg';
import './App.css';
import React from 'react'
import ReactDOM from 'react' 

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
          <h1>Your Library</h1>
          <ul>
            {this.state.books.map((data) => (
              <li key={data.name}> 
                <p>Name: {data.name}</p>
                <p>Author: {data.author}</p>
                <p>Published: {data.published}</p>
              </li>
            ))}
        </ul>
      </div>
    );
  }
}

function App() {
  return (
    <div className="App">
      <Library />
    </div>
  );
}

export default App;
