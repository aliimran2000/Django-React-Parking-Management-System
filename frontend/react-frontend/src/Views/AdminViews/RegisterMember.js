import React from 'react'
import { useHistory } from "react-router-dom";
import {Typography} from '@material-ui/core';
import { makeStyles } from '@material-ui/core/styles';
import TextField from '@material-ui/core/TextField'
import Grid from '@material-ui/core/Grid';
import { useState } from 'react';
import InputMask from 'react-input-mask';
import validator from 'validator';
import Button from '@material-ui/core/Button';
import Container from '@material-ui/core/Container';
import Box from '@material-ui/core/Box';
import axiosInstance from '../../Axios/AxiosInstance'

import isLoggedin from '../../Utils/LoginCheck'

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
  


export default function RegisterMember(props){

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
    const [errorm,setm] = useState("")

    function alphanumeric(value){
       if(value.match(/((^[0-9]+[a-z]+)|(^[a-z]+[0-9]+))+[0-9a-z]$/i)){
            return true
        }
        
        return false

    }


    function checkpassstrength(value){
        
        if((value.length < 8) || !alphanumeric(value) )
        {
            if(!errorState)
                SeterrorState(true)
            
            return(
                <Typography color="error">
                    Password must contain atleast 8 letters and must be alphanumeric       
                </Typography>
            )
        }
        else{
            if(errorState)
                SeterrorState(false)
        }
    }

    const emailtest = (value)=>{
        
        
        if(!validator.isEmail(value)){
            //SeterrorState(true)
            if(!errorState2)
                SeterrorState2(true)
            
            return (
                <Typography color="error">
                     Invalid Email
                </Typography>
            )
        }else{
            if(errorState2)
                SeterrorState2(false)
        }
    }

    
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
            setm("Invalid User Details")
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
    
    
    
    if(!done){
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
                <InputMask style = {{width: 350 ,  margin:10}} mask="99999-9999999-9" maskChar=" " value={CNIC} onChange={(event)=>{setCNIC(event.target.value.replaceAll("-",""))}} >
                    {()=><TextField required label="CNIC" variant="outlined" style = {{width: 350 ,  margin:10}}  />}
                </InputMask>
            </Grid>

            <Grid>
                <InputMask mask="9999-9999999" maskChar=" " value={Phone_No} onChange={(event)=>{setPhone(event.target.value.replace("-",""))}} >
                    {()=><TextField required label="Mobile Number" variant="outlined" style = {{width: 350 ,  margin:10}} />}
                </InputMask>
            </Grid>
            <Grid>
                <TextField style = {{width: 350 ,  margin:10}} required label="Address" multiline rows={4} value={Address} onChange={(event)=>{setAddress(event.target.value)}}/>
            </Grid>
        
            <Grid>
                <TextField  style = {{width: 350 ,  margin:10}} label="Date of Birth" type="date" defaultValue="2000-01-01" value={DateOfBirth} onChange={(event)=>{setDateOfBirth(event.target.value)}}/>
            </Grid>
            
            <Grid>
                <TextField style = {{width: 350 ,  margin:10}} required value={email} onChange={(event)=>{setEmail(event.target.value)}} label="E Mail" variant="outlined" />
                {emailtest(email)}
            </Grid>

            <Grid>
                <TextField style = {{width: 350 ,  margin:10}} required value={username} onChange={(event)=>{setUser(event.target.value)}} label="User ID" variant="outlined" />
            </Grid>
            
            <Grid>
                <TextField style = {{width: 350 ,  margin:10}} required value={password} onChange={(event)=>{setPassword(event.target.value)}}  label="Password" variant="outlined" type="password" />
                {checkpassstrength(password)}
            </Grid>

            {SubmitButtonDisplay()}

            <Typography variant='h4' color="error" style = {{width: 10000 ,  margin:10}}>
            {errorm}
            </Typography>
            
            
                
        </Box>
        </Container>
        
        </div>  
    )
    }
    else{
        return(
            <div>
                <Button onClick={() => {history.goBack()}}>
                    GO BACK
                </Button>
                <Typography variant='h3' color="primary" style = {{width: 10000 ,  margin:10}} >
                    MEMBER REGISTRATION SUCCESSFULL
                </Typography>
            </div>
        )
    }
    
   
};

