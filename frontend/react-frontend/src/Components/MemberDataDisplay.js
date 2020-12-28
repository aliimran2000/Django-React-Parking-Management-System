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

export default function MemberDataDisplay(props){
    const classes = useStyles();    
    
    const [Member_ID,setMember_ID] = useState(1);
    //let UD = {username:''}
    const [UD,setUD] = useState({username:''});
    

    async function getDatabyID(){
      let val = props.Rid
      let prom = await axiosInstance.post('member/getdetails/',{Member_ID:val})
    
      this.setState({UD:prom.data})
      //setUD(prom.data)
     
      
      }

    
    //getDatabyID()
    

    return(
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
      
    </div>
      )
    

  }

