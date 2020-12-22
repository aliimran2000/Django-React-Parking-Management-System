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
import isLoggedin from '../../Utils/LoginCheck'
import Memberverifier from '../../Components/MemberVerifier'




export default function DeRegisterMember(){
       
    
    
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
                <Typography variant='h3' color="error" style = {{width: 1000 ,  margin:0}} >
                    De-Register Member
                </Typography>
            </Grid>
            <Grid>
                <Memberverifier/>                 
            </Grid>

  

            </Box>
            </Container>
        </div>
    )
}