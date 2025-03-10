import express from 'express'
import routesCandidatas from './routes/candidatas'
import routesClientes from './routes/clientes'
import routesVotos from './routes/votos'

const app = express()
const port = 3000

app.use(express.json())

app.use("/candidatas", routesCandidatas)
app.use("/clientes", routesClientes)
app.use("/votos", routesVotos)

app.get('/', (req, res) => {
  res.send('API do Concurso Rainha da Fenadoce')
})

app.listen(port, () => {
  console.log(`Servidor rodando na porta: ${port}`)
})