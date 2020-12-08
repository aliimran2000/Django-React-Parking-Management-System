
import {  BrowserRouter as Router ,Switch, Route} from "react-router-dom";
//import { Link } from "react-router-dom";
import MenuAppBar from "./Components/MenuAppBar";
import LoginPage from './Views/LoginPage'
import MemberView from './Views/MemberView'
import RegisterMember from './Views/MemberView'








function App() {

  
  return (
    <div className="App">
        <Router>
          <Switch>  
            <Route exact path = "/" >
                <LoginPage/>             
            </Route>

            <MenuAppBar>  
              <Route exact path = "/MemberView">
                  <MemberView/>
              </Route>
              
              <Route exact path = "/RegisterMember">
                  <RegisterMember/>
              </Route>
            </MenuAppBar>
           
          
          </Switch>

        </Router>
    </div>
  );
}

export default App;
