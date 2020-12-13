import React from 'react'
import {Typography} from '@material-ui/core';



export default function MemberView(props){

    return(
        <div>
            <Typography variant="h2" color="error">
                this is the member view {localStorage.getItem('access_token')}
            </Typography>   
            
        </div>
    )

};

