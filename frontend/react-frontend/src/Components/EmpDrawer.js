import React from 'react';
import clsx from 'clsx';
import { makeStyles, useTheme } from '@material-ui/core/styles';
import Drawer from '@material-ui/core/Drawer';
import CssBaseline from '@material-ui/core/CssBaseline';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import List from '@material-ui/core/List';
import Typography from '@material-ui/core/Typography';
import Divider from '@material-ui/core/Divider';
import IconButton from '@material-ui/core/IconButton';
import MenuIcon from '@material-ui/icons/Menu';
import ChevronLeftIcon from '@material-ui/icons/ChevronLeft';
import ChevronRightIcon from '@material-ui/icons/ChevronRight';
import ListItem from '@material-ui/core/ListItem';
import ListItemIcon from '@material-ui/core/ListItemIcon';
import ListItemText from '@material-ui/core/ListItemText';
import DriveEtaIcon from '@material-ui/icons/DriveEta';
import HowToRegIcon from '@material-ui/icons/HowToReg';
import AccountCircleIcon from '@material-ui/icons/AccountCircle';
import { green,red,blue } from '@material-ui/core/colors';
import PowerSettingsNewIcon from '@material-ui/icons/PowerSettingsNew';
import LocalParkingIcon from '@material-ui/icons/LocalParking';
import ExitToAppIcon from '@material-ui/icons/ExitToApp';

const drawerWidth = 320;

const useStyles = makeStyles((theme) => ({
  root: {
    display: 'flex',
  },
  appBar: {
    transition: theme.transitions.create(['margin', 'width'], {
      easing: theme.transitions.easing.sharp,
      duration: theme.transitions.duration.leavingScreen,
    }),
  },
  appBarShift: {
    width: `calc(100% - ${drawerWidth}px)`,
    marginLeft: drawerWidth,
    transition: theme.transitions.create(['margin', 'width'], {
      easing: theme.transitions.easing.easeOut,
      duration: theme.transitions.duration.enteringScreen,
    }),
  },
  menuButton: {
    marginRight: theme.spacing(2),
  },
  hide: {
    display: 'none',
  },
  drawer: {
    width: drawerWidth,
    flexShrink: 0,
  },
  drawerPaper: {
    width: drawerWidth,
  },
  drawerHeader: {
    display: 'flex',
    alignItems: 'center',
    padding: theme.spacing(0, 1),
    // necessary for content to be below app bar
    ...theme.mixins.toolbar,
    justifyContent: 'flex-end',
  },
  content: {
    flexGrow: 1,
    padding: theme.spacing(3),
    transition: theme.transitions.create('margin', {
      easing: theme.transitions.easing.sharp,
      duration: theme.transitions.duration.leavingScreen,
    }),
    marginLeft: -drawerWidth,
  },
  contentShift: {
    transition: theme.transitions.create('margin', {
      easing: theme.transitions.easing.easeOut,
      duration: theme.transitions.duration.enteringScreen,
    }),
    marginLeft: 0,
  },
}));


function foradmin(b1){
  
  if(!b1){
    return 
  }

  return (
    <div>
      <Divider />
        <ListItem button onClick={()=>{window.location.href = "/RenewMembership"}}>
              <ListItemIcon><HowToRegIcon style={{ color: blue[500] }}/></ListItemIcon>
              <ListItemText primary="Renew Membership" />
        </ListItem> 
        <ListItem button onClick={()=>{window.location.href = "/RegisterMember"}}>
              <ListItemIcon><AccountCircleIcon  style={{ color: green[500] }} /></ListItemIcon>
              <ListItemText primary="Register Member" />
        </ListItem>
        <ListItem button onClick={()=>{window.location.href = "/DeRegisterMember"}}>
              <ListItemIcon><AccountCircleIcon  style={{ color: red[500] }} /></ListItemIcon>
              <ListItemText primary="De-Register Member" />
        </ListItem>
        <Divider /> 
        <ListItem button onClick={()=>{window.location.href = "/AddVehicle"}}>
              <ListItemIcon><DriveEtaIcon style={{ color: green[500] }}/></ListItemIcon>
              <ListItemText primary="Add Member Vehicle" />
        </ListItem>
        <ListItem button onClick={()=>{window.location.href = "/RemoveVehicle"}}>
              <ListItemIcon><DriveEtaIcon style={{ color: red[500] }}/></ListItemIcon>
              <ListItemText primary="Remove Member Vehicle" />
        </ListItem>
    </div>
  )
}




export default function EmpDrawer(props) {
  const classes = useStyles();
  const theme = useTheme();
  const [open, setOpen] = React.useState(false);


  


  const handleDrawerOpen = () => {
    setOpen(true);
  };

  const handleDrawerClose = () => {
    setOpen(false);
  };

  return (
    <div className={classes.root}>
      <CssBaseline />
      <AppBar
        position="fixed"
        className={clsx(classes.appBar, {
          [classes.appBarShift]: open,
        })}
      >
        <Toolbar>
          <IconButton
            color="inherit"
            aria-label="open drawer"
            onClick={handleDrawerOpen}
            edge="start"
            className={clsx(classes.menuButton, open && classes.hide)}
          >
            <MenuIcon />
          </IconButton>
          <Typography variant="h6" noWrap>
            {sessionStorage.getItem("USER_NAME")}
          </Typography>
        </Toolbar>
      </AppBar>
      <Drawer
        className={classes.drawer}
        variant="persistent"
        anchor="left"
        open={open}
        classes={{
          paper: classes.drawerPaper,
        }}
      >
        <div className={classes.drawerHeader}>
          <IconButton onClick={handleDrawerClose}>
            {theme.direction === 'ltr' ? <ChevronLeftIcon /> : <ChevronRightIcon />}
          </IconButton>
        </div>
        <List>
        {foradmin(props.adminpage)}
        <Divider />
        <ListItem button onClick={()=>{window.location.href = "/ParkCar"}}>
              <ListItemIcon><LocalParkingIcon style={{ color: green[500] }}/></ListItemIcon>
              <ListItemText primary="Park Car" />
        </ListItem>
        <ListItem button onClick={()=>{window.location.href = "/UnParkCar"}}>
              <ListItemIcon><ExitToAppIcon style={{ color: red[500] }}/></ListItemIcon>
              <ListItemText primary="Un-Park Car" />
        </ListItem>
        <Divider />
        <Divider />
        <ListItem button style={{color : green[500] , fontSize: 100 }}>
        <ListItemIcon><PowerSettingsNewIcon /></ListItemIcon>
        <ListItemText primary="LOGOUT" />
        </ListItem>
        
        </List>
      </Drawer>
    
    </div>
  );
}
