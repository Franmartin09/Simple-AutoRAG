'use client'

import { useState } from 'react'
import { Button } from "../components/ui/button"
import { Input } from "../components/ui/input"
import { Textarea } from "../components/ui/textarea"
import { Dialog, DialogContent, DialogHeader, DialogTitle } from "../components/ui/dialog"

export default function UploadModal({ onUpload, onClose }) {
  const [file, setFile] = useState(null)
  const [text, setText] = useState('')

  const handleSubmit = (e) => {
    e.preventDefault()
    if (file) {
      onUpload(file, text)
    }
  }

  return (
    <Dialog open={true} onOpenChange={onClose}>
      <DialogContent>
        <DialogHeader>
          <DialogTitle>Subir archivo</DialogTitle>
        </DialogHeader>
        <form onSubmit={handleSubmit} className="space-y-4">
          <Input
            type="file"
            onChange={(e) => setFile(e.target.files?.[0] || null)}
            required
          />
          <Textarea
            placeholder="Ingrese texto adicional"
            value={text}
            onChange={(e) => setText(e.target.value)}
          />
          <Button type="submit">Subir</Button>
        </form>
      </DialogContent>
    </Dialog>
  )
}