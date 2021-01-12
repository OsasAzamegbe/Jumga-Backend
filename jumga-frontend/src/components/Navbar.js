import React, {useState} from 'react';
import {Link} from 'react-router-dom';
import {FaBars, FaTimes} from 'react-icons/fa';
import './Navbar.css';



const Navbar = () => {

    const [click, setClick] = useState(false);

    const clickHandler = () => setClick(!click);
    const closeMobileMenu = () => setClick(false);
    // const signoutHandler = async () => {
    //     closeMobileMenu();
    //     return <Redirect to="/" />;
    // };

    // const protectedLinks = (
    //     <>
    //         <li className="nav-item">
    //             <Link to="/dashboard/" className="nav-links" onClick={closeMobileMenu} >
    //                 Dashboard
    //             </Link>
    //         </li>
    //     </>
    // )


    return (
        <nav className="navbar">
            <div className={`navbar-container container ${click ? "active" : ""}`}>
                <Link to="/" className="navbar-logo" onClick={closeMobileMenu}  >
                    Jumga
                </Link>
                <div className="menu-icon" onClick={clickHandler} >              
                    {click ? <FaTimes className="fa-times" /> : <FaBars className="fa-bars"/>}
                </div>
    
                <ul className={click ? "nav-menu active" : "nav-menu"}>
                    <li className="nav-item">
                        <Link to="/" className="nav-links" onClick={closeMobileMenu} >
                            Home
                        </Link>
                    </li>
                    <li className="nav-item">
                        <Link to="/signup/" className="nav-links" onClick={closeMobileMenu} >
                            SIGN UP
                        </Link>
                    </li>
                    
                    {/* {
                        user ?
                            <>
                                {protectedLinks}
                                <li className="nav-item">
                                    <Link to="#" className="nav-links" onClick={signoutHandler} >
                                        SIGN OUT
                                    </Link>
                                </li>
                            </>
                            
                        :
                        <>
                            <li className="nav-item">
                                <Link to="/signin/" className="nav-links" onClick={closeMobileMenu} >
                                    SIGN IN
                                </Link>
                            </li>
                            <li className="nav-item">
                                <Link to="/signup/" className="nav-links" onClick={closeMobileMenu} >
                                    SIGN UP
                                </Link>
                            </li>
                        </>                        
                    } */}
                    
                </ul>
            </div>
        </nav>

    );
};

export default Navbar;