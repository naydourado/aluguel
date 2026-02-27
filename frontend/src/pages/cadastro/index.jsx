import React, { useState } from "react"
import { useNavigate } from 'react-router-dom'
import axios from 'axios' 
import './styles.css'

export default function Cadastro() {
    const [user, setUser] = useState('')
    const [email, setEmail] = useState('')
    const [password, setPassword] = useState('')
    const [telefone, setTelefone] = useState('')
    const [tipo, setTipo] = useState('')
    const [message, setMessage] = useState('')

    const navigate = useNavigate()

    const cadastrar = async () => {
        try {
            const response = await axios.post('http://127.0.0.1:8000/api/register/',
                {
                    "username": user,
                    "email": email,
                    "password": password,
                    "telefone": telefone,
                    "tipo": tipo
                }
            )

            const resp = await axios.post('http://127.0.0.1:8000/api/token/',
                    {
                        "username": user,
                        "password": password,
                    }
                )
                localStorage.setItem('token', resp.data.access)
                navigate('/homeuser')

        } catch (error) {
             console.log(error.response?.data)
        }
    }    

    return (
        <div className="container_login">
            <section className="section_1">
                <p className="user">Cadastro</p>

                <p>Usuário</p>
                <input
                    className="caixa"
                    value={user}
                    onChange={(e) => { setUser(e.target.value) }}
                    placeholder="User"
                />

                <p>Email</p>
                <input
                    className="caixa"
                    value={email}
                    onChange={(e) => { setEmail(e.target.value) }}
                    placeholder="Email"
                />

                <p>Telefone</p>
                <input
                    className="caixa"
                    value={telefone}
                    onChange={(e) => { setTelefone(e.target.value) }}
                    placeholder="Email"
                />

                 <p>Tipo</p>
                <select
                    className="caixa"
                    value={tipo}
                    onChange={(e) => setTipo(e.target.value)}
                >
                    <option value="">Selecione</option>
                    <option value="LOCADOR">Locador</option>
                    <option value="LOCATARIO">Locatario</option>
                </select>

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

                <button className="btn_1" onClick={cadastrar}>Cadastrar</button>

            </section>
        </div>
    )
}