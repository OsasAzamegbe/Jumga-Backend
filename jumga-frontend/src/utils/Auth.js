import axios from 'axios';
import Cookies from 'js-Cookies';

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
        dispatch({
            type: "LOGIN",
            payload
        })
    } catch(err){
        console.log(err)
    }
};

export {
    signup
}