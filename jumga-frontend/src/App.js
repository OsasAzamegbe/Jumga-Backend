import React, { useEffect } from 'react';
import './App.css';

import {BrowserRouter as Router, Switch, Route} from 'react-router-dom';
import Cookies from 'js-cookie'

import Navbar from './components/Navbar';
import Home from './pages/home/Home';
import Signup from './pages/signup/SignUp';
import { useAuth } from './context/AuthProvider';
import AlertProvider from './context/AlertProvider';
import Alert from './components/Alert';

const App = () => {
  const { dispatch } = useAuth();

  useEffect(() =>{
    const user = Cookies.getJSON("user");
    const merchant = Cookies.getJSON("merchant");
    const dispatch_rider = Cookies.getJSON("dispatch_rider");
    if (user||merchant||dispatch_rider) {
      dispatch({
        type: "LOGIN",
        payload: {
          user,
          merchant,
          dispatch_rider
        }
      });
    };
  }, [dispatch]);

  return (
    <div className="App">
      <AlertProvider>
        <Router>
          <Navbar/>
          <Alert/>
          <Switch>
            <Route exact path="/" component={Home}/>
            <Route path="/signup/" component={Signup}/>
          </Switch>
        </Router>
      </AlertProvider>        
    </div>
  );
};

export default App;