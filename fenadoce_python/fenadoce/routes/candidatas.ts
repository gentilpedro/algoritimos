import { PrismaClient } from '@prisma/client'
import { Router } from 'express'
import { z } from 'zod'

const prisma = new PrismaClient()

const router = Router()

const candidataSchema = z.object({
  nome: z.string().min(10,
    { message: "Nome deve possuir, no mínimo, 10 caracteres" }),
  clube: z.string(),
  idade: z.number().min(16,
    { message: "Idade deve ser igual ou superior a 16 anos"}
  ),  
  sonho: z.string()
})

router.get("/", async (req, res) => {
  try {
    const candidatas = await prisma.candidata.findMany()
    res.status(200).json(candidatas)
  } catch (error) {
    res.status(500).json({ erro: error })
  }
})

router.post("/", async (req, res) => {

  const valida = candidataSchema.safeParse(req.body)
  if (!valida.success) {
    res.status(400).json({ erro: valida.error })
    return
  }

  try {
    const candidata = await prisma.candidata.create({
      data: valida.data
    })
    res.status(201).json(candidata)
  } catch (error) {
    res.status(400).json({ error })
  }
})

router.delete("/:id", async (req, res) => {
  const { id } = req.params

  try {
    const candidata = await prisma.candidata.delete({
      where: { id: Number(id) }
    })
    res.status(200).json(candidata)
  } catch (error) {
    res.status(400).json({ erro: error })
  }
})

router.put("/:id", async (req, res) => {
  const { id } = req.params

  const valida = candidataSchema.safeParse(req.body)
  if (!valida.success) {
    res.status(400).json({ erro: valida.error })
    return
  }

  try {
    const candidata = await prisma.candidata.update({
      where: { id: Number(id) },
      data: valida.data
    })
    res.status(200).json(candidata)
  } catch (error) {
    res.status(400).json({ error })
  }
})

export default router
