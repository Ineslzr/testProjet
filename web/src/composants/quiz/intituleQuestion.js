import React from 'react';
import '../../css/quiz/intituleQuestion.css';

function IntituleQuestion(props){
    return(
        <div className='question-text'>
            {props.intitule}
        </div>
    )
}

export default IntituleQuestion;