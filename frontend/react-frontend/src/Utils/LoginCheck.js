

export default function isLoggedin(){
    try {
        let T = sessionStorage.getItem('TYPE')
        return T;    
    }catch{
        return false;
    }
    
    
}