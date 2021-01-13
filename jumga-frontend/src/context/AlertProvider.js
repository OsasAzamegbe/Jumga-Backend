import React, { useContext, useReducer} from 'react';


const AlertContext = React.createContext();

const useAlerts = () => useContext(AlertContext);

const initAlertState = [{
    color: "alert-blue",
    message: ""
}];

const reducer = (state, action) => {
    switch (action.type) {
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
        default:
            return state;
    };
};

const AlertProvider = ({children}) => {
    const [alerts, dispatch] = useReducer(reducer, initAlertState);
    const value = {
        alerts,
        dispatch
    };

    return(
        <AlertContext.Provider value={value}>
            {children}
        </AlertContext.Provider>
    );
};

export default AlertProvider;
export { useAlerts }