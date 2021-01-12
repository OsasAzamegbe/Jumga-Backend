import React from 'react';
import './App.css';

import {BrowserRouter as Router, Switch, Route} from 'react-router-dom'

import Navbar from './components/Navbar';
import Home from './pages/home/Home';
import Signup from './pages/signup/SignUp';

const App = () => {
  return (
    <div className="App">
      <Router>
        <Navbar/>
        <Switch>
          <Route exact path="/" component={Home}/>
          <Route path="/signup/" component={Signup}/>
        </Switch>
      </Router>
    </div>
  );
};

export default App;