class User:
    def __init__(self, id, name, email, password):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
    
    def __str__(self):
        return f"User: {self.name}, {self.email}"
    