// component for the file upload
'use strict';

import React, {Component} from 'react';
import Button from '@material-ui/core/Button';
import Input from '@material-ui/core/Input';
import InputLabel from '@material-ui/core/InputLabel';
import FormControl from '@material-ui/core/FormControl';
import CloudUploadIcon from '@material-ui/icons/CloudUpload';
import withStyles from '@material-ui/core/styles/withStyles';
import LoadingIcon from './loading';
import ErrorMessage from './error';

const styles = () => ({
  paper:{
    textAlign:'center'
  },
  formItem:{
    paddingBottom:'10px',
    paddingTop:'10px'
  }
});
class FileUpload extends Component {
  constructor(props){
    super(props);
    this.state = {
      loading:false,
      error:false
    };
    this.handleSubmit = this.handleSubmit.bind(this);


  }
  handleSubmit(ev) {
      ev.preventDefault();
      // no client-side validation
      // error-checking is done on the server
      // send file to the server

      // create FormData object based on current state's file
      let form_data = new FormData($('#upload-file')[0]);
      $.ajax({
          type:'POST',
          url:'/audiofile',
          data: {test:'test'},
          contentType: false,
          cache: false,
          processData:false,
          beforeSend:()=>{
            this.setState({loading:true});
          },
          success: (data)=>{
              console.log(data)
              this.setState({loading:false});
              console.log("successfully uploaded file");
          },
          error: ()=>{
              console.log("something went wrong");
              this.setState({loading:false,error:true})
          }
      });
  }
  render(){
    return (
      <div className = {this.props.classes.paper}>
        <form id = "upload-file" method = "post" encType = "multipart/form-data">
          <div className = {this.props.classes.formItem}>
            <FormControl>
              <InputLabel htmlFor = "file-upload"></InputLabel>
              <Input id = "file-upload" type="file"></Input>
            </FormControl>
          </div>
          <div className = {this.props.classes.formItem}>
            <FormControl>
              <Button
                variant = "contained"
                color="secondary"
                startIcon={<CloudUploadIcon />}
                onClick={this.handleSubmit}
              >
              Upload
              </Button>
            </FormControl>
          </div>
        </form>
        <LoadingIcon loading = {this.state.loading} />
        <ErrorMessage error = {this.state.error} />
      </div>
    )
  }
}

export default withStyles(styles)(FileUpload);
