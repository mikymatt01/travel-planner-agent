// src/WebSocketContext.js

import React, { createContext, useContext, useEffect, useRef, useState } from 'react'

interface WebSocketContextProps {
  status: string
  lastMessage: any | null
  sendMessage: (msg: string) => void
  connect: () => void
  disconnect: () => void
  error: string | null
}
const WebSocketContext = createContext<WebSocketContextProps>({
  status: 'closed',
  lastMessage: null,
  sendMessage: (msg: string) => {},
  connect: () => {},
  disconnect: () => { },
  error: null
});

interface WebSocketProviderProps {
  url: string
  children: React.ReactNode
}

export const WebSocketProvider = ({ url, children }: WebSocketProviderProps) => {
  const socketRef = useRef<WebSocket | null>(null)
  
  const [status, setStatus] = useState('closed')
  const [lastMessage, setLastMessage] = useState<{message: string, type: string} | null>(null)
  const [error, setError] = useState<Event | null>(null)
  const [retry, setRetry] = useState<boolean>(false)

  useEffect(() => {
    setStatus('connecting')
    const ws = new WebSocket(url)
    socketRef.current = ws

    ws.onopen = () => {
      console.log('WebSocket opened')
      setStatus('open')
    }

    ws.onmessage = (event) => {
      try {
        const data = JSON.parse(event.data)
        console.log('WebSocket message received:', data.message)
        setLastMessage(data)
      } catch (e) {
        console.error('WebSocket message parse error', e)
        setLastMessage(event.data)
      }
    }

    ws.onerror = (err) => {
      console.error('WebSocket error', err)
      setError(err)
      setStatus('error')
    }

    ws.onclose = (event) => {
      console.log('WebSocket closed', event.code, event.reason)
      setStatus('closed')
    }

    return () => {
      console.log('Cleaning up websocket')
      if (socketRef.current) {
        socketRef.current.close()
      }
    }
  }, [url, retry])

  const sendMessage = (messageObj: string) => {
    if (socketRef.current && socketRef.current.readyState === WebSocket.OPEN) {
      socketRef.current.send(JSON.stringify({ 'prompt': messageObj }))
    } else {
      console.warn('WebSocket is not open: cannot send message')
    }
  };

  const connect = () => {
    if (!socketRef.current || socketRef.current.readyState === WebSocket.CLOSED) {
      console.log('Reconnecting WebSocket...')
      setRetry((prev) => !prev) // trigger useEffect to reconnect
      setStatus('open')
    }
  }

  const disconnect = () => {
    if (socketRef.current) {
      socketRef.current.close()
    }
  }

  return (
    <WebSocketContext.Provider
      value={{
        status,
        lastMessage,
        sendMessage,
        connect,
        disconnect,
        error: error ? error.toString() : null,
      }}
    >
      {children}
    </WebSocketContext.Provider>
  )
}

export const useWebSocket = () => {
  const context = useContext(WebSocketContext)
  if (context === undefined) {
    throw new Error('useWebSocket must be used inside a WebSocketProvider')
  }
  return context
}
