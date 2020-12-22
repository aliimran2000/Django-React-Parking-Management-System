import React from 'react'
import { useState } from 'react';
import {Typography} from '@material-ui/core';
import Container from '@material-ui/core/Container';
import Box from '@material-ui/core/Box';
import EmpDrawer from '../../Components/EmpDrawer';
import axiosInstance from '../../Axios/AxiosInstance'
import isLoggedin from '../../Utils/LoginCheck'




export default function AdminView(props){
    
    if(!(isLoggedin() === "PA")){
        console.log(isLoggedin()) 
        window.location.href = "/"
    }
    else{
        console.log(isLoggedin())
    }

    
    return(
        <div>
            
            <EmpDrawer adminpage={true}></EmpDrawer>
            
            <Container component="main" maxWidth="lg">
                <Box color="secondary.main" spacing={2} m={10} >
                    <Typography variant="h2" color="error">  this is the admin view </Typography>
                </Box>
            </Container>    
            
        </div>
    )

};

