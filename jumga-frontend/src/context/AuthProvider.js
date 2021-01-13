import React, { useContext } from 'react';


const AuthContext = React.createContext();

const useAuth = () => useContext(AuthContext);

const AuthProvider = ({children}) => {
    const value = {

    };

    return(
        <AuthContext.Provider value={value}>
            {children}
        </AuthContext.Provider>
    );
};

export default AuthProvider;
export { useAuth }