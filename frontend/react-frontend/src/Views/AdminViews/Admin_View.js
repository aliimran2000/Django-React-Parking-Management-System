import React from 'react'
import {Typography} from '@material-ui/core';
import Container from '@material-ui/core/Container';
import Box from '@material-ui/core/Box';
import EmpDrawer from '../../Components/EmpDrawer';
import ParkingDisplay from '../../Components/ParkingDisplay'
export default function AdminView(props){
    
    


    

    if(sessionStorage.getItem("TYPE") !== "PA"){
        window.location.href = "/"
    }



    
    
    return(
        <div>
            
            <EmpDrawer adminpage={true}></EmpDrawer>
            
            <Container component="main" maxWidth="lg">
                <Box  spacing={2} m={10} >
                <Typography variant="h3" align="center">
                    Welcome
                </Typography>
                <ParkingDisplay/>
                </Box>
            </Container>    
            
        </div>
    )

};

