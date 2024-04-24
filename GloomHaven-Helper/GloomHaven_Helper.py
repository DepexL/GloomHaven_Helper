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


    def get_characters(self, player_name):
        return self.players.get(player_name, [])

class Character_Creator:
    def __init__(self, Char_name, Specialty, Health, Level):
        self.Gold = 0
        self.xp = 0
        self.Char_name = Char_name
        self.Specialty = Specialty
        self.Level = Level
        self.Health = Health
        self.Skills = []
        self.Items = []
        
    def add_skill(self, skill_name):
        self.Skills.append(skill_name)

    

Demolitionist = Character_Creator("Demolitionist", "Melee Damage", 8, 1)
Demolitionist.add_skill("Explosive Blitz")
Demolitionist.add_skill("Know Out the support")
Demolitionist.add_skill("Crushing Weight")
Demolitionist.add_skill("Explode")
Demolitionist.add_skill("The big one")
Demolitionist.add_skill("One Two Punch")
Demolitionist.add_skill("Piston Punch")
Demolitionist.add_skill("Windup")
Demolitionist.add_skill("Implode")


player_tracker = PlayerTracker()


player_tracker.add_player("Player1")
player_tracker.add_character("Player1", "Demolitionist")
player_tracker.add_character("Player1", "Character2")


player1_characters = player_tracker.get_characters("Player1")
print("Player1 characters:", player1_characters)

player_tracker.remove_character("Player1", "Demolitionist")
print("Player1 characters:", player1_characters)





