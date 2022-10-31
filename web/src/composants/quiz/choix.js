import React from 'react';
import '../../css/quiz/choix.css';

function Choix(props){
    return(
        <button key={props.index} onClick={props.handleAnswerOptionClick}>{props.intitule}</button>
    )
}

export default Choix;