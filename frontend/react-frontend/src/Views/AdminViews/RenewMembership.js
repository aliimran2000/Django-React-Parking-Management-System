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
import { red,green,grey} from '@material-ui/core/colors';
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



export default function Renewmembership(){
   
    const classes = useStyles();
       
    if(!(isLoggedin() === "PA")){
        console.log(isLoggedin()) 
        window.location.href = "/"
    }
    else{
        console.log(isLoggedin())
    }
    
    const [UID,setUID] = useState(-1);
    const [success,setsuccess] = useState(0);
    const [errorMessage,SETem] = useState(' ');

      

    function DisplayRenew(){
        if(UID!==-1){
            if(success){
                return(
                    <Typography align="center" variant="h4" style={{color:green[500]}}>
                        MemberShip Successfully Renewed
                    </Typography>
                )
            }
            return(
                <Grid align="center" >
                        <Button  style = {{width: 450,height:50 ,  margin:15,backgroundColor:green[800],color:grey[100]}} variant="contained"  onClick={()=>{HandleRenewal()}}>
                            Renew MemberShip
                        </Button>
                </Grid>
            )
        }else{
            return null
        }
    }


    function HandleRenewal(){
        axiosInstance.post('member/renewmembership/',{
            Member_ID:UID
        }).then(
            result=>{
                if(result.status === 201){
                    setsuccess(1)
                }
            }
        ).catch(error=>{
            SETem(error.response.data)
            setsuccess(2)
        })
    }


    function RenewMemberShipDisplay(){
        if(UID !== -1){

            if(success===1){
                return ( 
                <Typography align="center" variant="h4" style={{color:green[500]}}>
                    MemberShip Renewed Successfully ... 
                </Typography>)
            }

            if(success===2){
                return ( 
                    <Typography align="left" variant="h7" style={{color:red[500],margin:5}}>
                        {errorMessage}
                    </Typography>)
            }

            return(
            <div>
                <Card align="center" style = {{width:1000,margin:5,backgroundColor:green[100]}} className={classes.root} variant="outlined">
                <CardContent>
                    <Grid align="center">
                        <Typography align="center" variant="h6" style={{color:green[500]}}>
                            MemberShip will only be renewed if Current MemberShip is expired   
                        </Typography>
                    </Grid>
                    <Grid align="center">
                        {DisplayRenew()}
                    </Grid>
                 </CardContent>
                </Card>
            </div>    
            )
        }else{
            return(null)
        }
    }



    

   
    return(
        <div>
            <GoBack/>
            <Container component="main" maxWidth="lg"> 
            <Box spacing={3} m={10}>

            <Grid>
                <Typography align="center" variant='h2' color="primary" style = {{width: 1000 ,  margin:0}} >
                   Renew Membership
                </Typography>
            </Grid>
            <Grid>
                <Memberverifier  Ddata={[UID,setUID]}/>
            </Grid>
                {RenewMemberShipDisplay()}
            <Grid>
            
            </Grid>

            </Box>
            </Container>
        </div>  
    )
   
   
};