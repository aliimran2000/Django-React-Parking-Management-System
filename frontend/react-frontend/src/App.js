
import {  BrowserRouter as Router ,Switch, Route} from "react-router-dom";
//import { useState } from 'react';
//import { Link } from "react-router-dom";
//import MenuAppBar from "./Components/MenuAppBar";
import LoginPage from './Views/LoginPage'

import RegisterMember from './Views//AdminViews/RegisterMember'
import DeRegisterMember from './Views//AdminViews/DeRegisterMember'
import MemberView from './Views/MemberViews/Member_View'
import AdminView from './Views/AdminViews/Admin_View'
import AddVehicle from './Views/AdminViews/AddVehicle'
import EmployView from './Views/Employ_View'
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

            <Route>
              <AddVehicle/>
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
            

            
            
            
            
            
            <Route path="*" component={NotFound} />
          
          
          </Switch>

        </Router>
    </div>
  );
}

export default App;
