//'use strict';
import React, { Component,Fragment } from 'react';
import Typography from '@material-ui/core/Typography';
import withStyles from '@material-ui/core/styles/withStyles';


const styles = () => ({
  root:{
    paddingTop:'10px',
    paddingBottom:'10px',
    textAlign:'center'
  }

});
// stateless description component
const Description = (props) => {
  return (
    <Fragment>
      <Typography className = {props.classes.root}>
        Here I'm going to describe some of the uses of this application
        and how it relates to segmenting audio samples. Blah blah
        Upload your file and jawn. FOurth change
      </Typography>
    </Fragment>
  );
}

export default (withStyles(styles)(Description));
