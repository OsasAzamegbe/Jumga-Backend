import React, { useContext, useReducer} from 'react';


const AlertContext = React.createContext();

const useAlerts = () => useContext(AlertContext);

const initAlertState = [];

const reducer = (state, action) => {
    switch (action.color) {
        case "RED":
            return [
                ...state,
                {
                color: "alert-red",
                message: action.message
            }];
        case "GREEN":
            return [
                ...state,
                {
                color: "alert-green",
                message: action.message
            }];
        case "BLUE":
            return [
                ...state,
                {
                color: "alert-blue",
                message: action.message
            }];
        case "DELETE":
            return state.filter((_, index) => index !== 0)
        default:
            return state;
    };
};

const AlertProvider = ({children}) => {
    const [alerts, dispatch] = useReducer(reducer, initAlertState);

    const setAlert = (color, message) => {
        dispatch({
            color,
            message
        });

        setTimeout(() =>{
            dispatch({color: "DELETE"})
        }, 5000)
    };

    const value = {
        alerts,
        setAlert
    };

    return(
        <AlertContext.Provider value={value}>
            {children}
        </AlertContext.Provider>
    );
};

export default AlertProvider;
export { useAlerts }