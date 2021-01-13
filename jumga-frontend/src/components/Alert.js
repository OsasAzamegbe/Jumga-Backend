import React from 'react';
import { useAlerts } from '../context/AlertProvider';

const AlertBox = ({message, color}) => {
    return (
    <div className="alert-container">
        <div className={`alert ${color}`}>
            <p className="alert-text" >{message}</p>
        </div>
    </div>
    
)};

const Alert = () => {
    const {alerts} = useAlerts();

    return (
        <>
            {
                alerts.length > 0 ?
                    alerts.map((alert, index) => {
                        return <AlertBox message={alert.message} color={alert.color} key={index} />
                    })
                : null
            }
        </>
    );
};

export default Alert;
