import React from 'react'
import {Typography} from '@material-ui/core';
import TextField from '@material-ui/core/TextField'
import Grid from '@material-ui/core/Grid';
import { useState } from 'react';
import Button from '@material-ui/core/Button';
import Container from '@material-ui/core/Container';
import Box from '@material-ui/core/Box';
import { makeStyles } from '@material-ui/core/styles';
import Card from '@material-ui/core/Card';
import CardContent from '@material-ui/core/CardContent';
import axiosInstance from '../Axios/AxiosInstance'
import { green,red,blue } from '@material-ui/core/colors';

const useStyles = makeStyles({
    root: {
      minWidth: 275,
    },
    bullet: {
      display: 'inline-block',
      margin: '0 2px',
      transform: 'scale(0.8)',
    },
    title: {
      fontSize: 14,
    },
    pos: {
      marginBottom: 12,
    },
  });


export default function MemberVerifier(props){
    const classes = useStyles();   
    const [username,setUser] = useState("");
    const [password,setPassword] = useState("");
    const [isverified,setverify] = useState(false);
    const [UD,setUD] = useState({username:"notfound"})
   
    


    function HandleVerify(){
      let prom
        axiosInstance.post('member/verifycredentials/',{
            username: username,
            password: password,}
        )
        .then(
          result=>{
            if(result.status === 200)
  
                axiosInstance.post('member/getdetails/',{Member_ID:result.data}).then(result1=>{
                  setUD(result1.data)
                  setverify(true)
                })
                 
            }
        )
        .catch(error=>{
          console.log(error)
          setverify(false)
        })
    
    }

    function display(){
        if(isverified){
            return (
            <div>
                <Card style = {{width:1000,margin:5}} className={classes.root} variant="outlined">
                  <CardContent>
                      <Typography variant="h5" component="h2">
                      Name : {UD.username}   
                      </Typography>
                      <Typography className={classes.pos} color="textSecondary">
                      Date of Birth : {UD.DateOfBirth}
                      </Typography>
                      <Typography variant="body2" component="p">
                      CNIC :  {UD.CNIC}
                      </Typography>
                      <Typography variant="body2" component="p">
                      Email :  {UD.email}
                      </Typography>
                  </CardContent>
                  
                </Card>
            </div>)
        }
    }

    return(
    <div>

            <Grid>
                <TextField style = {{width: 1000 ,  margin:5}} required value={username} onChange={(event)=>{setUser(event.target.value)}} label="User ID" variant="outlined" />
            </Grid>
            
            <Grid>
                <TextField style = {{width: 1000 ,  margin:5}} required value={password} onChange={(event)=>{setPassword(event.target.value)}}  label="Password" variant="outlined" type="password" />
            </Grid>
            {display()}
            <Button fullWidth variant="contained" color="primary" onClick={() => {HandleVerify()}}>
                Submit 
            </Button>
            

                

    </div>
      )
    

  }

