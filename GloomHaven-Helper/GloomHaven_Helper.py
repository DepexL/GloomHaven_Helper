from textwrap import fill
import tkinter
from tkinter import font
from turtle import width
from customtkinter import*
from PIL import Image

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

# GUI Section -------------------------------------------------------------------------

app = CTk()
app.geometry("1200x800")
app.title("GloomHaven-Helper")
app.resizable(width=False, height=False)

set_appearance_mode("dark")

# Starting Page
project_logo = CTkImage(dark_image=Image.open("gloomhaven-logo.png"), size=(1000, 350))
logo_label = CTkLabel(app, image=project_logo, text="")
logo_label.place(relx=0.5, rely=0.25, anchor="center")

frame_1 = CTkFrame(master=app, fg_color="#e5d8ad", height=250, width=750, border_color="#e5aaa7", border_width=2)
frame_1.pack(expand=True, fill="x", pady=200, padx=30, anchor="s")

frame_2 = CTkFrame(master=frame_1, fg_color="#e5d8ad")
frame_2.pack(side=TOP, expand=False, pady=10, padx=30)

# Garamond
desc_label = CTkLabel(master=frame_2, font=("Baskerville Old Face", 17, "bold"), text="Hello and welcome to gloomhaven helper. This app is intended to help you on your adventures by removing the need for character sheets", text_color="black")
desc_label.pack(anchor="s", expand=True, pady=10, padx= 10)

frame_3 = CTkFrame(master=frame_1, fg_color="#e5d8ad")
frame_3.pack(side=BOTTOM, expand=False, pady=10, padx=10)

def click_NewGame():
    print("new progress has been pressed")
    
def click_LoadGame():
    print("Load progress has been pressed")
    
def click_QuitGame():
    print("Quit App Has Been pressed")
    app.quit()
    
    

New_game_btn = CTkButton(master=frame_3, font=("Baskerville Old Face", 18, "bold"), text="New Progress", command=click_NewGame, height=50, fg_color="#9c4541", hover_color="#79312d")
New_game_btn.pack(side=LEFT, anchor="w", expand=True, pady=10, padx=30)

New_game_btn = CTkButton(master=frame_3, font=("Baskerville Old Face", 18, "bold"), text="Load Progress", command=click_LoadGame, height=50, fg_color="#9c4541", hover_color="#79312d")
New_game_btn.pack(side=LEFT, anchor="w", expand=True, pady=10, padx=30)

New_game_btn = CTkButton(master=frame_3, font=("Baskerville Old Face", 18, "bold"), text="Quit App", command=click_QuitGame, height=50, fg_color="#9c4541", hover_color="#79312d")
New_game_btn.pack(side=LEFT, anchor="w", expand=True, pady=20, padx=30)



app.mainloop()









