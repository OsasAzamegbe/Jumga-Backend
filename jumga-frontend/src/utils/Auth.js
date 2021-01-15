import Cookies from 'js-cookie';

//SIGNUP FUNC
const signup = async(body) => {
    try{
        const csrf = Cookies.get('csrftoken');
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

        return payload;
        
    } catch(err){
        return {status: "error", message: "Something went wrong."}
    }
};

export {
    signup
}