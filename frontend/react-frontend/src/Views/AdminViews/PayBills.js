import React from 'react'
import {Typography} from '@material-ui/core';
import { makeStyles } from '@material-ui/core/styles';
import { DataGrid } from '@material-ui/data-grid';
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


export default function PayBills(props){
    const classes = useStyles();
    const [UID,setUID] = useState(-1);
    
    const [Blst,SetLst] = useState([{'Bill_ID': "none",
    'Membership_ID': "none",
    'Generated_Date': "none",
    'Due_Date': "none",
    'Paid_Status': "none",
    'Bill_Amount': "none",
    'Bill_Type': "none",}]);
    
    
    const [success,setsuccess] = useState(false);
    const [Bsuccess,setBsuccess] = useState(0);
    
    if(!(isLoggedin() === "PA")){
      console.log(isLoggedin()) 
      window.location.href = "/"
    }
    else{
        console.log(isLoggedin())
    }

    const columns = [
      { field: 'id', headerName: 'Bill N.o', width: 100 },
      { field: 'Bill_Amount', headerName: 'Amount', width: 130 },
      { field: 'Bill_Type', headerName:'Type', width: 130 },
      { field: 'Membership_ID', headerName: 'M_Code', width: 130 },
      { field: 'Generated_Date', headerName: 'Generation Date', width: 300 },
      { field: 'Due_Date', headerName: 'Due Date', width: 300 },
    ];
    
    let id = 0
    const rows = [];
    
    let selected = []

    function PaySelectedBills(){
      axiosInstance.post('member/paybill/',{
        Bill_IDs:selected,
        Payment_Method:"C"
      }).then(
        result=>{
          setsuccess(true)
        }
    ).catch(error=>{
        //setVerror(error.response.data)
        setsuccess(false)
        setBsuccess(2)
    })
    }
    

    

   

    function GetListofBills(){
         axiosInstance.post('member/getunpaidbillsdetail/',{
            Member_ID:UID
        }).then(
            result=>{
                console.log(result.data.vehicles)    
                setBsuccess(1)
                let L = result.data
                SetLst(L)

                
                
            }
        ).catch(error=>{
            //setVerror(error.response.data)
            setBsuccess(2)
        })
    }


  
    function DisplayBills(){
      if(success){
            return (
            
                <Typography variant="caption" color="success" >
                    Bill Paid SuccessFully
                </Typography>    
           )
      }
        
      if(Bsuccess === 1){
        for (var i = 0 ; i < Blst.length; i++ ){
          let Gdata = Blst[i]
          Gdata["id"] = Blst[i]["Bill_ID"]
          rows.push(Gdata)
          console.log(Gdata)
        }
        return (
            <div>
            <div style={{ height: 400, width: '94%' }}>
              <DataGrid rows={rows} columns={columns} pageSize={5} checkboxSelection onSelectionChange={(event)=>{
                selected = (event.rowIds)
                console.log(selected)
              }}/>
            </div>
            <Button style = {{width: 1000 ,  margin:5 ,backgroundColor:green[300]}} variant="contained"  onClick={()=>{PaySelectedBills()}}>
              Pay Selected Bills
            </Button>

            </div>

              )
      }else if (Bsuccess === 2){
          return (
              <Typography variant="caption" color="error">
                  Unable to get Bill Data
              </Typography>
          )}
      }



    function BillPay(){
        if(UID !== -1){

            return(
                <div>
                <Button style = {{width: 1000 ,  margin:5 ,backgroundColor:green[800]}} variant="contained"  onClick={()=>{GetListofBills()}}>
                    Get Bills
                </Button>
                {DisplayBills()}
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
              <Box spacing={3} m={10} direction="center">
              <Grid>
                  <Typography align="center" variant='h2' color="primary" style = {{width: 1000 ,  margin:0}} >
                    View / Pay Bills
                  </Typography>
              </Grid>
              <Grid>
                  <Memberverifier  Ddata={[UID,setUID]}/>
              </Grid>
              <Grid>
                {BillPay()}
              </Grid>
              </Box>           
            </Container>
        </div>  
    )
   
   
};

