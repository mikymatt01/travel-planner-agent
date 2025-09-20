import React from "react"

interface ButtonProps {
    disabled?: boolean
    onClick: () => void
    children?: React.ReactNode
}

const Button = ({ onClick, disabled, children }: ButtonProps) => {
    return (
        <button
            onClick={onClick}
            disabled={disabled}
            style={{
                padding: 10,
                borderRadius: 25,
                border: 'none',
                backgroundColor: disabled ? '#ccc' : '#000',
                color: 'white',
                cursor: disabled ? 'not-allowed' : 'pointer',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
            }}
        >
            {children}
        </button>
    )
}

export default Button