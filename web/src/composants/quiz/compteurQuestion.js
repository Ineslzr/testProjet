import React from 'react';
import '../../css/quiz/compteurQuestion.css';

function CompteurQuestion(props){
    return(
        <div className='question-count'>
			<span>Question {props.currentQuestion}</span>/{props.nbQuestions}
        </div>
    )
}

export default CompteurQuestion;