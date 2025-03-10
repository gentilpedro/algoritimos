import { Combustivel, PrismaClient } from '@prisma/client'
import { Router } from 'express'
import { z } from 'zod'
import { verificaToken } from '../middlewares/verificaToken'

const prisma = new PrismaClient()
const router = Router()

const carroSchema = z.object({
  modelo: z.string(),
  marca: z.string().min(3,
    { message: "Marca deve ter, no mínimo, 3 caracteres" }),
  ano: z.number().min(1980,
    { message: "Ano deve ser superior ou igual a 1980" }),
  preco: z.number().positive(
    { message: "Preço não pode ser negativo" }),
  cor: z.string().optional(),
  combustivel: z.nativeEnum(Combustivel).optional(),
  km: z.number().optional(),
  usuarioId: z.number()
})

router.get("/", async (req, res) => {
  try {
    const carros = await prisma.carro.findMany({
      orderBy: { id: 'desc' },
      // select: {
      //   id: true,
      //   modelo: true,
      //   ano: true,
      //   preco: true
      // }
    })
    res.status(200).json(carros)
  } catch (error) {
    res.status(500).json({ erro: error })
  }
})

router.post("/", verificaToken, async (req, res) => {

  const valida = carroSchema.safeParse(req.body)
  if (!valida.success) {
    res.status(400).json({ erro: valida.error })
    return
  }

  try {
    const carro = await prisma.carro.create({
      data: valida.data
    })
    res.status(201).json(carro)
  } catch (error) {
    res.status(400).json({ error })
  }
})

router.delete("/:id", verificaToken, async (req: any, res) => {
  const { id } = req.params

  try {
    const excluido = await prisma.carro.findUnique({
      where: { id: Number(id) }
    })

    if (excluido) {
      await prisma.carroArquivado.create({
        data: { ...excluido, usuarioId: req.userLogadoId }
      })
    }

    const carro = await prisma.carro.delete({
      where: { id: Number(id) }
    })

    await prisma.log.create({
      data: {
        descricao: `Exclusão do Carro: ${id}`,
        complemento: `Funcionário: ${req.userLogadoNome}`,
        usuarioId: req.userLogadoId
      }
    })

    res.status(200).json(carro)
  } catch (error) {
    res.status(400).json({ erro: error })
  }
})

router.put("/:id", verificaToken, async (req, res) => {
  const { id } = req.params

  const valida = carroSchema.safeParse(req.body)
  if (!valida.success) {
    res.status(400).json({ erro: valida.error })
    return
  }

  try {
    const carro = await prisma.carro.update({
      where: { id: Number(id) },
      data: valida.data
    })
    res.status(201).json(carro)
  } catch (error) {
    res.status(400).json({ error })
  }
})

// quando quisermos alterar apenas algum/alguns atributo(s)
router.patch("/:id", async (req, res) => {
  const { id } = req.params

  const partialCarroSchema = carroSchema.partial()

  const valida = partialCarroSchema.safeParse(req.body)
  if (!valida.success) {
    res.status(400).json({ erro: valida.error })
    return
  }

  try {
    const carro = await prisma.carro.update({
      where: { id: Number(id) },
      data: valida.data
    })
    res.status(201).json(carro)
  } catch (error) {
    res.status(400).json({ error })
  }
})

router.get("/pesquisa/:modelo", async (req, res) => {
  const { modelo } = req.params
  try {
    const carros = await prisma.carro.findMany({
      where: { modelo: { contains: modelo } }
    })
    res.status(200).json(carros)
  } catch (error) {
    res.status(500).json({ erro: error })
  }
})

export default router
