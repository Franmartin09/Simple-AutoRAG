'use client'

import { useState } from 'react'
import { Button } from "../components/ui/button"
import { Input } from "../components/ui/input"

export default function ChatInterface() {
  const [message, setMessage] = useState('')

  const handleSubmit = (e) => {
    e.preventDefault()
    // Aquí iría la lógica para enviar el mensaje
    console.log('Mensaje enviado:', message)
    setMessage('')
  }

  return (
    <div className="fixed inset-0 bg-white flex flex-col">
      <div className="flex-1 overflow-auto p-4">
        {/* Aquí irían los mensajes del chat */}
      </div>
      <form onSubmit={handleSubmit} className="p-4 border-t flex">
        <Input
          type="text"
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          placeholder="Escribe un mensaje..."
          className="flex-1 mr-2"
        />
        <Button type="submit">Enviar</Button>
      </form>
    </div>
  )
}