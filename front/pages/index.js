'use client'

import { useState } from 'react'
import Image from 'next/image'
import LoginModal from '../components/LoginModal'
import { Button } from "../components/ui/button"
import { useSession } from "next-auth/react"
import UploadModal from '../components/UploadModal'
import ChatInterface from '../components/ChatInterface'


export default function Home() {
  const [showLoginModal, setShowLoginModal] = useState(false)
  const [showUploadModal, setShowUploadModal] = useState(false)
  const [isUploading, setIsUploading] = useState(false)
  const [showChat, setShowChat] = useState(false)
  const { data: session } = useSession()

  const handleCreate = () => {
    if (session) {
      setShowUploadModal(true)
    } else {
      setShowLoginModal(true)
    }
  }

  const handleUpload = async (file, text) => {
    setIsUploading(true)
    // Aquí iría la lógica para subir el archivo
    // Por ejemplo:
    // const formData = new FormData()
    // formData.append('file', file)
    // formData.append('text', text)
    // const response = await fetch('http://localhost:3000/api/upload', {
    //   method: 'POST',
    //   body: formData
    // })
    // if (response.ok) {
    //   setShowChat(true)
    // }
    setIsUploading(false)
    setShowUploadModal(false)
    setShowChat(true) // Simulamos una carga exitosa
  }

  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
      <div className="z-10 max-w-5xl w-full items-center justify-between font-mono text-sm">
        <h1 className="text-4xl font-bold mb-4">RAG AI Application</h1>
        <p className="mb-4">Esta es una aplicación de Generación Aumentada por Recuperación con IA.</p>
        <Image
          src="/placeholder.svg"
          alt="RAG AI"
          width={500}
          height={300}
          className="mb-4"
        />
        <Button onClick={handleCreate}>Crear</Button>
      </div>

      {showLoginModal && <LoginModal onClose={() => setShowLoginModal(false)} />}
      {showUploadModal && <UploadModal onUpload={handleUpload} onClose={() => setShowUploadModal(false)} />}
      {isUploading && (
        <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center">
          <div className="animate-spin rounded-full h-32 w-32 border-t-2 border-b-2 border-white"></div>
        </div>
      )}
      {showChat && <ChatInterface />}
    </main>
  )
}