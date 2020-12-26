import React from 'react'
import {Typography} from '@material-ui/core';
import TextField from '@material-ui/core/TextField'
import Grid from '@material-ui/core/Grid';
import Container from '@material-ui/core/Container';
import Box from '@material-ui/core/Box';
import UnParkComponent from '../Components/UnParkComponent'
import GoBack from '../Components/GoBack'
import isLoggedin from '../Utils/LoginCheck'



export default function UnParkCar(props){
    
    

    let val = isLoggedin()
    if(val !== "PA" && val !== "PE" ){
        console.log(isLoggedin()) 
        window.location.href = "/"
    }
    else{
        console.log(isLoggedin())
    }

    return (
        <div>
            <GoBack/>

            <Container component="main" maxWidth="lg"> 
            <Box spacing={3} m={10}>

            <Grid align="center">
                <Typography variant='h3' color="error" style = {{width: 1000 ,  margin:0}} >
                    UnPark Car
                </Typography>
            </Grid>
            <Grid>
                <UnParkComponent />
            </Grid>
            <Grid>
            
            </Grid>
            
            </Box>
            </Container>
        </div>)

  }

