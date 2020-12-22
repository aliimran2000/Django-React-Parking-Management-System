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
import axiosnojwt from '../Axios/axiosnojwt'
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


export default function MemberDataDisplay(props){
    const classes = useStyles();    
    
    const [Member_ID,setMember_ID] = useState(1);
    const [UD,setUD] = useState({username:''});
    

    async function getDatabyID(){
      let prom = await axiosInstance.post('member/getdetails/',{Member_ID:Member_ID})
      setUD(prom.data)      
    }
      
    return(
      <div>

      <Card style = {{width:1000,margin:5}} className={classes.root} variant="outlined">
        
        <CardContent>
            <Grid>
                  <TextField style = {{width:960,margin:5}} required label="Enter User Account ID" variant="outlined" onChange={(event)=>{setMember_ID(event.target.value)}}/>
            </Grid>
            
            <Typography variant="h5" component="h2">
            Name : {UD.username}   
            </Typography>
            <Typography className={classes.pos} color="textSecondary">
            Date of Birth : {UD.DateOfBirth}
            </Typography>lulloo pudoo har kubooter dunda doli
            <Typography variant="body2" component="p">
            CNIC :  {UD.CNIC}
            </Typography>
            <Typography variant="body2" component="p">
            Email :  {UD.email}
            </Typography>
            
        </CardContent>
        
        </Card>
        
        <Button  style={{ width:1005 ,color: green[1000],background:blue[400] ,margin:5}} onClick={()=>getDatabyID()}>
            Search User
        </Button>
    </div>
      )
    

  }

