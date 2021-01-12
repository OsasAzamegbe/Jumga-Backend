import React from 'react';
import './Home.css';
import Section from '../../components/Section';
import {sectionOneObj, sectionTwoObj} from './Data';


const Home = () => {
    return (
        <div className="home">
            <div className="home-container">
                <Section
                {...sectionOneObj}
                />
                <Section
                {...sectionTwoObj}
                />
            </div>
        </div>
    )
}

export default Home