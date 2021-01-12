import React from 'react';
import {Link} from 'react-router-dom';
import './Section.css'


const Section = ({
    lightBg, topLine, lightText, lightTextDesc, headLine, description, buttonLabel, img, alt, imgStart, hideButton, buttonLink
}) => {

    return(
        <div className={lightBg ? 'home__home-section' : 'home__home-section darkBg'}>
            <div className="container">
                <div 
                className="row home__home-row"
                style={{display: 'flex', flexDirection: imgStart ? 'row-reverse' : 'row'}}>
                    <div className="col">
                        <div className="home__home-text-wraper">
                            <div className={lightBg ? "top-line" : "top-line light-red"}>{topLine}</div>
                            <h1 className={lightText ? 'heading' : 'heading dark'}>{headLine}</h1>
                            <p className={lightTextDesc ? 'home__home-subtitle' : 'home__home-subtitle dark'}>{description}</p>
                            {!hideButton ? 
                            <Link to={buttonLink}>
                                <button className="btn">{buttonLabel}</button>
                            </Link> : ""
                            }

                        </div>
                    </div>
                    <div className="col">
                        <div className="home__home-img-wrapper">
                            <img className="home__home-img" src={img} alt={alt}/> 
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default Section;