class TaskModel:
    def __init__(self, userId, id, title, completed):
        self.userId = userId
        self.id = id
        self.title = title
        self.completed = completed
        
    @classmethod
    def from_json(cls, data):
        return cls(
        userId = data.get("userId"),
        id = data.get("id"),
        title = data.get("title"),
        completed = data.get("completed")
        )

    def __repr__(self):
        return f"TaskModel(userId = {self.userId}, id = {self.id}, title = '{self.title}', completed = {self.completed})"