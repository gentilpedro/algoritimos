import { PrismaClient } from '@prisma/client'
import { Router } from 'express'
import { z } from 'zod'

const prisma = new PrismaClient()

const router = Router()

const clienteSchema = z.object({
  nome: z.string().min(10,
    { message: "Nome deve possuir, no mínimo, 10 caracteres" }),
  email: z.string().min(10,
    { message: "E-mail deve possuir, no mínimo, 10 caracteres" }),
  cidade: z.string(),
  dataNasc: z.string().date(),
})

router.get("/", async (req, res) => {
  try {
    const clientes = await prisma.cliente.findMany({
      include: { 
        votos: true
      }
    })
    res.status(200).json(clientes)
  } catch (error) {
    res.status(500).json({ erro: error })
  }
})

router.post("/", async (req, res) => {

  const valida = clienteSchema.safeParse(req.body)
  if (!valida.success) {
    res.status(400).json({ erro: valida.error })
    return
  }

  try {
    const cliente = await prisma.cliente.create({
      data: {...valida.data,
        dataNasc: valida.data.dataNasc + "T00:00:00Z"}
    })
    res.status(201).json(cliente)
  } catch (error) {
    res.status(400).json({ error })
  }
})

router.delete("/:id", async (req, res) => {
  const { id } = req.params

  try {
    const cliente = await prisma.cliente.delete({
      where: { id: Number(id) }
    })
    res.status(200).json(cliente)
  } catch (error) {
    res.status(400).json({ erro: error })
  }
})

router.put("/:id", async (req, res) => {
  const { id } = req.params

  const valida = clienteSchema.safeParse(req.body)
  if (!valida.success) {
    res.status(400).json({ erro: valida.error })
    return
  }

  try {
    const cliente = await prisma.cliente.update({
      where: { id: Number(id) },
      data: {...valida.data,
        dataNasc: valida.data.dataNasc + "T00:00:00Z"}
    })
    res.status(200).json(cliente)
  } catch (error) {
    res.status(400).json({ error })
  }
})

export default router
