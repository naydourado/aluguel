import React, { useEffect, useState } from 'react'
import axios from 'axios'

export default function HomeUser() {
    const [user, setUser] = useState([]) //se não colocar colchetes, vai dar ruim, porque são muitos usuários
    const [inputText, setInputText] = useState("")
    const [userFiltrado, setUserFiltrado] = useState("")
    const token = localStorage.getItem('token')

    const listar = async () => {
        try {
            const response = await axios.get('http://127.0.0.1:8000/api/usuarios',
                {
                headers: {Authorization: `Bearer ${token}`}
                }
            )
            
        } catch (error) {
            console.log("Erro: ", error)
        }
        // console.log(response.data[0]) - traz o valor da posição 
    }

    const pesquisar = async () => {
        try {
            const response = await axios.get(`http://127.0.0.1:8000/api/usuarios/?nome=${inputText}`,
                {
                    headers: {Authorization: `Bearer ${token}`}
                }   
            )
            setUserFiltrado(response.data)
        } catch (error) {
            console.log("Erro: ", error)
        }
    }

    useEffect(() => {
        listar()
    }, [])

    return (
        <div className='content1'>
            <p>Essa é a página Home!</p>

            <table border="1">
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Nome</th>
                        <th>E-mail</th>
                        <th>Telefone</th>
                        <th>Tipo</th>
                    </tr>
                </thead>
                <tbody>
                    {user.map((u) => (
                        <tr key={u.id}>
                            <td>{u.id}</td>
                            <td>{u.nome}</td>
                            <td>{u.email}</td>
                            <td>{u.telefone}</td>
                            <td>{u.tipo}</td>
                        </tr>
                    ))}
                </tbody>
            </table>

            <input type="text" placeholder='Digite o nome' value={inputText} onChange={(e) => setInputText(e.target.value)} />
            <button onClick={pesquisar}>Pesquisar</button>

            {userFiltrado.length != 0 ?
                <table border="1">
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Nome</th>
                        <th>E-mail</th>
                        <th>Telefone</th>
                        <th>Tipo</th>
                    </tr>
                </thead>
                <tbody>
                    {userFiltrado.map(item => (
                        <tr key={item.id}>
                            <td>{item.id}</td>
                            <td>{item.nome}</td>
                            <td>{item.email}</td>
                            <td>{item.telefone}</td>
                            <td>{item.tipo}</td>
                        </tr>
                    ))}
                </tbody>
            </table>                
                : ""}
        </div>
    )
}