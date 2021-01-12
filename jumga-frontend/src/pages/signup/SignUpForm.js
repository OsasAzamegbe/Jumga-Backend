import React, {useState} from 'react';
import { Link, Redirect } from 'react-router-dom';
import './SignUp.css'

import Form from '../../components/Form';

import validateInput from '../../utils/Validation';


const SignUpForm = () => {

    const [first_name, setfirst_name] = useState("");
    const [last_name, setLast_name] = useState("");
    const [username, setusername] = useState("");
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [password_confirm, setpassword_confirm] = useState("");
    const [loading, setLoading] = useState(false);
    const [errors, setErrors] = useState(null);


    const redirect = (route) => <Redirect to={route}/>;
    
    const first_nameHandler = (e) => {
        setfirst_name(e.target.value);

    };
    
    const last_nameHandler = (e) => {
        setLast_name(e.target.value);

    };
    
    const usernameHandler = (e) => {
        setusername(e.target.value);

    };

    const emailHandler = (e) => {
        setEmail(e.target.value);
        
    };

    const passwordHandler = (e) => {
        setPassword(e.target.value);
        
    };

    const password_confirmHandler = (e) => {
        setpassword_confirm(e.target.value);
        
    };

    const submitHandler = async (e) => {
        e.preventDefault();

        setLoading(true);
        setErrors(null);
        
        const {status} = validateInput({email, password, password_confirm}, setErrors);

        if(status && !errors){
            //SIGNUP FUNC 
            redirect("/dashboard/");     
        };
        
        setLoading(false);
    };

    const formComponentData = [
        {
            label: "First Name",
            onChange: first_nameHandler,
            value: first_name,
            name: 'first_name',
            id: 'first_name',
            type: "text",
            isRequired: true,
            placeholder: 'Your First Name'
        },
        {
            label: "Last Name",
            onChange: last_nameHandler,
            value: last_name,
            name: 'last_name',
            id: 'last_name',
            type: "text",
            isRequired: true,
            placeholder: 'Your Last Name'
        },
        {
            label: "Username",
            onChange: usernameHandler,
            value: username,
            name: 'username',
            id: 'username',
            type: "text",
            isRequired: true,
            placeholder: 'Your Username'
        },
        {
            label: "Email",
            onChange: emailHandler,
            value: email,
            name: 'email',
            id: 'email',
            type: "email",
            isRequired: true,
            placeholder: 'Your Email'
        },
        {
            label: "Password",
            onChange: passwordHandler,
            value: password,
            name: 'password',
            id: 'password',
            type: "password",
            isRequired: true,
            placeholder: 'Your Password'
        },
        {
            label: "Password Confirmation",
            onChange: password_confirmHandler,
            value: password_confirm,
            name: 'password_confirm',
            id: 'password_confirm',
            type: "password",
            isRequired: true,
            placeholder: 'Confirm Password'
        }
    ];

    return (
        <div className="form">
            <header>Sign Up</header>            
            <div className="auth-form-wrapper">
                <Form                
                inputObjectList={formComponentData}
                submitHandler={submitHandler}
                btnLabel="Sign Up"
                isLoading={loading}
                errors={errors} />
            </div>
            <small>Already have an account? <Link to="/signin"><mark>Sign In</mark></Link> </small>
        </div>
    );
};


export default SignUpForm;