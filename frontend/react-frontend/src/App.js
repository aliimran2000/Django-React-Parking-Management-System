
import {  BrowserRouter as Router ,Switch, Route} from "react-router-dom";
import { useState } from 'react';
//import { Link } from "react-router-dom";
//import MenuAppBar from "./Components/MenuAppBar";
import LoginPage from './Views/LoginPage'

import RegisterMember from './Views/RegisterMember'
import MemberView from './Views/MemberView'
import NotFound from './Views/NotFound'






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

            <Route exact path = "/MemberView">
                  <MemberView />  
            </Route>
            
            
            
            
            <Route path="*" component={NotFound} />
          
          
          </Switch>

        </Router>
    </div>
  );
}

export default App;
