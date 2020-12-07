import './App.css';
import {  BrowserRouter as Router ,Switch, Route} from "react-router-dom";
import { Link } from "react-router-dom";

import LoginPage from './Views/LoginPage'
import MemberView from './Views/MemberView'



function App() {
  return (
    <div className="App">
  <Router>
           
    <Switch>  
      <Route exact path = "/" >
          <LoginPage/>             
      </Route>
  
      <Route exact path = "/MemberView">
          <MemberView/>
      </Route>
    
    </Switch>
   </Router>
      
    </div>
  );
}

export default App;
