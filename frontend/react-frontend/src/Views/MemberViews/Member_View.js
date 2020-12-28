import React from 'react'
import {Typography} from '@material-ui/core';
import PersistentDrawerLeft from '../../Components/Drawer'
import Card from '@material-ui/core/Card';
import CardContent from '@material-ui/core/CardContent';
import Container from '@material-ui/core/Container';
import Box from '@material-ui/core/Box';
import Accordion from '@material-ui/core/Accordion';
import AccordionSummary from '@material-ui/core/AccordionSummary';
import AccordionDetails from '@material-ui/core/AccordionDetails';
import { makeStyles } from '@material-ui/core/styles';
import Grid from '@material-ui/core/Grid';
import { useState } from 'react';
import Button from '@material-ui/core/Button';
import ExpandMoreIcon from '@material-ui/icons/ExpandMore';
import { green, purple } from '@material-ui/core/colors';
import axiosInstance from '../../Axios/AxiosInstance'
import { DataGrid } from '@material-ui/data-grid';
import ParkingDisplay from '../../Components/ParkingDisplay'
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

//member/getparkedvehiclesdetail/
export default function MemberView(props){
    const classes = useStyles();   
    const [UD,setUD] = useState({username:"notfound"})
    
    const [Bsuccess,setBsuccess] = useState(0);
    const [Blst,SetLst] = useState([{'id':0,'Bill_ID': "none",
    'Membership_ID': "none",
    'Generated_Date': "none",
    'Due_Date': "none",
    'Paid_Status': "none",
    'Bill_Amount': "none",
    'Bill_Type': "none",}]);
    
    const columns = [
        { field: 'id', headerName: 'N.o', width: 100 },  
        { field: 'Bill_Amount', headerName: 'Amount', width: 130 },
        { field: 'Bill_Type', headerName:'Type', width: 130 },
        { field: 'Paid_Status', headerName: 'Paid', width: 300 },
        { field: 'Generated_Date', headerName: 'Generation Date', width: 300 },
        { field: 'Due_Date', headerName: 'Due Date', width: 300 },
        
      ];
      
      

    function GetListofBills(){
        axiosInstance.post('member/getbillsdetail/').then(
           result=>{
               console.log(result.data.vehicles)    
               setBsuccess(1)
               let L = result.data
               //SetLst(L)
               let rows = [];
               for (var i = 0 ; i < L.length; i++ ){
                let Gdata = L[i]
                
                Gdata["id"] = i+1
                rows.push(Gdata)
              }
              console.log(rows)
              SetLst(rows)
              
           }
       ).catch(error=>{
           setBsuccess(2)
       })
   }

   
   

    return(
        <div>
            <PersistentDrawerLeft message={sessionStorage.getItem("USER_NAME")}></PersistentDrawerLeft>
            
            <Container component="main" maxWidth="lg"> 
            <Box spacing={3} m={10}>

            <Accordion >
            <AccordionSummary  onClick={()=>{GetListofBills()}}  expandIcon={<ExpandMoreIcon />}   aria-controls="panel1a-content"   id="panel1a-header"   style={{backgroundColor:green[200]}}>
                <Typography >My Bills</Typography>
            </AccordionSummary>
            <AccordionDetails  style={{backgroundColor:green[50]}} >
                
            <div style={{ height: 400, width: '100%' }}>
                <DataGrid rows={Blst} columns={columns} pageSize={5} />
            </div>
                
                
            </AccordionDetails>
            </Accordion>
            <Accordion >
                <AccordionSummary expandIcon={<ExpandMoreIcon />}   aria-controls="panel1a-content"   id="panel1a-header"   style={{backgroundColor:green[200]}}>
                    <Typography >My Active Parkings</Typography>
                </AccordionSummary>
                <AccordionDetails  style={{backgroundColor:green[50]}} >
                    <ParkingDisplay my/>
                </AccordionDetails>
            </Accordion>
            </Box>
            </Container>
            
            
        </div>
    )

};

