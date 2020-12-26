import React from 'react'
import TextField from '@material-ui/core/TextField'
import Grid from '@material-ui/core/Grid';
import { useState } from 'react';
import Button from '@material-ui/core/Button';
import { makeStyles } from '@material-ui/core/styles';
import MemberVerifier from '../Components/MemberVerifier'
import axiosInstance from '../Axios/AxiosInstance'

import { green} from '@material-ui/core/colors';
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

    const [emss,setemess] = useState("")
    const [UID,setUID] = useState(-1);
    


    function HandleUnPark(){
      let prom
        axiosInstance.post('member/exitvehicle/',{
            Member_ID: UID,
            Vehicle_ID: Vehicle_ID,}
        )
        .then(res =>{
          if(res.status === 200)
            setdone(true)
            setemess("SUCCESS")
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
        <Button style = {{width: 1000 ,  margin:5,backgroundColor:green[500]}} variant="contained"  onClick={() => {setdone(false)}}>
                Vehicle Unparked ...OK 
        </Button>
        )
      }
    }

    

    return(
    <div> 
            <MemberVerifier  Ddata={[UID,setUID]}/>       
            <Grid>
                <TextField style = {{width: 1000 ,  margin:5}} required value={Vehicle_ID} onChange={(event)=>{setVehicle_ID(event.target.value)}}  label="Vehicle_ID" variant="outlined" />
            </Grid>
            
            {DisplayButton()}
    </div>
      )
    

  }

