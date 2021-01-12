import React from 'react';
import './SignUp.css'

import Card from '../../components/Card';
import SignUpForm from './SignUpForm';


const SignUp = () => {
    return (
        <div className="page" >
            <header>CREATE AN ACCOUNT TODAY</header>            
            <Card childComponent={<SignUpForm/>} />
        </div>               
    );
};

export default SignUp;