from textwrap import fill
import tkinter
from tkinter import font
from turtle import width
from customtkinter import*
from PIL import Image
import customtkinter

# Žaidėjų ir žmogeliukų kūrimas - Funkcijos ir t.t.

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
        return f"Mana: {self.Mana}"
    
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
    def __init__(self, Char_name, Specialty, Health, Level, Mana):
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

# testai
player_tracker = PlayerTracker()


player_tracker.add_player("Player1")
player_tracker.add_character("Player1", "Demolitionist")
player_tracker.add_character("Player1", "Character2")


player1_characters = player_tracker.get_characters("Player1")
print("Player1 characters:", player1_characters)

player_tracker.remove_character("Player1", "Demolitionist")
print("Player1 characters:", player1_characters)

# GUI Section -------------------------------------------------------------------------




# Starting Page
class App(customtkinter.CTk):
    def __init__(self):
        
        self.player_tracker = PlayerTracker()
        
        # Programos Atrodymas
        super().__init__()
        self.geometry("1200x800")
        self.title("GloomHaven-Helper")
        self.resizable(width=False, height=False)
        set_appearance_mode("dark")
        self.create_page1()
        
# Pirmas pradinis puslapis - Pradzia

    def create_page1(self):
        
        project_logo = CTkImage(dark_image=Image.open("gloomhaven-logo.png"), size=(1000, 350))        

        self.logo_label = CTkLabel(self, image=project_logo, text="")
        self.logo_label.place(relx=0.5, rely=0.25, anchor="center")

        self.frame_1 = CTkFrame(master=self, fg_color="#e5d8ad", height=250, width=750, border_color="#e5aaa7", border_width=2)
        self.frame_1.pack(expand=True, fill="x", pady=200, padx=30, anchor="s")

        self.frame_2 = CTkFrame(master=self.frame_1, fg_color="#e5d8ad")
        self.frame_2.pack(side=TOP, expand=False, pady=10, padx=30)

        self.desc_label = CTkLabel(master=self.frame_2, font=("Baskerville Old Face", 17, "bold"), text="Hello and welcome to gloomhaven helper. This app is intended to help you on your adventures by removing the need for character sheets", text_color="black")
        self.desc_label.pack(anchor="s", expand=True, pady=10, padx= 10)

        self.frame_3 = CTkFrame(master=self.frame_1, fg_color="#e5d8ad")
        self.frame_3.pack(side=BOTTOM, expand=False, pady=10, padx=10)
        
        self.New_game_btn = CTkButton(master=self.frame_3, font=("Baskerville Old Face", 18, "bold"), text="New Progress", command=self.click_NewGame, height=50, fg_color="#9c4541", hover_color="#79312d")
        self.New_game_btn.pack(side=LEFT, anchor="w", expand=True, pady=10, padx=30)

        self.New_game_btn = CTkButton(master=self.frame_3, font=("Baskerville Old Face", 18, "bold"), text="Load Progress", command=self.click_LoadGame, height=50, fg_color="#9c4541", hover_color="#79312d")
        self.New_game_btn.pack(side=LEFT, anchor="w", expand=True, pady=10, padx=30)

        self.New_game_btn = CTkButton(master=self.frame_3, font=("Baskerville Old Face", 18, "bold"), text="Quit App", command=self.click_QuitGame, height=50, fg_color="#9c4541", hover_color="#79312d")
        self.New_game_btn.pack(side=LEFT, anchor="w", expand=True, pady=20, padx=30)

    def click_NewGame(self):
        print("new progress has been pressed")
        self.frame_1.pack_forget()
        self.logo_label.place_forget()
        self.create_page2()

    def click_LoadGame(self):
        print("Load progress has been pressed")
        self.frame_1.pack_forget()
        self.logo_label.place_forget()
        
    
    def click_QuitGame(self):
        print("Quit App Has Been pressed")
        self.quit()

 # Antras puslapis - New Game How many players
    def create_page2(self):
        self.Players = "1"        

        self.frame_1 = CTkFrame(master=self, fg_color="#e5d8ad", height=1200, width=750, border_color="#e5aaa7", border_width=2)
        self.frame_1.pack(expand=True, fill="both", pady=50, padx=30, anchor="s")
        
        self.frame_2 = CTkFrame(master=self.frame_1, fg_color="#e5d8ad", height=1200, width=750, border_color="#e5aaa7", border_width=0)
        self.frame_2.pack(expand=True, fill="x", pady=0, padx=30)
        
        self.desc_label = CTkLabel(master=self.frame_2, font=("Baskerville Old Face", 32, "bold"), text="For starters lets choose how many player will be playing", text_color="black")
        self.desc_label.pack(anchor="s", expand=True, pady=10, padx= 10)    
        
        self.combobox_players = customtkinter.CTkComboBox(master=self.frame_2, values=["Solo Game", "2 Player Game", "3 Player Game",
                                                                                       "4 Player Game"], font=("Baskerville Old Face", 22, "bold")
                                                          , command=self.combobox_callback_players, width=500, fg_color="#e5d8ad", text_color="black",
                                                          dropdown_font=("Baskerville Old Face", 22, "bold"))
        self.combobox_players.set("Solo Game")
        self.combobox_players.pack(expand=True, pady=10, padx= 10)      
        
        self.Next_btn_1 = CTkButton(master=self.frame_2, font=("Baskerville Old Face", 18, "bold"), text="Next", command=self.Next_btn_1, height=50, fg_color="#9c4541", hover_color="#79312d")
        self.Next_btn_1.pack(side=LEFT, expand=True, pady=20, padx=30)
        

    
    def combobox_callback_players(self, choice):
        if choice == "Solo Game":
            self.Players = 1
        if choice == "2 Player Game":
            self.Players = 2
        if choice == "3 Player Game":
            self.Players = 3
        if choice == "4 Player Game":
            self.Players = 4    
    
    def Next_btn_1(self):
        print("Choose button has been pressed")
        self.frame_1.pack_forget()
        self.create_page3()

