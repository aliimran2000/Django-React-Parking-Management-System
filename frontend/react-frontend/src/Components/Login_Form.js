import {React,useState} from 'react';

import TextField from '@material-ui/core/TextField';
import { Button, Grid ,Typography } from '@material-ui/core';

import axiosInstance from '../Axios/AxiosInstance'


export default function Login_Form(prop) {
    //const classes = useStyles();

    const[username,setUser] = useState("")
    const[password,setPassword] = useState("")
    
    
    function HandleLogin() {
        axiosInstance.post('/member/login/', {
            username: username,
            password: password
        }).then(
            result => {
                axiosInstance.defaults.headers['Authorization'] = "JWT " + result.data.access;
                localStorage.setItem('access_token', result.data.access);
                localStorage.setItem('refresh_token', result.data.refresh);

                if(result.status === 200){
                    window.location.href = "/MemberView/"
                }
                    
            }
        ).catch (error => {
            throw error;
        })
    }
    
    
    

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
              <Grid>
                   <Typography variant="h5">MEMBER LOGIN</Typography>
              </Grid>
              <br/>
              <Grid item >
                  <TextField value={username} onChange={(event)=>{setUser(event.target.value)}} id="outlined-basic" label="User ID" variant="outlined" />
              </Grid><br/>   
              <Grid item >
                  <TextField value={password} onChange={(event)=>{setPassword(event.target.value)}} id="outlined-basic" label="Password" variant="outlined" type="password" />
              </Grid>
              <br/>
              <Grid>
                  <Button color="primary" variant="contained" onClick={HandleLogin}>SIGN IN</Button>
              </Grid>
          </div>
      </Grid>
  );
}