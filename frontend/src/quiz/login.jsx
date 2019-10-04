import React, { Component } from 'react'
import "./login.css"

export default class Login extends Component {
    constructor(props) {
        super(props)

        this.state = {
            "username": ""
        }

        this.inputChange = this.inputChange.bind(this)
        this.startLogin = this.startLogin.bind(this)

    }

    inputChange(e) {
        if (e.target.id == "username") {
            this.setState({"username": e.target.value})
        }
    }

    startLogin(e) {
        var username = this.state.username
        if (username.length > 2) {
            localStorage.setItem("username", username)
            this.props.history.push("/quiz/");
        } else {
            alert("Digite um nome de usuário maior")
        }
    }

    render() {
        return (
            <div className="login_panel">
                <div className="row">
                    <h1>efut</h1>
                    <h4>quiz futebolistico</h4>
                </div>
                <div className="row">
                    <input type="text" placeholder="Nome de usuário..." id="username" className="form-control" onChange={this.inputChange} />
                </div>
                <div className="row">
                    <button onClick={this.startLogin} className="btn btn-light btn-sm" >Jogar</button>
                </div>
            </div>
        )
    }
}