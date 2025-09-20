from crewai.memory.storage.interface import Storage

class CustomStorage(Storage):
    def __init__(self):
        self.memories = []

    def save(self, value, metadata=None, agent=None):
        self.memories.append({
            "value": value,
            "context": value,
            "metadata": metadata,
            "agent": agent
        })

    def search(self, query, limit=10, score_threshold=0.5):
        # Implement your search logic here
        result = [m for m in self.memories if query.lower() in str(m["value"]).lower()]
        if len(result) == 0:
            if len(self.memories) > 0:
                print('memories: ', self.memories[-4:])
                return self.memories[-4:]
            else:
                print('empty memories')
                return []
        return result

    def reset(self):
        self.memories = []
