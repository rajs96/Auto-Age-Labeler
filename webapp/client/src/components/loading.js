import React from 'react';
import CircularProgress from '@material-ui/core/CircularProgress';
import withStyles from '@material-ui/core/styles/withStyles';

const styles = () => ({
  loader:{
    paddingTop:'10px',
    paddingBottom:'10px'
  }
});

// loading icon component
const LoadingIcon = (props) => {
    // selectively renders based on whether loading
    // props is true
    if (!props.loading) {
      return null;
    }
    return (
      <div className = {props.classes.loader}>
        <CircularProgress color = "secondary"/>
      </div>
    );
}

export default withStyles(styles)(LoadingIcon);
