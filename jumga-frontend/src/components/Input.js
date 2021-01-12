import React from 'react';


const Input = ({id, label, onChange, value, name, type, isRequired, placeholder, errors}) => {
    return (
        <div className="form-group">
            <label htmlFor={id} className="form-label">{label}</label>
            <input
            onChange={onChange}
            value={value}
            className='form-input'
            name={name}
            id={id}
            type={type}
            required={isRequired}
            placeholder={placeholder}
            inputMode={type === "number" ? "decimal" : "text"}
            />
            {errors ? <small className="error">{ errors[name]  }</small>: null}
        </div>
    );
};


export default Input;