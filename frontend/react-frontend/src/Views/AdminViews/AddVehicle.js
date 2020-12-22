import React from 'react'
import { useHistory } from "react-router-dom";
import {Typography} from '@material-ui/core';
import { makeStyles } from '@material-ui/core/styles';
import TextField from '@material-ui/core/TextField'
import Grid from '@material-ui/core/Grid';
import { useState } from 'react';
import isLoggedin from '../../Utils/LoginCheck'
import Button from '@material-ui/core/Button';
import Container from '@material-ui/core/Container';
import Box from '@material-ui/core/Box';
import axiosInstance from '../../Axios/AxiosInstance'



const useStyles = makeStyles((theme) => ({
    paper: {
      marginTop: theme.spacing(8),
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
    },
    avatar: {
      margin: theme.spacing(1),
      backgroundColor: theme.palette.secondary.main,
    },
    form: {
      width: '100%', // Fix IE 11 issue.
      marginTop: theme.spacing(1),
    },
    submit: {
      margin: theme.spacing(3, 0, 2),
    },
  }));
  


export default function AddVehicle(props){

    if(!(isLoggedin() === "PA")){
        console.log(isLoggedin()) 
        window.location.href = "/"
    }
    else{
        console.log(isLoggedin())
    }
    
    let history = useHistory();
    
    const [first_name,setfirst_name] = useState('');
    const [last_name,setlast_name] = useState(''); 
    const [Address,setAddress] = useState('');
    const [CNIC, setCNIC] = useState('');
    const [Phone_No,setPhone] = useState('');
    const [DateOfBirth,setDateOfBirth] = useState();
    const [username,setUser] = useState("");
    const [password,setPassword] = useState("");
    const [email,setEmail] = useState("");
    const [errorState,SeterrorState] = useState(true);
    const [errorState2,SeterrorState2] = useState(true);
    const [done,isdone] = useState(false)
    

  

    
    function handleSubmit(event){
        axiosInstance.post('member/signup/', {
            username: username,
            password: password,
            first_name : first_name,
            last_name:last_name,
            Address:Address,
            CNIC:CNIC,
            Phone_No:Phone_No,
            DateOfBirth:DateOfBirth,
            email:email,
        }).then(
            result => {
                
                if(result.status === 201){
                  isdone(true)
                  //window.location.href = "/"
                 }
            }
        ).catch (error => {
            
          })
    }

    function SubmitButtonDisplay(){
        if(errorState || errorState2){
            return( 
                <Button fullWidth variant="contained" color="primary" disabled className={useStyles.submit}//onClick={(event)=>{HandleRequest()}}
                 >
                Submit 
                </Button>
                )
            }
        else{
            return(
                <Button fullWidth variant="contained" color="primary" className={useStyles.submit}  onClick={(event)=>{handleSubmit()}}>
                Submit </Button>
            )
        }
    }
    
    
   
    return(
        <div>
        <Button color='primary' onClick={() => {history.goBack()}}>
                    GO BACK
        </Button>   
        <Container component="main" maxWidth="md"> 
        <Box spacing={3} m={10}>
            <Grid>
                <Typography variant='h3' color="primary" style = {{width: 10000 ,  margin:10}} >
                    Member Registration Form
                </Typography>
            </Grid>
            <Grid container direction="row" >
                <TextField style = {{width: 350 ,  margin:10}} required label="First Name" variant="outlined"  value={first_name} onChange={(event)=>{setfirst_name(event.target.value)}}/>
                <TextField style = {{width: 350 , margin:10}} required label="Last Name" variant="outlined"   value={last_name} onChange={(event)=>{setlast_name(event.target.value)}}/> 
            </Grid>

            <Grid>
                <TextField style = {{width: 350 ,  margin:10}} required label="Address" multiline rows={4} value={Address} onChange={(event)=>{setAddress(event.target.value)}}/>
            </Grid>
        
            <Grid>
                <TextField  style = {{width: 350 ,  margin:10}} label="Date of Birth" type="date" defaultValue="2000-01-01" value={DateOfBirth} onChange={(event)=>{setDateOfBirth(event.target.value)}}/>
            </Grid>
        
            <Grid>
                <TextField style = {{width: 350 ,  margin:10}} required value={username} onChange={(event)=>{setUser(event.target.value)}} label="User ID" variant="outlined" />
            </Grid>
      

            {SubmitButtonDisplay()}

            
                
        </Box>
        </Container>
        
        </div>  
    )
   
   
};

