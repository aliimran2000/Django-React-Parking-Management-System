import {React,useState} from 'react';

//import axios from 'axios';
import { makeStyles } from '@material-ui/core/styles';
import TextField from '@material-ui/core/TextField';
import { Button, Grid } from '@material-ui/core';


function HandleLogin(){

}

const useStyles = makeStyles((theme) => ({
    root: {
      '& > *': {
        margin: theme.spacing(1),
        width: '50ch',
        marginTop: "10",
        alignItems:"center",
      },
    },
  }));


export default function Login_Form(prop) {
    //const classes = useStyles();

    const[User,setUser] = useState("")
    const[Password,setPassword] = useState("")
    
    
    return (
    <Grid  
    container
    spacing={15}
    marginTop="10"
    alignItems="center"
    alignContent="center" 
    justify="center"
    style={{ minHeight: '100vh' }}
>
        <div>

            <Grid item >
                <TextField value={User} onChange={(event)=>{setUser(event.target.value)}} id="outlined-basic" label="User ID" variant="outlined" />
            </Grid><br/>   
            <Grid item >
                <TextField value={Password} onChange={(event)=>{setPassword(event.target.value)}} id="outlined-basic" label="Password" variant="outlined" type="password" />
            </Grid>
            <br/>
            <Grid>
                <Button color="primary" variant="contained" >SIGN IN</Button>
            </Grid>
        </div>
    </Grid>
  );
}