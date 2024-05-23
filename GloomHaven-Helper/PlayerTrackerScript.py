class PlayerTracker:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.players = {}
        return cls._instance

    def add_player(self, player_name):
        if player_name not in self.players:
            self.players[player_name] = []

    def remove_player(self, player_name):
        if player_name in self.players:
            del self.players[player_name]

    def add_character(self, player_name, character_name):
        if player_name in self.players:
            self.players[player_name].append({'name': character_name})

    def remove_character(self, player_name, character_name):
        if player_name in self.players:
            characters = self.players[player_name]
            for character in characters:
                if character['name'] == character_name:
                    characters.remove(character)
                    break

    def get_players_and_characters(self):
        return self.players

    def get_characters(self, player_name):
        return self.players.get(player_name, [])

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            for player, characters in self.players.items():
                file.write(f"{player}\n")
                for character in characters:
                    file.write(f"  {character['name']}\n")

    def load_from_file(self, filename):
        self.players = {}
        with open(filename, 'r') as file:
            lines = file.readlines()
            player = None
            for line in lines:
                if not line.startswith("  "):
                    player = line.strip()
                    self.players[player] = []
                else:
                    character_name = line.strip()
                    self.players[player].append({'name': character_name})
