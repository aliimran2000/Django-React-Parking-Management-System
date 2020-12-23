import React from 'react'
import {Typography} from '@material-ui/core';
import { makeStyles } from '@material-ui/core/styles';
import TextField from '@material-ui/core/TextField'
import Grid from '@material-ui/core/Grid';
import { useState } from 'react';
import isLoggedin from '../../Utils/LoginCheck'
import Button from '@material-ui/core/Button';
import Container from '@material-ui/core/Container';
import Box from '@material-ui/core/Box';
import axiosInstance from '../../Axios/AxiosInstance'
import GoBack from '../../Components/GoBack'
import Memberverifier from '../../Components/MemberVerifier'
import { green,red,blue } from '@material-ui/core/colors';
import Card from '@material-ui/core/Card';
import CardContent from '@material-ui/core/CardContent';


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


export default function AddVehicle(props){
    const classes = useStyles();
    const [UID,setUID] = useState(-1);
    const [success,setsuccess] = useState(false);
    const [Vehicle_ID,setVID] = useState('');
    const [Vehicle_Model,setVM] = useState('');
    



    function HandleRegVec(){
        let prom = axiosInstance.post('member/registervehicle/',{
            Vehicle_ID: Vehicle_ID,
            Vehicle_Model: Vehicle_Model,
            Member_ID:UID
        }).then(
            result=>{
                if(result.status === 201){
                    setsuccess(true)
                }
            }
        ).catch(error=>{
            console.log(error)
        })
    }


    function VehicleRegForm(){
        if(UID !== -1){

            if(success){
                return ( 
                <Typography align="center" variant="h4" style={{color:green[500]}}>
                    Vehicle Added Successfully
                </Typography>)
            }

            return(
            <div>
                <Card style = {{width:1000,margin:5,backgroundColor:green[100]}} className={classes.root} variant="outlined">
                <CardContent>
                    <Grid>
                        <Typography variant="h4" style={{color:green[500]}}>
                            Enter Car Details Here
                        </Typography>
                    </Grid>
                    
                    <Grid>
                        <TextField style = {{width: 950 ,  margin:5}} variant="outlined" required label="Vehicle ID" value={Vehicle_ID} onChange={(event)=>{setVID(event.target.value)}}/>
                    </Grid>
                    
                    <Grid>
                        <TextField style = {{width: 950  ,  margin:5}} variant="outlined" required label="Car Model Details"  value={Vehicle_Model} onChange={(event)=>{setVM(event.target.value)}}/>
                    </Grid>    
                    <Grid>
                        <Button style = {{width: 1000 ,  margin:5,backgroundColor:green[800]}} variant="contained"  onClick={()=>{HandleRegVec()}}>
                            Register Car
                        </Button>
                    </Grid>
                 </CardContent>
                </Card>
            </div>    
            )
        }else{
            return(null)
        }
    }


    if(!(isLoggedin() === "PA")){
        console.log(isLoggedin()) 
        window.location.href = "/"
    }
    else{
        console.log(isLoggedin())
    }
    

   
    return(
        <div>
            <GoBack/>
            <Container component="main" maxWidth="lg"> 
            <Box spacing={3} m={10}>

            <Grid>
                <Typography align="center" variant='h2' color="primary" style = {{width: 1000 ,  margin:0}} >
                   Register Vehicle
                </Typography>
            </Grid>
            <Grid>
                <Memberverifier  Ddata={[UID,setUID]}/>
            </Grid>
                {VehicleRegForm()}
            <Grid>
            
            </Grid>

            </Box>
            </Container>
        </div>  
    )
   
   
};

