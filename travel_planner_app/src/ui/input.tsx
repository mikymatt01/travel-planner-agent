import React from "react"

const Input = ({ value, onChange, onKeyDown }: { value: string; onChange: (e: React.ChangeEvent<HTMLInputElement>) => void; onKeyDown: (e: React.KeyboardEvent<HTMLInputElement>) => void }) => {
    return (
        <input
            type="text"
            value={value}
            onChange={onChange}
            onKeyDown={onKeyDown}
            style={{
                width: '100%',
                padding: 10,
                fontSize: 16,
                borderRadius: 5,
                border: '1px solid #ccc',
                boxSizing: 'border-box',
            }}
            placeholder="Type your message..."
        />
    )
}

export default Input