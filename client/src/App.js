import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import  Search from './components/Search';
import  Result from './components/Result';

const STREAM_SOURCE = window.STREAM_SOURCE;
const PUBLIC_URL = window.PUBLIC_URL;

class App extends Component {
  constructor() {
    super();
    this.state = {
      query: '',
      results: null,
    };
  }

  onSubmit(evt) {
    const query = evt.target.value;
    this.setState((prevState, props) => ({ query }));
    fetch(`/api/media_types?q=${query}`);
  }

  componentDidMount() {
    // connect to stream
    const source = new EventSource(STREAM_SOURCE);
    source.addEventListener('info', (event) => {
      const data = JSON.parse(event.data);
      if (data.webpage_url === this.state.query) {
        this.setState((prevState, props) => ({ results: data }));
      }
    }, false);
  }

  render() {
    const {results, onSubmit} = this.state;
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h1 className="App-title">Offline Tube</h1>
        </header>
        <Search onSubmit={onSubmit} />
        <Result results={results} />
      </div>
    );
  }
}

export default App;
