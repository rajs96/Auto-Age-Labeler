import React, { Fragment } from 'react';
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
        Differences in age creates bias in voice-based machine learning models.
        Automatically label your voice data with age categories so you can create
        segmented speech models that are less biased.
      </Typography>
    </Fragment>
  );
}

export default (withStyles(styles)(Description));
