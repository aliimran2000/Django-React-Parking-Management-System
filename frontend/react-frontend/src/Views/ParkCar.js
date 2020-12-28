import React from 'react'
import {Typography} from '@material-ui/core';
import { makeStyles } from '@material-ui/core/styles';

import Grid from '@material-ui/core/Grid';
import { useState } from 'react';
import isLoggedin from '../Utils/LoginCheck'
import Button from '@material-ui/core/Button';
import Container from '@material-ui/core/Container';
import Box from '@material-ui/core/Box';
import axiosInstance from '../Axios/AxiosInstance'
import GoBack from '../Components/GoBack'
import Memberverifier from '../Components/MemberVerifier'
import Card from '@material-ui/core/Card';
import CardContent from '@material-ui/core/CardContent';
import Accordion from '@material-ui/core/Accordion';
import AccordionSummary from '@material-ui/core/AccordionSummary';
import AccordionDetails from '@material-ui/core/AccordionDetails';
import ExpandMoreIcon from '@material-ui/icons/ExpandMore';
import { green, purple } from '@material-ui/core/colors';

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
export default function ParkCar(props){

    const classes = useStyles();
    const [UID,setUID] = useState(-1);
    const [VecLst,SetLst] = useState([{Vehicle_ID: "non",Vehicle_Model: "non"}]);
    const [success,setsuccess] = useState(false);
    const [Vsuccess,setVsuccess] = useState(0);
    const [emss,setemess] = useState("")
    

    
    function DisplayError(){
        return (
            <Typography variant="caption" color="error">
                {emss}
            </Typography>
            )
    }

    //member/getvehiclesdetail/
    //'member/deregistervehicle/'

    function HandleParkVec(Vehicle_ID){
        axiosInstance.post('member/parkvehicle/',{
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
            setemess(error.response.data)
        })
    }

    function GetListofVehicles(){
         axiosInstance.post('member/getvehiclesdetail/',{
            Member_ID:UID
        }).then(
            result=>{
                console.log(result.data.vehicles)    
                setVsuccess(1)
                let L = result.data.vehicles
                SetLst(L)
                
            }
        ).catch(error=>{
            setemess(error.response.data)
            setVsuccess(2)
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
                
                <Button variant="contained" style={{color:green[700]}} onClick={()=> HandleParkVec(CAR.Vehicle_ID)}>
                    Park Car
                </Button>

                
                </Grid>
            </AccordionDetails>
          </Accordion>
        )

    }

    function DisplayListofVehicles(){
        if(success){
            setsuccess(false)
            setVsuccess(1)
            setemess("SUCCESS")
            return (
            <div>
                <Typography variant="caption" style={{color:purple[500]}} >
                    Vehicle Parked Succesfully
                </Typography>    
            </div>)
            
        }
        else {
        
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
                    Unable to Park Vehicle
                </Typography>
            )}
       }
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

    let val = isLoggedin()
    if(val !== "PA" && val !== "PE" ){
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
                   Park Car
                </Typography>
            </Grid>
            <Grid>
                <Memberverifier  Ddata={[UID,setUID]}/>
            </Grid>
                {VehicleDeReg()}
            <Grid>
            

            </Grid>
            {DisplayError()}
            </Box>
            </Container>
        </div>  
    )
   
}