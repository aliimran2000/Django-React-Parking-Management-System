import './App.css';
import {  BrowserRouter as Router ,Switch, Route} from "react-router-dom";
import { Link } from "react-router-dom";

import LoginPage from './Views/LoginPage'
import MemberView from './Views/MemberView'

import { createMuiTheme } from '@material-ui/core/styles';
import { ThemeProvider } from '@material-ui/styles';
import { purple } from '@material-ui/core/colors';

const theme = createMuiTheme({
  palette: {
    primary: {
      // Purple and green play nicely together.
      main: purple[500],
    },
    secondary: {
      // This is green.A700 as hex.
      main: '#11cb5f',
    },
  },
});



function App() {



  return (
    <div className="App">
  <ThemeProvider theme={theme}>
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
  </ThemeProvider>
    </div>
  );
}

export default App;
