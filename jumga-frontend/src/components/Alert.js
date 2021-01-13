import React from 'react';
import { useAlerts } from '../context/AlertProvider';

const AlertBox = (message, color) => (
    <div className={`alert ${color}`}>
        <p className="alert-text" >{message}</p>
    </div>
);

const Alert = () => {
    const {alerts} = useAlerts();

    return (
        <>
            {
                alerts.length > 0 ?
                    alerts.map((index, alert) => {
                        return <AlertBox message={alert.message} color={alert.color} key={index} />
                    })
                : null
            }
        </>
    );
};

export default Alert;
