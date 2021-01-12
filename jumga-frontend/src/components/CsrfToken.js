import React, {useEffect} from 'react';
import axios from 'axios';


const CsrfToken = () => {
    useEffect(() =>{
        const loadCsrf = async () =>{
            const url = `${process.env.REACT_APP_BACKEND_API_URL}/getcsrf`;
            await axios.get(url);
        };

        loadCsrf();
    }, []);

    return (
        <div>
            <input type="hidden"/>
        </div>
    );
};

export default CsrfToken;