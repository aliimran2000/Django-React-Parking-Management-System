import React from 'react'
import TextField from '@material-ui/core/TextField'
import Grid from '@material-ui/core/Grid';
import { useState } from 'react';
import Button from '@material-ui/core/Button';
import { makeStyles } from '@material-ui/core/styles';
import Card from '@material-ui/core/Card';
import CardContent from '@material-ui/core/CardContent';
import axiosInstance from '../Axios/AxiosInstance'


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


export default function UnParkComponent(props){
    
    const [Member_ID,setUser] = useState("");
    const [Vehicle_ID,setVehicle_ID] = useState("");
    const [done,setdone] = useState(false);
    const [errorm,seterrorm] = useState(false);
   
    


    function HandleUnPark(){
      let prom
        axiosInstance.post('member/exitvehicle/',{
            Member_ID: Member_ID,
            Vehicle_ID: Vehicle_ID,}
        )
        .then(res =>{
          if(res.status === 200)
            setdone(true)
          }
        ).catch(
            seterrorm(true)
        )
          
        

    }

    function DisplayButton(){
      if(!done){

        if(errorm){
          return (
            <Button style = {{width: 1000 ,  margin:5}} variant="contained" color="secondary" onClick={() => {setdone(false);seterrorm(false)}}>
                Error Unparking Car ... Try Again 
          </Button>
          )
        }

        return (
          <Button style = {{width: 1000 ,  margin:5}} variant="contained" color="primary" onClick={() => {HandleUnPark()}}>
                  UnPark 
          </Button>
        )
      }
      else if(done){
        return (
        <Button style = {{width: 1000 ,  margin:5}} variant="contained" color="secondary" onClick={() => {setdone(false)}}>
                Vehicle Unparked ...OK 
        </Button>
        )
      }
    }

    

    return(
    <div>
            <Grid>
                <TextField style = {{width: 1000 ,  margin:5}} required value={Member_ID} onChange={(event)=>{setUser(event.target.value)}} label="Member ID" variant="outlined" />
            </Grid>
            
            <Grid>
                <TextField style = {{width: 1000 ,  margin:5}} required value={Vehicle_ID} onChange={(event)=>{setVehicle_ID(event.target.value)}}  label="Vehicle_ID" variant="outlined" />
            </Grid>
            
            {DisplayButton()}
    </div>
      )
    

  }

