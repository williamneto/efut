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
        this.sendAnswer = this.sendAnswer.bind(this)

        if (localStorage.getItem("username")) {
            var username = localStorage.getItem("username")
            this.state.username = username

            this.getQuestion()
        } else {
            this.props.history.push("/")
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
            this.setState({ 
                "question" : response.data.question, 
                "options": response.data.options
            })
        }
    }

    async sendAnswer(user_answer) {
        var data = {
            "cmd": "answer_question",
            "username": this.state.username,
            "question_id": this.state.question.question_id,
            "answer": user_answer
        }
        let response = await axios({
            method: "post",
            url: `${API_HOST}/question/`,
            data: qs.stringify(data)
        })
        if (response) {
            if (response.data.correct) {
                alert("Acertou!")
            } else {
                alert("Errou!")
            }
        }

        this.getQuestion()
    }

    render() {
        return (
            <div>
                <Question sendAnswer={this.sendAnswer} question={this.state.question} options={this.state.options} />
            </div>
        )
    }
}