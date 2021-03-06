import React from 'react'
import {Typography} from '@material-ui/core';
import { makeStyles } from '@material-ui/core/styles';

import Grid from '@material-ui/core/Grid';
import { useState } from 'react';
import isLoggedin from '../../Utils/LoginCheck'
import Button from '@material-ui/core/Button';
import Container from '@material-ui/core/Container';
import Box from '@material-ui/core/Box';
import axiosInstance from '../../Axios/AxiosInstance'
import GoBack from '../../Components/GoBack'
import Memberverifier from '../../Components/MemberVerifier'
import { green,grey} from '@material-ui/core/colors';
import Card from '@material-ui/core/Card';
import CardContent from '@material-ui/core/CardContent';
import Accordion from '@material-ui/core/Accordion';
import AccordionSummary from '@material-ui/core/AccordionSummary';
import AccordionDetails from '@material-ui/core/AccordionDetails';
import ExpandMoreIcon from '@material-ui/icons/ExpandMore';

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


export default function RemoveVehicle(props){
    const classes = useStyles();
    const [UID,setUID] = useState(-1);
    const [VecLst,SetLst] = useState([{Vehicle_ID: "non",Vehicle_Model: "non"}]);
    const [success,setsuccess] = useState(false);
    const [Vsuccess,setVsuccess] = useState(0);
    const [em,setem] = useState("");
    

    
    

    //member/getvehiclesdetail/
    //'member/deregistervehicle/'

    function HandleDeRegVec(Vehicle_ID){
        axiosInstance.post('member/deregistervehicle/',{
            Vehicle_ID: Vehicle_ID,
            Member_ID:UID
        }).then(
            result=>{
                if(result.status === 200){
                    setsuccess(true)
                }
            }
        ).catch(error=>{
            setsuccess(false)
            setem(error.response.data)
        })
    }

    function GetListofVehicles(){
         axiosInstance.post('member/getvehiclesdetail/',{
            Member_ID:UID
        }).then(
            result=>{
                console.log(result.data)    
                setVsuccess(1)
                let L = result.data.vehicles
                SetLst(L)
                
            }
        ).catch(error=>{
            //setVerror(error.response.data)
            setVsuccess(2)
            setem(error.response.data)
        })
    }


    function DisplayCarItem(CAR){
        return (
            <Accordion >
            <AccordionSummary   expandIcon={<ExpandMoreIcon />}   aria-controls="panel1a-content"   id="panel1a-header"   style={{backgroundColor:green[200]}}>
                <Typography >{CAR.Vehicle_ID}</Typography>
            </AccordionSummary>
            <AccordionDetails  style={{backgroundColor:green[50]}} >
                <Grid container   direction="row" justify="space-between" alignItems="center">
                
                <Typography>
                    {CAR.Vehicle_Model}
                </Typography>
                
                <Button variant="contained" color="secondary" onClick={()=> HandleDeRegVec(CAR.Vehicle_ID)}>
                    DeRegister
                </Button>

                
                </Grid>
            </AccordionDetails>
          </Accordion>
        )

    }

    function DisplayListofVehicles(){
        if(success){
            return (
            <div>
                <Typography variant="caption" color="success" >
                    Vehicle removed succesfully
                </Typography>    
            </div>)
        }
        
        if(Vsuccess === 1){
            return (
                <div>
                
                <Grid >
                     {VecLst.map(e => 
                            <Grid>{DisplayCarItem(e)}</Grid>
                     )}
                </Grid>
                
                </div>)
        }else if (Vsuccess === 2){
            return (
                <Typography variant="caption" color="error">
                    {em}
                </Typography>
            )}
       }

    function VehicleDeReg(){
        if(UID !== -1){

            return(
            <div>
                <Card style = {{width:1000,margin:5,backgroundColor:green[300]}} className={classes.root} variant="outlined">
                <CardContent>

                    <Grid align="center" >
                        <Button style = {{width: 800 ,  margin:10 ,backgroundColor:green[800]}} variant="contained"  onClick={()=>{GetListofVehicles()}}>
                            GET LIST OF CARS
                        </Button><br/>
                        {DisplayListofVehicles()}
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
                   De-Register Vehicle
                </Typography>
            </Grid>
            <Grid>
                <Memberverifier  Ddata={[UID,setUID]}/>
            </Grid>
                {VehicleDeReg()}
            <Grid>
            
            </Grid>
            <Typography variant="caption" color="error">
                    {em}
            </Typography>
            </Box>
            </Container>
        </div>  
    )
   
   
};

