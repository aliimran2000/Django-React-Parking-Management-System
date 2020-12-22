import React from 'react'
import {Typography} from '@material-ui/core';
import Container from '@material-ui/core/Container';
import Box from '@material-ui/core/Box';
import EmpDrawer from '../../Components/EmpDrawer';


function getname(){
    return "Ali Imran"
}



export default function AdminView(props){

    return(
        <div>
            <EmpDrawer adminpage={true} message={getname()}></EmpDrawer>
            
            <Container component="main" maxWidth="lg">
                <Box color="secondary.main" spacing={2} m={10} >
                    <Typography variant="h2" color="error">  this is the admin view </Typography>
                </Box>
            </Container>    
            
        </div>
    )

};

