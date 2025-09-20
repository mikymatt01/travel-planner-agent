const baseUrl = 'http://127.0.0.1:4000'

export const askToBot = async (message: string) => {
    try {
        const response = await fetch(`${baseUrl}/crewai`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ prompt: message })
        })
        const data = await response.json()
        return data
    } catch (error) {
        console.error('Error:', error)
        throw error
    }
}
