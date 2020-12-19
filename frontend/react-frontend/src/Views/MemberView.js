import React from 'react'
import {Typography} from '@material-ui/core';
import PersistentDrawerLeft from '../Components/Drawer'
import Button from '@material-ui/core/Button';
import Container from '@material-ui/core/Container';
import Box from '@material-ui/core/Box';

export default function MemberView(props){

    return(
        <div>
            <PersistentDrawerLeft message="Member View"></PersistentDrawerLeft>
            
            <Container component="main" maxWidth="lg">
                <Box color="secondary.main" spacing={2} m={10} >
                    <Typography variant="h2" color="error">  this is the member view </Typography>
                    
                </Box>
            </Container>    
            
        </div>
    )

};

