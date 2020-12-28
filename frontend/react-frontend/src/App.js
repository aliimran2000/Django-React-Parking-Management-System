
import {  BrowserRouter as Router ,Switch, Route} from "react-router-dom";
//import { useState } from 'react';
//import { Link } from "react-router-dom";
//import MenuAppBar from "./Components/MenuAppBar";
import LoginPage from './Views/LoginPage'

import RegisterMember from './Views//AdminViews/RegisterMember'
import DeRegisterMember from './Views//AdminViews/DeRegisterMember'
import MemberView from './Views/MemberViews/Member_View'
import AdminView from './Views/AdminViews/Admin_View'
import RenewMembership from './Views/AdminViews/RenewMembership'
import AddVehicle from './Views/AdminViews/AddVehicle'
import RemoveVehicle from './Views/AdminViews/RemoveVehicle'
import PayBills from './Views/AdminViews/PayBills'
import EmployView from './Views/Employ_View'
import ParkCar from './Views/ParkCar'
import UnParkCar from './Views/UnParkCar'

import NotFound from './Views/NotFound'

//import { useHistory } from "react-router-dom";




function App() {

  
  return (
    <div className="App">
        <Router>
          <Switch>  
            <Route exact path = "/" >
                <LoginPage />              
            </Route>
    

            <Route exact path = "/RegisterMember">
                <RegisterMember/>
            </Route>
            <Route exact path = "/DeRegisterMember">
                <DeRegisterMember/>
            </Route>
            <Route exact path = "/RenewMembership">
              <RenewMembership/>
            </Route>
            <Route exact path = "/AddVehicle">
              <AddVehicle/>
            </Route>
            <Route exact path = "/RemoveVehicle">
              <RemoveVehicle/>
            </Route>
            <Route exact path = "/ParkCar">
              <ParkCar/>
            </Route>
            
            <Route exact path = "/UnParkCar">
              <UnParkCar/>
            </Route>




            <Route exact path = "/Member">
                  <MemberView />  
            </Route>
            
            <Route exact path = "/Admin">
                  <AdminView />  
            </Route>

            <Route exact path = "/Employ">
                  <EmployView />  
            </Route>
            
            <Route exact path = "/PayBills">
                  <PayBills />  
            </Route>
            
            
            
            
            
            <Route path="*" component={NotFound} />
          
          
          </Switch>

        </Router>
    </div>
  );
}

export default App;
