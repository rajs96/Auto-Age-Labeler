"use strict";
import React, { Component,Fragment } from 'react';
import withStyles from '@material-ui/core/styles/withStyles';
import Snackbar from '@material-ui/core/Snackbar';

const styles = () => ({
  loader:{
    paddingTop:'10px',
    paddingBottom:'10px'
  }
});

// loading icon component
class ErrorMessage extends Component {
  constructor(props){
    super(props);
    this.handleClose = this.handleClose.bind(this);
  }
  // set it to false on close
  handleClose () {
    //this.setState({display:false});
  }
  render() {
    console.log("error state",this.state)
    return (
      <Snackbar
        anchorOrigin={{vertical:'bottom',horizontal:'left'}}
        open = {this.props.error}
        onClose = {this.handleClose}
        variant = "error"
        message = "Test if this works"
      />
    );
  }
}

export default withStyles(styles)(ErrorMessage);
