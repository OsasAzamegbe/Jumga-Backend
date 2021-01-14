import React, { useContext, useReducer} from 'react';


const AuthContext = React.createContext();

const useAuth = () => useContext(AuthContext);

const initUserState = {
    isAuthenticated: false,
    user: null,
    merchant: null,
    dispatchRider: null
};

const reducer = (state, action) => {
    switch (action.type) {
        case "LOGIN":
            localStorage.setItem("user", JSON.stringify(action.payload.user));
            localStorage.setItem("merchant", JSON.stringify(action.payload.merchant))
            localStorage.setItem("dispatchRider", JSON.stringify(action.payload.dispatch_rider));
            return {
                ...state,
                isAuthenticated: true,
                user: action.payload.user,
                merchant: action.payload.merchant,
                dispatchRider: action.payload.dispatch_rider
            };
        case "LOGOUT":
            localStorage.clear();
            return {
                ...state,
                isAuthenticated: false,
                user: null,
                merchant: null,
                dispatchRider: null
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