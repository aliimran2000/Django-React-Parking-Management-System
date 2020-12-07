import React from 'react'
import {Typography} from '@material-ui/core';
import Login_Form from '../Components/Login_Form'


function LoginPage(props){

    return(
        <React.Fragment>
            <Typography variant="h2">
                Parking Managemeent System
            </Typography>
            <Login_Form/>
        </React.Fragment>
    )

};


export default LoginPage;