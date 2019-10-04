import React, { Component } from 'react'
import axios from "axios"
import qs from "qs"
import 'babel-polyfill';

const URL = "http://localhost:8000"

export default class Quiz extends Component {
    constructor(props) {
        super(props)

        if (localStorage.getItem("username")) {
            var username = localStorage.getItem("username")

        } else {
            this.props.history.push("/login")
        }
    }

    render() {
        return (
            <div>

            </div>
        )
    }
}