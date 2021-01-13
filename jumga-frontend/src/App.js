import React, { useEffect } from 'react';
import './App.css';

import {BrowserRouter as Router, Switch, Route} from 'react-router-dom'

import Navbar from './components/Navbar';
import Home from './pages/home/Home';
import Signup from './pages/signup/SignUp';
import { useAuth } from './context/AuthProvider';

const App = () => {
  const { dispatch } = useAuth();

  useEffect(() =>{
    const user = JSON.parse(localStorage.getItem("user"));
    const merchant = JSON.parse(localStorage.getItem("merchant"));
    const dispatchRider = JSON.parse(localStorage.getItem("dispatchRider"));
    if (user||merchant||dispatchRider) {
      dispatch({
        type: "LOGIN",
        payload: {
          user,
          merchant,
          dispatchRider
        }
      });
    };
  }, [dispatch]);

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