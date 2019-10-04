import React, { Component } from 'react'
import "./question.css"


export default props => {
    if (props.question.type == "0") {
        if (props.question.hint) {
            var logo = true
        } else {
            var logo = false
        }
        return(
            <div className="question-panel">
                <div className="statement">
                    <h3>{props.question.statement}</h3>
                    <div className="team-img">
                        {logo ? (
                            <img src={props.question.hint} />
                        ) : ("")}
                    </div>
                </div>
                <div className="options row">
                    {props.options.map(option =>(
                        <div className="col-sm-4 option" onClick={() => props.sendAnswer(option)}>
                            {option}
                        </div>
                    ))}
                </div>
            </div>
        )
    } else {
        return(
            <div></div>
        )
    }
}