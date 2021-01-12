import React from 'react';
import './Card.css';


const Card = ({
    childComponent
}) => {

    return(
        <div className="card">
            {childComponent}
        </div>
    )
}

export default Card;