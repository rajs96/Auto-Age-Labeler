import React, { Component} from 'react';
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
  }

  render() {
    console.log("error state",this.state)
    return (
      <Snackbar
        anchorOrigin={{vertical:'bottom',horizontal:'left'}}
        open = {this.props.error}
        message = "Upload unsuccessful"
      />
    );
  }
}

export default withStyles(styles)(ErrorMessage);
