import axios from 'axios';
import Cookies from 'js-cookies';

//SIGNUP FUNC
const signup = async(body, dispatch) => {
    try{
        const csrf = Cookies.getItem('csrftoken');
        const config = {
            "Accept": "application/json",
            "Content-type": "application/json",
            "X-CSRFToken": csrf
        };
        const url = `${process.env.REACT_APP_BACKEND_API_URL}/auth/signup`
        const response = await axios.post(url, body, config);
        const payload = await response.json();
        if (response.status === 201){
            dispatch({
                type: "LOGIN",
                payload
            })
        } else{
            console.log(payload)
        };

        return payload;
        
    } catch(err){
        console.log(err)
    }
};

export {
    signup
}