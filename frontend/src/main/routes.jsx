import React from "react"
import { HashRouter, Route, Redirect } from "react-router-dom"
import Login from "../quiz/login"
import Quiz from "../quiz/quiz"

export default props => (
    <HashRouter>
        <Route path="/login" component={Login} />
        <Route path="/quiz" component={Quiz} />
    </HashRouter>
)