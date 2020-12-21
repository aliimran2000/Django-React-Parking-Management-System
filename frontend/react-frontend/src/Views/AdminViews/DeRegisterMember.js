import React from 'react'
import {Typography} from '@material-ui/core';
import TextField from '@material-ui/core/TextField'
import Grid from '@material-ui/core/Grid';
import { useState } from 'react';
import Button from '@material-ui/core/Button';
import Container from '@material-ui/core/Container';
import Box from '@material-ui/core/Box';
import GoBack from '../../Components/GoBack'
import { makeStyles } from '@material-ui/core/styles';
import Card from '@material-ui/core/Card';
import CardContent from '@material-ui/core/CardContent';
import axiosInstance from '../../Axios/AxiosInstance'
import axiosnojwt from '../../Axios/axiosnojwt'
import { green,red,blue } from '@material-ui/core/colors';

const useStyles = makeStyles({
    root: {
      minWidth: 275,
    },
    bullet: {
      display: 'inline-block',
      margin: '0 2px',
      transform: 'scale(0.8)',
    },
    title: {
      fontSize: 14,
    },
    pos: {
      marginBottom: 12,
    },
  });

export default function DeRegisterMember(){
    const classes = useStyles();    
    
    const [DC,setDC] = useState(false);
    const [id,setid] = useState('');


    function getDatabyID(UID){
      //const USERDATA = axiosnojwt.get('/getnamebyid',{id:UID})
      const USERDATA = {"Name":"Ali Imran" , "DOB":"11-02-2000","CNIC":"12314556688"} 
      return USERDATA
    }


    function deregisterapicall(){

    }


    function displayCard(){
      if(DC){
      let UD = getDatabyID(id);
      return (
        <div>
          <Card style = {{width:1000,margin:5}} className={classes.root} variant="outlined">
            
            <CardContent>
                <Typography className={classes.title} color="error" gutterBottom>
                The DeRegistration Action is irreversible Make Sure the data entered is correct
                </Typography>
                <Typography variant="h5" component="h2">
                Name :  {UD.Name}
                </Typography>
                <Typography className={classes.pos} color="textSecondary">
                Date of Birth : {UD.DOB} 
                </Typography>
                <Typography variant="body2" component="p">
                CNIC : {UD.CNIC}
                </Typography>
            </CardContent>
            
            </Card>
            <Button fullWidth style={{ color: blue[1000],background:red[400] ,margin:5}}>
              CONFIRM DEREGISTRATION
            </Button>
        </div>
      )}
      return null;
    }



    return(
        <div>
            <GoBack/>
            <Container component="main" maxWidth="lg"> 
            <Box spacing={3} m={10}>

            <Grid>
                <Typography variant='h3' color="error" style = {{width: 10000 ,  margin:10}} >
                    De-Register Member
                </Typography>
            </Grid>
            <Grid>
                  <TextField style = {{width:1000,margin:5}} required label="Enter User Account ID" variant="outlined" onChange={(event)=>{setid(event.target.value)}} />
            </Grid>
            <Grid>
            <Grid>
              {displayCard()}
            </Grid>
            <Button style={{ color: blue[1000],background:green[500] , margin:5}} onClick={()=>setDC(true)}>
                  CHECK
            </Button>  
            </Grid>
            

            

            </Box>
            </Container>
        </div>
    )
}