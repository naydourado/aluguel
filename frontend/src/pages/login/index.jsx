import React, { useState } from "react"
import { useNavigate } from 'react-router-dom'
import { Link } from 'react-router-dom'
import axios from 'axios' // Tem que usa o fetch
import './styles.css'

// o export transforma algo em externo
// default - exportando apenas uma coisa (se for mais de uma, é só export)
// entre o export e o return é JS
// dentro do return é o jsx
export default function Login() {
    // setUser - responsável por armazenar dados na user
    // useState('') - valor que vai iniciar a user (nesse caso, uma lista vazia)
    const [user, setUser] = useState('')
    const [password, setPassword] = useState('')
    const [message, setMessage] = useState('')

    const navigate = useNavigate()

    // arrow function ()=>{} - função anônima
    const logar = async () => {
        try {
            const response = await axios.post(
                'http://127.0.0.1:8000/api/token/',
                {
                    username: user,
                    password: password
                }
            )
            console.log("Deu certo")
            setMessage("Usuário logado")

            localStorage.setItem('token', response.data.access)

            const me = await axios.get('http://127.0.0.1:8000/api/me/')

            if (me.data.is_staff){
                navigate('/homeuser') 
            }else{
                navigate('/homeuser') 
            }
       

        } catch (error) {
            console.log("Error: ", error)
            setMessage("Usuário ou senha inválido...")
        }
    }

    return (
        <div className="container_login">
            <section className="section_1">
                <p className="user">Login</p>

                <p>Usuário</p>
                <input
                    className="caixa"
                    value={user}
                    onChange={(e) => { setUser(e.target.value) }}
                    placeholder="User"
                />

                <p>Senha</p>
                <input
                    className="caixa"
                    value={password}
                    onChange={(e) => { setPassword(e.target.value) }}
                    placeholder="Password"
                />

                <div className="text_1">
                    <p>{message}</p>
                </div>

                <button className="btn_1" onClick={logar}>Enter</button>
            </section>

            <Link to='/cadastro'>Cadastre-se</Link>
        </div>
    )
}