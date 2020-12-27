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
import { green} from '@material-ui/core/colors';



export default function PayBills(props){
    
    const [UID,setUID] = useState(-1);
    const [selectedbills,setselectedbills] = useState([])
    const [Bill,setbill] = useState(0)
    const [success,setsuccess] = useState(false);
    const [Bsuccess,setBsuccess] = useState(0);
    const [Blst,SetLst] = useState([{'Bill_ID': "none",
    'Membership_ID': "none",
    'Generated_Date': "none",
    'Due_Date': "none",
    'Paid_Status': "none",
    'Bill_Amount': "none",
    'Bill_Type': "none",}]);
    
    
    
    if(!(isLoggedin() === "PA")){
      console.log(isLoggedin()) 
      window.location.href = "/"
    }
    else{
        console.log(isLoggedin())
    }

    const columns = [
      { field: 'id', headerName: 'ID', width: 100 },
      { field: 'Bill_ID', headerName: 'Bill No.', width: 100 },  
      { field: 'Bill_Amount', headerName: 'Amount', width: 130 },
      { field: 'Bill_Type', headerName:'Type', width: 130 },
      { field: 'Membership_ID', headerName: 'M_Code', width: 130 },
      { field: 'Generated_Date', headerName: 'Generation Date', width: 300 },
      { field: 'Due_Date', headerName: 'Due Date', width: 300 },
    ];
    
    
    const rows = [];
    
    
    let selected = []

    function PaySelectedBills(){
      axiosInstance.post('member/paybill/',{
        Bill_IDs:selectedbills,
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
    

    function sumselected(){
      let SUM = 0
      selected.forEach((e)=>{
        SUM = SUM + parseInt(Blst[parseInt(e)-1].Bill_Amount)
        
      }
      )
      return SUM
    }

    function funcselectedbills(){
      let temp = []
      selected.forEach((e)=>{
        temp.push(Blst[parseInt(e)-1].Bill_ID)        
      }
      )
      setselectedbills(temp)
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
          //Gdata["id"] = Blst[i]["Bill_ID"]
          Gdata["id"] = i+1
          rows.push(Gdata)
          
        }
        return (
            <div>
            <div style={{ height: 400, width: '94%' }}>
              <DataGrid rows={rows} columns={columns} pageSize={5} checkboxSelection onSelectionChange={(event)=>{
                selected = (event.rowIds)
                console.log(event.rowIds)
                setbill(sumselected())
                funcselectedbills()
              }}/>
            </div>
            <Button style = {{width: 1000 ,  margin:5 ,backgroundColor:green[300]}} variant="contained"  onClick={()=>{PaySelectedBills()}}>
              Pay Selected Bills TOTAL : {Bill}
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
                <br/>
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

