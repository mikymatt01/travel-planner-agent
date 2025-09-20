import React from 'react'
import './App.css'
import { WebSocketProvider } from './hook/webSocketContext'
import ChatBot from './ui/chatbot'

export enum Role {
  user = 'user',
  bot = 'bot',
}

const wsUrl = `ws://localhost:4000/ws/chat`

function App() {
  return (
    <WebSocketProvider url={wsUrl}>
      <ChatBot />
    </WebSocketProvider>
  )
}

export default App
