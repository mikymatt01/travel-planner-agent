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
        if len(self.memories) > 0:
            return self.memories[-4:]
        else:
            return []

    def reset(self):
        self.memories = []
