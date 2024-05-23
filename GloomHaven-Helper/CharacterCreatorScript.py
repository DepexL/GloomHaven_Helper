# Sukurti Leveling sistema!!!!

class Character_Creator:
    def __init__(self, Char_name, Specialty, Health, Level):
        self.Gold = 0
        self.xp = 0
        self.Char_name = Char_name
        self.Specialty = Specialty
        self.Level = Level
        self.Health = 8
        self.Skills = []
        self.Items = []
        
    def add_skill(self, skill_name):
        if skill_name not in self.Skills: 
            self.Skills.append(skill_name)
        
class Voidwarden_class(Character_Creator):
    def __init__(self, Char_name, Specialty, Health, Level, Mana):
        super().__init__(Char_name, Specialty, Health, Level)
        self.Mana = Mana  # New attribute specific to Character_Class


    def add_skill(self, skill_name):
        if skill_name not in self.Skills: 
            self.Skills.append(skill_name)
        else:
            print(f"{skill_name} already exists in the skills list.")


    def display_mana(self):
        return f"Mana: {self.Mana}"
    
class Hatchet_class(Character_Creator):
    def __init__(self, Char_name, Specialty, Health, Level, Stamina):
        super().__init__(Char_name, Specialty, Health, Level)
        self.Stamina = Stamina 


    def add_skill(self, skill_name):
        if skill_name not in self.Skills: 
            self.Skills.append(skill_name)
        else:
            print(f"{skill_name} already exists in the skills list.")


    def display_mana(self):
        return f"Mana: {self.Stamina}"
    
class RedGuard_class(Character_Creator):
    def __init__(self, Char_name, Specialty, Health, Level, Rage):
        super().__init__(Char_name, Specialty, Health, Level)
        self.Rage = Rage 


    def add_skill(self, skill_name):
        if skill_name not in self.Skills: 
            self.Skills.append(skill_name)
        else:
            print(f"{skill_name} already exists in the skills list.")


    def display_mana(self):
        return f"Mana: {self.Mana}"
    

class Demolitionist_class(Character_Creator):
    def __init__(self, Char_name, Specialty, Health, Level, GunPowder):
        super().__init__(Char_name, Specialty, Health, Level)
        self.GunPowder = GunPowder  


    def add_skill(self, skill_name):
        if skill_name not in self.Skills: 
            self.Skills.append(skill_name)
        else:
            print(f"{skill_name} already exists in the skills list.")


    def display_mana(self):
        return f"Mana: {self.Mana}"
    

    
# Klasiu kurimas kuriuos zaidejas gales pasirinkti
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

