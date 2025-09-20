import React, { useEffect, useState } from 'react'
import CardMessage from './card'
import { TextField } from '@mui/material'
import { Loader, SendIcon, Dot } from 'lucide-react'
import Button from './button'
import { useWebSocket } from '../hook/webSocketContext'

export enum Role {
  user = 'user',
  bot = 'bot',
}

interface Message {
  role: Role
  text: string
  type?: string
}

const defaultMessages: Message[] = []

function ChatBot() {
    const { status, lastMessage, sendMessage, connect, disconnect } = useWebSocket()
    const [isLoading, setIsLoading] = useState(false)
    const [messages, setMessages] = useState<Message[]>(defaultMessages)
    const [message, setMessage] = useState<Message>({
        role: Role.user,
        text: ''
    })
    const handleClick = async () => {
      setIsLoading(true)
      if (message.text === '') {
          setIsLoading(false)
          return
      }
      setMessages(() => [...messages, message])
      setMessage({
          role: Role.user,
          text: ''
      })
      sendMessage(message.text)
      setIsLoading(false)
    }
  
  useEffect(() => {
    if (!lastMessage) return
    setMessages((prev) => {
      const history = prev.filter((p) => p.type !== 'log')
      return [
        ...history,
        { role: Role.bot, text: lastMessage.message, type: lastMessage.type }
      ]
    })
  }, [lastMessage])

  const handleConnection = () => {
    if (status === 'closed') {
      connect()
    } else {
      disconnect()
    }
  }
  const color = React.useMemo(() => {
    return status === 'open' ? 'green' : status === 'closed' ? 'red' : 'orange'
  }, [status])
  return (
    <div style={{
        flex: 1,
        justifyContent: 'center',
        alignItems: 'center',
        display: 'flex',
        flexDirection: 'column',
        backgroundColor: 'white',
        height: '100%',
        paddingLeft: '25%',
        paddingRight: '25%',
        paddingTop: 30
      }}>
        <div style={{ display: 'flex', flexDirection: 'row', alignItems: 'center' }}>
          <h1>Travel Support Agent</h1>
          <Dot size={100} color={color} onClick={handleConnection} />
        </div>
        <div style={{
          flex: 1,
          width: '100%',
          paddingBottom: 150,
          overflowY: 'auto',
          position: 'relative'
        }}>
          {
              messages.map(({text, role, type}, idx) => (
                  <CardMessage text={text} role={role} idx={idx} key={idx} type={type} />
              ))
          }
        </div>
        <div style={{ display: 'flex', border: '1px solid lightgrey', position: 'fixed', alignItems: 'center', flexDirection: 'row', width: '50%', bottom: 50, borderRadius: 25, padding: 10, backgroundColor: 'white', marginTop: 20 }}>
          <div style={{ flex: 1, minHeight: 30, marginLeft: 10, marginRight: 10 }}>
              <TextField
                  variant="standard"
                  placeholder="Write the input here..."
                  multiline
                  minRows={2}
                  fullWidth
                  InputProps={{
                      disableUnderline: true
                  }}
                  sx={{
                      '& textarea': {
                          maxHeight: '150px',
                          overflowY: 'auto',
                      },
                  }}
                  value={message.text}
                  onChange={(e) => setMessage({ ...message, text: e.target.value })}
              />
          </div>
            <Button disabled={isLoading} onClick={handleClick}>
              {isLoading ? <Loader /> : <SendIcon />}
            </Button>
        </div>
      </div>
  )
}

export default ChatBot