# Trecias puslapis - Zaidejas ir Zmogeliukai
    def create_page3(self):
        self.frame_1 = CTkFrame(master=self, fg_color="#e5d8ad", height=1200, width=750, border_color="#e5aaa7", border_width=2)
        self.frame_1.pack(expand=True, fill="both", pady=(50, 20), padx=30, anchor="n")  # Adjusted pady and anchor
    
        self.frame_2 = CTkFrame(master=self.frame_1, fg_color="#e5d8ad", height=1200, width=750, border_color="#e5aaa7", border_width=0)
        self.frame_2.pack(expand=True, fill="x", pady=0, padx=30)
        
        self.frame_3 = CTkFrame(master=self.frame_1, fg_color="#ECCE5C", border_color="black", border_width=2)
        self.frame_3.place(relx=0.5, rely=0.30, anchor="n")  # Center vertically within frame_1
        
        self.frame_4 = CTkFrame(master=self.frame_1, fg_color="#e5d8ad")
        self.frame_4.place(relx=0.5, rely=0.40, anchor="n")  # Center vertically within frame_1
    
        self.desc_label = CTkLabel(master=self.frame_2, font=("Baskerville Old Face", 32, "bold"), text="Now Lets Create Players And Characters", text_color="black")
        self.desc_label.pack(anchor="n", expand=True, pady=(10, 400), padx= 10)    

# Solo Game selection stage 1.
        self.desc_label = CTkLabel(master=self.frame_3, font=("Baskerville Old Face", 22, "bold"), text="Player Name:", text_color="black")
        self.desc_label.pack(side=LEFT, anchor="n", pady=20, padx=30)    
        
        self.entry_name = CTkEntry(master=self.frame_3, placeholder_text="Start typing...", fg_color="#e5d8ad",font=("Baskerville Old Face", 22, "bold"), text_color="black" , width=200 )
        self.entry_name.pack(side=LEFT, anchor="n", pady=20, padx=30)
        
        self.desc_label = CTkLabel(master=self.frame_3, font=("Baskerville Old Face", 22, "bold"), text="How many characters: ", text_color="black")
        self.desc_label.pack(side=LEFT, anchor="n", pady=20, padx=30)    
        
        self.combobox_players = customtkinter.CTkComboBox(master=self.frame_3, values=["1", "2", "3",
                                                                                       "4"], font=("Baskerville Old Face", 22, "bold")
                                                          , command=self.combobox_callback_charNumb, width=1, fg_color="#e5d8ad", text_color="black",
                                                          dropdown_font=("Baskerville Old Face", 22, "bold"), hover=True)
        self.combobox_players.set("1")
        self.combobox_players.pack(expand=True, pady=10, padx= 10)      

        
        self.btn_submit = CTkButton(master=self.frame_4, font=("Baskerville Old Face", 18, "bold"), text="Submit", command=self.click_handler1, height=50, fg_color="#9c4541", hover_color="#79312d")
        self.btn_submit.pack(side=LEFT, anchor="n", pady=20, padx=30)
        

        self.charNumb = int(self.combobox_players.get())

    def combobox_callback_charNumb(self, choice):
        self.charNumb = int(choice)
    
    def click_handler1(self):
        name = self.entry_name.get()
        self.player_tracker.add_player(name)
        for i in range(self.charNumb):
            # add characters Names and skills and level
            character_name = f"Character{i+1}"
            self.player_tracker.add_character(name, character_name)
        characters = self.player_tracker.get_characters(name)
        print(f"Name: {name}, Characters: {characters}")
        
# Solo Game selection stage 2.
    

# x puslapis - Load Game
    def create_page4(self):
        pass


    
  

app = App()
app.mainloop()









