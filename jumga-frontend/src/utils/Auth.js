import Cookies from 'js-cookies';

//SIGNUP FUNC
const signup = async(body, dispatch) => {
    try{
        const csrf = Cookies.getItem('csrftoken');
        const url = `${process.env.REACT_APP_BACKEND_API_URL}/auth/signup`
        const response = await fetch(url, {
            method: "POST",
            headers: {
                "Accept": "application/json",
                "Content-type": "application/json",
                "X-CSRFToken": csrf
            },
            body: JSON.stringify(body)
        });
        const payload = await response.json();

        if (response.status === 201){
            dispatch({
                type: "LOGIN",
                payload
            })
        };

        return payload;
        
    } catch(err){
        return {status: "error", message: "Something went wrong."}
    }
};

export {
    signup
}