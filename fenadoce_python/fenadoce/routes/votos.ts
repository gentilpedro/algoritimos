import { PrismaClient } from '@prisma/client'
import { Router } from 'express'
import { z } from 'zod'
import nodemailer from "nodemailer";

const prisma = new PrismaClient()

const router = Router()

const transporter = nodemailer.createTransport({
  host: "sandbox.smtp.mailtrap.io",
  port: 587,
  secure: false, // true for port 465, false for other ports
  auth: {
    user: "ae4cc5c3908728",
    pass: "765d02632275d3",
  },
})

const votoSchema = z.object({
  clienteId: z.number(),
  candidataId: z.number(),
  justificativa: z.string().optional()
})

async function enviaEmail(email: string, nome: string, candidata: string) {
  let mensagem = "<h3>Concurso Rainha da Fenadoce</h3>"
  mensagem += `<h4>Estimado(a): ${nome}</h4>`
  mensagem += "<h4>Obrigado por participar de nosso concurso...</h4>"
  mensagem += `<h4>Você votou na Candidata: ${candidata}</h4>`
  
  // send mail with defined transport object
  const info = await transporter.sendMail({
    from: '"Concurso Rainha da Fenadoce" <concursofenadoce@gmail.com>', // sender address
    to: email, // list of receivers
    subject: "Confirmação Voto Rainha da Fenadoce", // Subject line
    text: "Obrigado pelo voto...", // plain text body
    html: mensagem
  });

  console.log("Message sent: %s", info.messageId);
  // Message sent: <d786aa62-4e0a-070a-47ed-0b0666549519@ethereal.email>
}

router.get("/", async (req, res) => {
  try {
    const votos = await prisma.voto.findMany({
      include: {
        cliente: true,
        candidata: true
      }
    })
    res.status(200).json(votos)
  } catch (error) {
    res.status(500).json({ erro: error })
  }
})

router.post("/", async (req, res) => {

  const valida = votoSchema.safeParse(req.body)
  if (!valida.success) {
    res.status(400).json({ erro: valida.error })
    return
  }

  try {
    const [voto, candidata] = await prisma.$transaction([
      prisma.voto.create({ data: valida.data }),
      prisma.candidata.update({
        where: { id: valida.data.candidataId },
        data: { numVotos: { increment: 1 } }
      })
    ])

    // obtém os dados do cliente e candidata
    const dadoCliente = await prisma.cliente.findUnique(
      { where: { id: valida.data.clienteId } })
    const dadoCandidata = await prisma.candidata.findUnique(
      { where: { id: valida.data.candidataId } })

    enviaEmail(dadoCliente?.email as string, 
               dadoCliente?.nome as string, 
               dadoCandidata?.nome as string)  

    res.status(201).json({ voto, candidata })
  } catch (error) {
    res.status(400).json({ error })
  }
})

router.delete("/:id", async (req, res) => {
  const { id } = req.params

  try {

    // obtém os dados do voto (no caso, o id da candidata - para subtrair)
    const dadoVoto = await prisma.voto.findUnique({ where: { id: Number(id) } })

    const [voto, candidata] = await prisma.$transaction([
      prisma.voto.delete({ where: { id: Number(id) } }),
      prisma.candidata.update({
        where: { id: dadoVoto?.candidataId },
        data: { numVotos: { decrement: 1 } }
      })
    ])

    res.status(201).json({ voto, candidata })
  } catch (error) {
    res.status(400).json({ erro: error })
  }
})

export default router
