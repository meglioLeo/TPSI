class PostModel:
    def __init__(self, userId, id, title, body, link, comment_count):
        self.userId = userId
        self.id = id
        self.title = title
        self.body = body
        self.link = link
        self.comment_count = comment_count
    
    @staticmethod
    def from_json(cls, data):
        return cls(
            userId = data.get("userId"),
            id = data.get("id"),
            title = data.get("title"),
            body = data.get("body"),
            link = data.get("link"),
            comment_count = data.get("comment_count")
        )
        
    def __repr__(self):
        return f"PostModel(userId = {self.userId}, id = {self.id}, title = '{self.title}', body = '{self.body}', link = '{self.link}')"