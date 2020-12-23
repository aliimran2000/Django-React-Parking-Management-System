import {React,useState} from 'react';
import axiosInstance from '../Axios/AxiosInstance'

import Button from '@material-ui/core/Button';
import CssBaseline from '@material-ui/core/CssBaseline';
import TextField from '@material-ui/core/TextField';
//import FormControlLabel from '@material-ui/core/FormControlLabel';
//import Checkbox from '@material-ui/core/Checkbox';
import Link from '@material-ui/core/Link';
import Typography from '@material-ui/core/Typography';
  import { makeStyles } from '@material-ui/core/styles';
import Container from '@material-ui/core/Container';
import parkinglogo from '../Images/logo.png'




const useStyles = makeStyles((theme) => ({
  paper: {
    marginTop: theme.spacing(8),
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
  },
  avatar: {
    margin: theme.spacing(1),
    backgroundColor: theme.palette.secondary.main,
  },
  form: {
    width: '100%', // Fix IE 11 issue.
    marginTop: theme.spacing(1),
  },
  submit: {
    margin: theme.spacing(3, 0, 2),
  },
}));




export default function LoginPage() {
  const classes = useStyles();

  const[username,setUser] = useState("")
  const[password,setPassword] = useState("")
  const[WrongPass,setWrongPass] = useState(false)
  
  
  function SetType(){
  axiosInstance.post('/account/gettype/').then(
    result=>{
      sessionStorage.setItem("TYPE",result.data)
      
        
      if(result.data === "PA" ){
        window.location.href = "/Admin"
      }else if(result.data === "PE"){
        window.location.href = "/Employ"
      }else{
        window.location.href = "/Member"
      }

    }
  ).catch(error=>{
    console.log(error)
  })
  }


  function HandleLogin(event) {
    
   axiosInstance.post('/member/login/', {
          username: username,
          password: password
      }).then(
          result => {
              axiosInstance.defaults.headers['Authorization'] = "JWT " + result.data.access;
              localStorage.setItem('access_token', result.data.access);
              localStorage.setItem('refresh_token', result.data.refresh);

              if(result.status === 200){
                window.location.href = "/Admin"

                sessionStorage.setItem("USER_NAME",username)
                console.log(localStorage.getItem('access_token'))
                SetType()
               }
          }
      ).catch (error => {
        setWrongPass(true)
      })
  }
  

  function ReEnterPasswordMessage(){
    if(WrongPass){
        return (
                <Typography color="error">
                    UserID or Password was incorrect !!!
                </Typography>
        );
    }
  }


  return (
    <Container component="main" maxWidth="xs">
      <CssBaseline />
      
      <div className={classes.paper}>
       
        <img src={parkinglogo} alt=" parkinglogo" />
       

        <Typography component="h1" variant="h5" color="primary">
          Parking Management System
        </Typography>
              
        <div className={classes.form} >
            <TextField margin="normal" required
                fullWidth value={username} onChange={(event)=>{setUser(event.target.value)}} label="User" variant="outlined"/>
            <TextField margin="normal" required
                fullWidth value={password} onChange={(event)=>{setPassword(event.target.value)}}  label="Password" variant="outlined" type="password" />
            
            {ReEnterPasswordMessage()}

            <Button
                fullWidth
                variant="contained"
                color="primary"
                className={classes.submit}
                onClick={(event)=>{HandleLogin()}}
            >
                Sign In
            </Button>
        </div>

        
      </div>
    </Container>
  );
}