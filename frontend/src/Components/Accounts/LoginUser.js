import React, { Component } from 'react'
import {Row} from 'reactstrap';


class LoginUser extends Component {
    constructor(props) {
        super(props)
        this.state = {
            password : ''
        }
    }
    handlePasswordChange = (e) => {
        this.setState({
            password : e.target.value
        })
    }
    render() {
        return (
            <div>
                <form onSubmit={e => this.props.handleLogin(e, {
                    username : this.props.username, 
                    password : this.state.password
                })} >
                    <Row>
                        <label htmlFor="username" >Username</label>
                        <input type="text"
                        onChange={this.props.handleLoginChange} 
                        value={this.props.username} 
                        name="username"
                        id="username"
                        placeholder="Username" />
                    </Row>
                    <Row>
                        <label htmlFor="password" >Password</label>
                        <input type="password"
                        onChange={this.handlePasswordChange} 
                        value={this.state.password} 
                        name="password"
                        id="password"
                        placeholder="Password" />
                    </Row>
                    <button type='submit'>Login</button>
                </form>
            </div>
        )
    }
}

export default LoginUser
