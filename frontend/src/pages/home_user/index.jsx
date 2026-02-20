import React, {useEffect, useState} from 'react'
import axios from 'axios'

export default function HomeUser(){
    const token = localStorage.getItem('token')
    const [usuarios, setUsuarios] = useState([])

    const listar = async ()=>{
        const response = await axios.get('http://127.0.0.1:8000/api/usuarios')
        console.log(response.data)
        setUsuarios(response)

        // console.log(response.data[0]) - traz o valor da posição 
    }

    useEffect(()=>{
        listar()
    },[])
    
    return(
        <div>
            <p>Essa é a página Home!</p>
            <p>Token: {token}</p>

            <table border="1">
                <tr>
                    <th>Nome</th>
                    <th>E-mail</th>
                    <th>Telefone</th>
                    <th>Tipo</th>
                </tr>
                {usuar}
                <tr>
                    <td></td>
                    <td></td>
                </tr>                   
            </table>

        </div>
    )
}