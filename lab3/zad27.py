class User:
    def __init__(self):
        self.users = {}

    def register(self, username, password):
        if username not in self.users:
            self.users[username] = password
            print(f"Użytkownik {username} został zarejestrowany.")
        else:
            print("Nazwa użytkownika jest już zajęta.")

    def login(self, username, password):
        if username in self.users and self.users[username] == password:
            print(f"Użytkownik {username} zalogowany.")
        else:
            print("Nieprawidłowa nazwa użytkownika lub hasło.")

user_system = User()
user_system.register("janek", "haslo123")
user_system.login("janek", "haslo123")
user_system.login("janek", "zlehaslo")
