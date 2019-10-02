import React, { Component } from 'react'

export default class Login extends Component {
    constructor(props) {
        super(props)

    }

    render() {
        return (
            <div className="card">
                <div className="row">
                    <div className="col-sm-12">
                        <input type="text" placeholder="Nome de usuário..." id="username" className="form-control" />
                    </div>
                    <div className="col-sm-12">
                        <button className="btn btn-light btn-sm" >Jogar</button>
                    </div>
                </div>
            </div>
        )
    }
}