# Other imports
'''
from email.policy import default
from textwrap import fill
import tkinter
from tkinter import font
from turtle import width
'''
from customtkinter import*
from PIL import Image

# Scripts
import customtkinter
import PlayerTrackerScript
from Designs import ButtonDesignScript
from Designs import TextDesignScript

# Starting Page

class App(customtkinter.CTk):
    def __init__(self):
        
        self.player_tracker = PlayerTrackerScript.PlayerTracker()
        self.button_designer = ButtonDesignScript.btn_design()
        self.text_designer = TextDesignScript.text_design()
        
        # Programos Atrodymas ir iskvietimas
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

        self.desc_label = self.text_designer.default_text(
            "Hello and welcome to gloomhaven helper. This app is intended to help you on your adventures by removing the need for character sheets",
            self.frame_2, 17)
        self.desc_label.pack(anchor="s", expand=True, pady=10, padx= 10)

        self.frame_3 = CTkFrame(master=self.frame_1, fg_color="#e5d8ad")
        self.frame_3.pack(side=BOTTOM, expand=False, pady=10, padx=10)
        
        self.New_game_btn = self.button_designer.default_button("New Progress", self.frame_3, self.click_NewGame)
        self.New_game_btn.pack(side=LEFT, anchor="w", expand=True, pady=10, padx=30)

        self.New_game_btn = self.button_designer.default_button("Load Progress", self.frame_3, self.click_LoadGame)
        self.New_game_btn.pack(side=LEFT, anchor="w", expand=True, pady=10, padx=30)

        self.New_game_btn = self.button_designer.default_button("Quit App", self.frame_3, self.click_QuitGame)
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
        
        self.desc_label = self.text_designer.default_text("For starters lets choose how many player will be playing", self.frame_2, 32)
        self.desc_label.pack(anchor="s", expand=True, pady=10, padx= 10)    
        
        self.combobox_players = customtkinter.CTkComboBox(master=self.frame_2, values=["Solo Game", "2 Player Game", "3 Player Game",
                                                                                       "4 Player Game"], font=("Baskerville Old Face", 22, "bold")
                                                          , command=self.combobox_callback_players, width=500, fg_color="#e5d8ad", text_color="black",
                                                          dropdown_font=("Baskerville Old Face", 22, "bold"))
        self.combobox_players.set("Solo Game")
        self.combobox_players.pack(expand=True, pady=10, padx= 10)            

        self.Next_btn_1 = self.button_designer.default_button("Text", self.frame_2, self.Next_btn_1)
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
        self.desc_label = self.text_designer.default_text("Player Name:", self.frame_3, 22)
        self.desc_label.pack(side=LEFT, anchor="n", pady=20, padx=30)    
        
        self.entry_name = CTkEntry(master=self.frame_3, placeholder_text="Start typing...", fg_color="#e5d8ad",font=("Baskerville Old Face", 22, "bold"), text_color="black" , width=200 )
        self.entry_name.pack(side=LEFT, anchor="n", pady=20, padx=30)
        
        self.desc_label = self.text_designer.default_text("How many characters: ", self.frame_3, 22)
        self.desc_label.pack(side=LEFT, anchor="n", pady=20, padx=30)    
        
        self.combobox_players = customtkinter.CTkComboBox(master=self.frame_3, values=["1", "2", "3",
                                                                                       "4"], font=("Baskerville Old Face", 22, "bold")
                                                          , command=self.combobox_callback_charNumb, width=1, fg_color="#e5d8ad", text_color="black",
                                                          dropdown_font=("Baskerville Old Face", 22, "bold"), hover=True)
        self.combobox_players.set("1")
        self.combobox_players.pack(expand=True, pady=10, padx= 10)      

        
        self.btn_submit = self.button_designer.default_button("Submit", self.frame_4, self.click_handler1)
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









