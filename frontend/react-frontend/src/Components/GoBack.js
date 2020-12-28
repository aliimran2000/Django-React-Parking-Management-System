import Button from '@material-ui/core/Button';
import { useHistory } from "react-router-dom";





export default function GoBack(){
    let history = useHistory();
    
    return (
    <Button color='primary' onClick={() => {history.goBack()}}>
        GO BACK
    </Button>  
    )
}

