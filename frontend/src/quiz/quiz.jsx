import React, { Component } from 'react'
import axios from "axios"
import qs from "qs"
import 'babel-polyfill';
import Question from "./question"

const API_HOST = "http://localhost:8000"

export default class Quiz extends Component {
    constructor(props) {
        super(props)

        this.state = {
            "username": "",
            "question": {}
        }

        this.getQuestion = this.getQuestion.bind(this)

        if (localStorage.getItem("username")) {
            var username = localStorage.getItem("username")
            this.state.username = username

            this.getQuestion()
        } else {
            this.props.history.push("/login")
        }
    }

    async getQuestion() {
        var data = {
            "cmd": "get_question",
            "username": this.state.username
        }
        let response = await axios({
            method: "post",
            url: `${API_HOST}/question/`,
            data: qs.stringify(data)
        })

        if (response) {
            //alert(response.data.question)
            this.setState({ 
                "question" : response.data.question, 
                "options": response.data.options
            })
            console.log(this.state)
        }
    }

    sendAnswer(user_answer) {
        alert(user_answer)
    }

    render() {
        return (
            <div>
                <Question sendAnswer={this.sendAnswer} question={this.state.question} options={this.state.options} />
            </div>
        )
    }
}