class User:
    users = [
        {"username": "youssuf", "password": "123qwe12"},
        {"username": "hussain", "password": "123qwe12"},
    ]

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    def exists(self, username: str) -> bool:
        for user in self.users:
            if username == user["username"]:
                return True

        return False

    def login(self, username: str, password: str) -> bool:
        for user in self.users:
            if username == user["username"] and password == user["password"]:
                return True

        return False
