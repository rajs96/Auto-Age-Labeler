"use strict";
import React, { Component,Fragment } from 'react';
import {withRouter} from 'react-router-dom';
import Grid from '@material-ui/core/Grid';
import Typography from '@material-ui/core/Typography';
import withStyles from '@material-ui/core/styles/withStyles';
import  FileUpload  from './fileUpload';
import Description from './description'


// styles for our homepage
const styles = () => ({
  typographyHeading:{
    textAlign:'center',
    paddingTop:'10px',
    paddingBottom:'10px'
  }
});

// stateless homepage component
const Homepage = (props) => {

  return (
    <Fragment>
      <Grid container = {true}>
        <Grid item = {true} md = {3}></Grid>
        <Grid item = {true} md = {6}>
          <Typography className = {props.classes.typographyHeading}
           variant = 'h2'
           color = "secondary">
            Automatic age labeler for voice samples
          </Typography>
        </Grid>
        <Grid item = {true} md = {3}></Grid>
        <Grid item = {true} md = {3}></Grid>
        <Grid item = {true} md = {6}>
          <Typography>
            <Description/>
          </Typography>
        </Grid>
        <Grid item = {true} md = {3}></Grid>
        <Grid item = {true} md = {3}></Grid>
        <Grid item = {true} md = {6}>
          <FileUpload/>
        </Grid>
        <Grid item = {true} md = {3}></Grid>
      </Grid>
    </Fragment>
  )
}

export default withRouter(withStyles(styles)(Homepage));
