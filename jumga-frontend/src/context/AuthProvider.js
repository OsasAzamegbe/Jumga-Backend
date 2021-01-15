import React, { useContext, useReducer} from 'react';
import Cookies from 'js-cookie';


const AuthContext = React.createContext();

const useAuth = () => useContext(AuthContext);

const initUserState = {
    isAuthenticated: false,
    user: null,
    merchant: null,
    dispatch_rider: null
};

const reducer = (state, action) => {
    switch (action.type) {
        case "LOGIN":
            Cookies.set("user", action.payload.user, {expires: 7});
            Cookies.set("merchant", action.payload.merchant, {expires: 7})
            Cookies.set("dispatch_rider", action.payload.dispatch_rider, {expires: 7});
            return {
                ...state,
                isAuthenticated: true,
                user: action.payload.user,
                merchant: action.payload.merchant,
                dispatch_rider: action.payload.dispatch_rider
            };
        case "LOGOUT":
            Cookies.remove("user");
            Cookies.remove("merchant");
            Cookies.remove("dispatch_rider");
            return {
                ...state,
                isAuthenticated: false,
                user: null,
                merchant: null,
                dispatch_rider: null
            };
        default:
            return state;
    };
};

const AuthProvider = ({children}) => {
    const [state, dispatch] = useReducer(reducer, initUserState);
    const value = {
        state,
        dispatch
    };

    return(
        <AuthContext.Provider value={value}>
            {children}
        </AuthContext.Provider>
    );
};

export default AuthProvider;
export { useAuth }