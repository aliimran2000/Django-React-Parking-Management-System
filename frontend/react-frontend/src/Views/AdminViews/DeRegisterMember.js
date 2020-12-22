import React from 'react'
import {Typography} from '@material-ui/core';
import TextField from '@material-ui/core/TextField'
import Grid from '@material-ui/core/Grid';
import { useState } from 'react';
import Button from '@material-ui/core/Button';
import Container from '@material-ui/core/Container';
import Box from '@material-ui/core/Box';
import GoBack from '../../Components/GoBack'
import { makeStyles } from '@material-ui/core/styles';
import { green,red,blue } from '@material-ui/core/colors';
import MemberDataDisplay from '../../Components/MemberDataDisplay'
import isLoggedin from '../../Utils/LoginCheck'

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

export default function DeRegisterMember(){
    const classes = useStyles();    
    let AccountID  = ""
    
    if(!(isLoggedin() === "PA")){
      console.log(isLoggedin()) 
      window.location.href = "/"
    }
    else{
        console.log(isLoggedin())
    }

    
    return(
        <div>
            <GoBack/>
            <Container component="main" maxWidth="lg"> 
            <Box spacing={3} m={10}>

            <Grid>
                <Typography variant='h3' color="error" style = {{width: 10000 ,  margin:10}} >
                    De-Register Member
                </Typography>
            </Grid>
            <Grid>
                  <MemberDataDisplay/>
            </Grid>

  

            </Box>
            </Container>
        </div>
    )
}