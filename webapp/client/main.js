"use strict";

import React, { Component } from 'react';
import { render } from 'react-dom';
import { BrowserRouter, Route, Redirect } from 'react-router-dom';
import { Helmet } from 'react-helmet';

import Homepage from './components/homepage';

class App extends Component {
    constructor(props) {
        super(props);

    }
    render(){
      return (
        <BrowserRouter>
          <div>
            <Helmet>
              <style>{'body {background-color: #616161}'}</style>
            </Helmet>
              <Route exact path = "/" render = {props =>{
                  return <Homepage/>
            }
          }/>
          </div>
        </BrowserRouter>
      )
    }
}
render(
    <App/>,
    document.getElementById('rootDiv')
);
