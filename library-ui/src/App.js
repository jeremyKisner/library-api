import logo from './logo.svg';
import './App.css';
import React from 'react'
import ReactDOM from 'react' 

const Book = (data) => {
  console.log('here data ', data.data.name)
  return (
    <div key={data.data.name}>
      <h2>{data.data.name}</h2>
      <h3>{data.data.author}</h3>
      <h4>{data.data.published}</h4>
    </div>
  )
}

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
          {this.state.books.map((data, index) => (
            <Book key={index} data={data} />
          ))}
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
