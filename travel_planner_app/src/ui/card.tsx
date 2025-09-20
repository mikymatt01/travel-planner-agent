import React from "react"
import { Role } from "../App"
import ReactMarkdown from 'react-markdown'
import remarkBreaks from 'remark-breaks'

interface CardProps {
    text: string
    role: 'user' | 'bot'
    idx: number
    type?: string
}
const CardMessage = ({ idx, text, role, type }: CardProps) => {
    const markdownStyles = `
        pre {
            white-space: pre-wrap;
            overflow-x: auto;
        }
        .markdown-content p,
        .markdown-content span,
        .markdown-content h3 {
            overflow-wrap: break-word;
            word-break: break-word;
            white-space: normal;
        }
    `
    return (
        <>
            <style>{markdownStyles}</style>
            <div
                style={{
                    justifySelf: role === Role.user ? 'flex-end' : 'flex-start',
                    backgroundColor: role === Role.user ? '#e9e9e980' : 'transparent',
                    borderWidth: role === Role.bot ? 0.5 : 0,
                    marginBottom: 10,
                    marginLeft: role === Role.bot ? 0 : 20,
                    marginRight: role === Role.bot ? 20 : 0,
                    borderRadius: 50,
                    paddingTop: 1,
                    paddingBottom: 1,
                    paddingRight: 6,
                    paddingLeft: 6,
                    overflowWrap: 'break-word',
                    wordWrap: 'break-word',
                    color: type === 'log' ? 'gray' : 'black',
                }}
                key={idx}
            >
                <ReactMarkdown remarkPlugins={[remarkBreaks]}>
                    {text}
                </ReactMarkdown>
            </div>
        </>
    )
}

export default CardMessage