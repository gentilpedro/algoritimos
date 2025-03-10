import express from 'express'
import routesCarros from './routes/carros'
import routesUsuarios from './routes/usuarios'
import routesLogin from './routes/login'

const app = express()
const port = 3000

app.use(express.json())

app.use("/carros", routesCarros)
app.use("/usuarios", routesUsuarios)
app.use("/login", routesLogin)

app.get('/', (req, res) => {
  res.send('API de Cadastro de Carros')
})

app.listen(port, () => {
  console.log(`Servidor rodando na porta: ${port}`)
})