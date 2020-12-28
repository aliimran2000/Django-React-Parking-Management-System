import React from 'react'
import { useState } from 'react';
import Box from '@material-ui/core/Box';
import axiosInstance from '../Axios/AxiosInstance'
import Button from '@material-ui/core/Button';
import { green} from '@material-ui/core/colors';
import Grid from '@material-ui/core/Grid';
import ButtonGroup from '@material-ui/core/ButtonGroup';
import { Typography } from '@material-ui/core';

export default function ParkingDisplay(props){
    
    
    const [ParkData,setParkData] = useState([{'Vehicle_ID': '',
     'In_Time': '', 
     'Out_Time': '', 
     'Slot_Given': '',}])


    function getparkedvehicles(){
        axiosInstance.post('employee/getallparkingsdetail/').then(
            result=>{
                //console.log(result.data)
                setParkData(result.data)
                
            
            }
        ).catch(error=>{
            console.log(error)
        })
    }

    function getmyparkedvehicles(){
        axiosInstance.post('member/getparkedvehiclesdetail/').then(
            result=>{
                //console.log(result.data)
                setParkData(result.data.parkedVehicles)
                
            
            }
        ).catch(error=>{
            console.log(error)
        })
    }



    
    

    function displayCar(Car){        
        return (
            <div>
            <ButtonGroup color="primary" aria-label="outlined primary button group">
                <Button>{Car.Vehicle_ID}</Button>
                <Button>{Car.Slot_Given}</Button>
                <Button>{Car.In_Time}</Button>
            </ButtonGroup>
            </div>
        )
    }

    function displayparkedcars(){
        
        if(ParkData.length === 0){
            if(!props.my){
            return ( <Box >
                <Typography variant="h3" align="center" color="primary">
                    LOT EMPTY
                </Typography>
            </Box>
            )
        }else {
            return ( <Box >
                <Typography variant="h3" align="center" color="primary">
                    No Car Parked :)
                </Typography>
            </Box>
            )
        }
        }
        return (
            <Box >
            <Grid container direction="column" justify="center" alignItems="center">
                {ParkData.map(car=> (
                    <div style={{margin:10}}>{displayCar(car)}</div>
                ))}
            </Grid>
            </Box>
        )
    }
    
    if(!props.my){
    return(
        
        <div>
            
           
          
                <Box color="secondary.main" spacing={2} m={10} >
                
                <Grid align="center">
                <Button style = {{width: 400 ,  margin:10 ,backgroundColor:green[300]}} variant="contained" onClick={()=>{getparkedvehicles()}}>
                    Refresh Parking
                </Button>
                </Grid>
                <Grid>
                    {displayparkedcars()}
                </Grid>

                </Box>
           
            
        </div>
    )}
    else{
        return(
        
            <div>
                
               
              
                    
                    <Grid align="center">
                    <Button style = {{width: 400 ,  margin:10 ,backgroundColor:green[300]}} variant="contained" onClick={()=>{getmyparkedvehicles()}}>
                        Refresh Parking
                    </Button>
                    </Grid>
                    <Grid>
                        {displayparkedcars()}
                    </Grid>
    
                    
               
                
            </div>
        )
    }

};

