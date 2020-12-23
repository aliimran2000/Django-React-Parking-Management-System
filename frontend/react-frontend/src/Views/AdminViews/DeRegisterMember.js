import React from 'react'
import {Typography} from '@material-ui/core';
import TextField from '@material-ui/core/TextField'
import Grid from '@material-ui/core/Grid';
import { useState } from 'react';
import Button from '@material-ui/core/Button';
import Container from '@material-ui/core/Container';
import Box from '@material-ui/core/Box';
import GoBack from '../../Components/GoBack'
import isLoggedin from '../../Utils/LoginCheck'
import Memberverifier from '../../Components/MemberVerifier'
import { green,red,blue } from '@material-ui/core/colors';
import axiosInstance from '../../Axios/AxiosInstance'




let gotid = true;

export default function DeRegisterMember(){
      

    const [UID,setUID] = useState(-1);
    const [done,setdone] = useState(0);
    const [DregB,showDregB] = useState(false);
    const [success,setsuccess] = useState(0);
    let recmessage = ""


    function HandleDergister(){
      axiosInstance.post('member/deregister/',{Member_ID:UID})
      .then( result=>{
        if(result.status === 201){
          setsuccess(1)
          
        }
      }).catch(error =>{
        setsuccess(2)
        
      })
    
    }

    function DELSUCCESS(){
      if(success===1){
        return (
          <Typography color="primary">
            Member Deletion Succesfull
          </Typography>
        )        
      }else if(success===2){
        return(
        <Typography variant="caption" color="error">
          Unable to delete member please pay your dues first          
        </Typography>
      )
      }else {
        return null
      }
    }

    function Dbutton(){
      if(UID !== -1){
      return (
      <div>
        <Button style = {{width: 1000 ,  margin:5,backgroundColor:red[500]}} variant="contained"  onClick={()=>{HandleDergister()}}>
          DeRegister Member
        </Button>
          
        {DELSUCCESS()}
       </div>
       )
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
                <Typography variant='h3' color="error" style = {{width: 1000 ,  margin:0}} >
                    De-Register Member
                </Typography>
            </Grid>
            <Grid>
                <Memberverifier  Ddata={[UID,setUID]}/>
            </Grid>
            <Grid>
              {Dbutton()}
            </Grid>

            </Box>
            </Container>
        </div>
    )
}