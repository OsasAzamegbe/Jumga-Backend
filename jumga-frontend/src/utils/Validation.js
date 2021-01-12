const setErrorsObj = (setErrors, key, error) => {
    setErrors(errors => {
        const newErrors = {...errors};
        newErrors[key] = error;
        return newErrors;
    });
};

const validatePassword = (password) => {
    const re = /^(?=.*[0-9])(?=.*[A-Z])(?=.*[!@#$%^&*/\\():-~`{}[\]])[a-zA-Z0-9!@#$%^&*/\\():-~`{}[\]]{8,100}$/;
    return re.test(String(password));
}

const validateEmail = (email) => {
    const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(String(email).toLowerCase());
};

const validateInput = (options, setErrors) => {
    const keys = Object.keys(options);
    let status = true;

    if (keys.includes("email")) {

        const email = options.email.trim();

        if (!email){
            setErrorsObj(setErrors, "email", "Field cannot be empty.");
            status= false;
        } else if (!validateEmail(email)) {
            setErrorsObj(setErrors, "email", "Email address is invalid.");
            status= false;
        };
    };

    if (keys.includes("password")) {

        const password = options.password.trim();

        if (!password){
            setErrorsObj(setErrors, "password", "Field cannot be empty.");
            status= false;
        } else if (!validatePassword(password)){
            setErrorsObj(setErrors, "password", "Password must be 8 - 100 characters long and must contain at least: one uppercase letter, one digit and one special character.");
            status= false;
        };
    };

    if (keys.includes("password_confirm")){
        const password_confirm = options.password_confirm.trim();
        if (!options.password || options.password !== password_confirm){
            setErrorsObj(setErrors, "password_confirm", "Passwords do not match.");
            status= false;
        } 
    };

    const validated = Object.assign({}, ...Object.keys(options).map(key => !["password", "password_confirm"].includes(key) 
    ? ({ [key]: options[key].trim()})
    : ({ [key]: options[key]})));

    return {validated, status};

};

export default validateInput;