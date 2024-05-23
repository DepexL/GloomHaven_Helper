# Other imports
from tkinter import *
from customtkinter import *
from PIL import Image
from tkinter import messagebox

# Scripts
import customtkinter
import PlayerTrackerScript
from Designs import ButtonDesignScript
from Designs import TextDesignScript


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.player_tracker = PlayerTrackerScript.PlayerTracker()
        self.button_designer = ButtonDesignScript.btn_design()
        self.text_designer = TextDesignScript.text_design()
        

        self.setup_window()
        self.create_page1()
        
    def setup_window(self):
        self.geometry("1200x800")
        self.title("GloomHaven-Helper")
        self.resizable(width=False, height=False)
        set_appearance_mode("dark")
        
    
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
        self.desc_label.pack(anchor="s", expand=True, pady=10, padx=10)

        self.frame_3 = CTkFrame(master=self.frame_1, fg_color="#e5d8ad")
        self.frame_3.pack(side=BOTTOM, expand=False, pady=10, padx=10)
        
        self.new_game_btn = self.button_designer.default_button("New Progress", self.frame_3, self.click_NewGame)
        self.new_game_btn.pack(side=LEFT, anchor="w", expand=True, pady=10, padx=30)

        self.load_game_btn = self.button_designer.default_button("Load Progress", self.frame_3, self.click_LoadGame)
        self.load_game_btn.pack(side=LEFT, anchor="w", expand=True, pady=10, padx=30)

        self.quit_game_btn = self.button_designer.default_button("Quit App", self.frame_3, self.click_QuitGame)
        self.quit_game_btn.pack(side=LEFT, anchor="w", expand=True, pady=20, padx=30)

    def click_NewGame(self):
        print("new progress has been pressed")
        self.frame_1.pack_forget()
        self.logo_label.place_forget()
        self.create_page2()

    def click_LoadGame(self):
        print("Load progress has been pressed")
        self.player_tracker.load_from_file("savefile.txt")
        self.frame_1.pack_forget()
        self.logo_label.place_forget()
        self.load_game()
        self.create_page4()
        
    def load_game(self):
        self.create_page4()
        messagebox.showinfo("Load Game", "Game progress loaded successfully.")
        
    
    def click_QuitGame(self):
        print("Quit App Has Been pressed")
        self.quit()

    def create_page2(self):
        self.Players = 1     

        self.frame_1 = CTkFrame(master=self, fg_color="#e5d8ad", height=1200, width=750, border_color="#e5aaa7", border_width=2)
        self.frame_1.pack(expand=True, fill="both", pady=50, padx=30, anchor="s")
        
        self.frame_2 = CTkFrame(master=self.frame_1, fg_color="#e5d8ad", height=1200, width=750, border_color="#e5aaa7", border_width=0)
        self.frame_2.pack(expand=True, fill="x", pady=0, padx=30)
        
        self.desc_label = self.text_designer.default_text("For starters, let's choose how many players will be playing", self.frame_2, 32)
        self.desc_label.pack(anchor="s", expand=True, pady=10, padx=10)    
        
        self.combobox_players = customtkinter.CTkComboBox(master=self.frame_2, values=["Solo Game", "2 Player Game", "3 Player Game", "4 Player Game"],
                                                          font=("Baskerville Old Face", 22, "bold"), command=self.combobox_callback_players,
                                                          width=500, fg_color="#e5d8ad", text_color="black", dropdown_font=("Baskerville Old Face", 22, "bold"))
        self.combobox_players.set("Solo Game")
        self.combobox_players.pack(expand=True, pady=10, padx=10)            

        self.next_btn_1 = self.button_designer.default_button("Next", self.frame_2, self.next_btn_1)
        self.next_btn_1.pack(side=LEFT, expand=True, pady=20, padx=30)

    def combobox_callback_players(self, choice):
        players_map = {
            "Solo Game": 1,
            "2 Player Game": 2,
            "3 Player Game": 3,
            "4 Player Game": 4
        }
        self.Players = players_map.get(choice, 1)
        print(self.Players)
    
    def next_btn_1(self):
        print("Choose button has been pressed")
        self.frame_1.pack_forget()
        self.create_page3()

    def create_page3(self):
        
        self.frame_1 = CTkFrame(master=self, fg_color="#e5d8ad", height=1200, width=750, border_color="#e5aaa7", border_width=2)
        self.frame_1.pack(expand=True, fill="both", pady=(50, 20), padx=30, anchor="n")  
    
        self.frame_2 = CTkFrame(master=self.frame_1, fg_color="#e5d8ad", height=100, width=250, border_color="#e5aaa7", border_width=0)
        self.frame_2.pack(expand=True, fill="x", pady=0, padx=20)
        
        self.frame_3 = CTkFrame(master=self.frame_1, fg_color="#ECCE5C", border_color="black", border_width=2)
        self.frame_3.pack(expand=True, fill="x", pady=0, padx=20, anchor="n")
    
        self.desc_label = self.text_designer.default_text("Now Let's Create Players And Characters", self.frame_2, 32)
        self.desc_label.pack(anchor="n", expand=True, pady=(10, 10), padx=10)   

        self.add_player_character_widgets()
        
        self.charNumb = int(self.combobox_chars.get())
    
    def add_player_character_widgets(self):
        self.character_entries = []
        for i in range(self.Players):
            self.desc_label = self.text_designer.default_text(f"Player {i+1} Name:", self.frame_3, 22)
            self.desc_label.pack(side=LEFT, anchor="n", pady=20, padx=30)    
        
            self.entry_name = CTkEntry(master=self.frame_3, placeholder_text="Start typing...", fg_color="#e5d8ad", font=("Baskerville Old Face", 22, "bold"), text_color="black", width=200)
            self.entry_name.pack(side=LEFT, anchor="n", pady=20, padx=30)
        
            self.desc_label_char = self.text_designer.default_text(f"How many characters for Player {i+1}:", self.frame_3, 22)
            self.desc_label_char.pack(side=LEFT, anchor="n", pady=20, padx=30)    
        
            self.combobox_chars = customtkinter.CTkComboBox(master=self.frame_3, values=["1", "2"], font=("Baskerville Old Face", 22, "bold"),
                                                            command=self.combobox_callback_charNumb, width=1, fg_color="#e5d8ad", text_color="black",
                                                            dropdown_font=("Baskerville Old Face", 22, "bold"))
            self.combobox_chars.set("1")
            self.combobox_chars.pack(expand=True, pady=10, padx=10)      
    
    def combobox_callback_charNumb(self, choice):
        if self.character_entries :
            pass
        else:
            self.frame_4 = CTkFrame(master=self.frame_1, fg_color="#ECCE5C", border_width=2)
            self.frame_4.pack(expand=True, fill="x", pady=0, padx=20, anchor="n")
            self.btn_submit = self.button_designer.default_button("Submit", self.frame_4, self.click_handler1)
            self.btn_submit.pack(side=RIGHT, anchor="e", pady=20, padx=30)
            

        for entry in self.character_entries:
            entry.destroy()
        self.character_entries = []

        self.charNumb = int(choice)
        for i in range(self.charNumb):
            character_entry = self.create_label_entry(self.frame_4, f"Character {i+1} Name:", 22, "Start typing...", 200)
            self.character_entries.append(character_entry)
        

    def create_label_entry(self, master, label_text, font_size, placeholder, entry_width):
        frame = CTkFrame(master=master, fg_color="#ECCE5C")
        frame.pack(anchor="n", pady=5, padx=30)
        
        label = self.text_designer.default_text(label_text, frame, font_size)
        label.pack(side=LEFT, anchor="n", pady=20, padx=30)    
        
        entry = CTkEntry(master=frame, placeholder_text=placeholder, fg_color="#e5d8ad", font=("Baskerville Old Face", font_size, "bold"), text_color="black", width=entry_width)
        entry.pack(side=LEFT, anchor="n", pady=20, padx=30)
        ''' Unfineshed:
        combobox_chars = customtkinter.CTkComboBox(master=self.frame_3, values=["1", "2"], font=("Baskerville Old Face", 22, "bold"),
                                                            command=self.combobox_callback_charNumb, width=1, fg_color="#e5d8ad", text_color="black",
                                                            dropdown_font=("Baskerville Old Face", 22, "bold"))
        combobox_chars.set("1")
        combobox_chars.pack(expand=True, pady=10, padx=10)  
        '''
        return frame

    def click_handler1(self):
        player_name = self.entry_name.get()
        self.player_tracker.add_player(player_name)
        for i, frame in enumerate(self.character_entries):
            entry = frame.winfo_children()[1]  
            character_name = entry.get()
            self.player_tracker.add_character(player_name, character_name)
        characters = self.player_tracker.get_characters(player_name)
        print(f"Name: {player_name}, Characters: {characters}")
        print("Going to main program")
        self.frame_1.pack_forget()
        self.create_page4()

    def create_page4(self):
        self.frame_2.pack_forget()
        self.frame_1.pack_forget()
        for widget in self.frame_1.winfo_children():
            widget.destroy()

        self.frame_1 = CTkFrame(master=self, fg_color="#e5d8ad", height=1200, width=750, border_color="#e5aaa7", border_width=2)
        self.frame_1.pack(expand=True, fill="both", pady=(50, 20), padx=30, anchor="n")  

        self.frame_2 = CTkFrame(master=self.frame_1, fg_color="#e5d8ad", border_color="#e5aaa7", border_width=0)
        self.frame_2.pack(expand=True, fill="y", padx=20)

        
        players_and_characters = self.player_tracker.get_players_and_characters()
        frames = []

        for i, (player, characters) in enumerate(players_and_characters.items()):
            frame = CTkFrame(master=self.frame_2, fg_color="#e5d8ad", border_color="black", border_width=2)
            frame.pack(expand=True, fill="x", pady=10, padx=20, anchor="n")
            frames.append(frame)

            players_label = self.text_designer.default_text("Player: ", frame, 22)
            players_label.pack(side=LEFT, padx=10, pady=10)
            player_label = self.text_designer.default_text(player, frame, 18)
            player_label.pack(side=LEFT, padx=10, pady=10)

            if len(characters) > 1:
                characters_label = self.text_designer.default_text("Characters: ", frame, 22)
                characters_label.pack(side=LEFT, padx=10, pady=10)
                for character in characters:
                    character_label = self.text_designer.default_text(character['name'], frame, 22)
                    character_label.pack(side=LEFT, padx=10, pady=2)
            elif len(characters) == 1:
                character_label = self.text_designer.default_text("Character: " + characters[0]['name'], frame, 18)
                character_label.pack(side=LEFT, padx=10, pady=10)

            remove_btn = self.button_designer.default_button("Remove", frame, lambda p=player: self.remove_player_and_characters(p))
            remove_btn.pack(side=RIGHT, padx=10, pady=10)

            new_character_btn = self.button_designer.default_button("New Character", frame, lambda p=player: self.create_new_character(p))
            new_character_btn.pack(side=RIGHT, padx=10, pady=10)
            
        self.save_game_btn = self.button_designer.default_button("Save Progress", self.frame_2, self.click_SaveGame)
        self.save_game_btn.pack(side=LEFT, anchor="w", expand=True, pady=10, padx=30)

        for i in range(4 - len(frames)):
            frame = CTkFrame(master=self.frame_2, fg_color="#e5d8ad", border_color="black", border_width=2)
            frame.pack(expand=True, fill="x", pady=10, padx=20, anchor="n")
            add_player_btn = self.button_designer.default_button("Add Player", frame, self.add_player_dialog)
            add_player_btn.pack(side=TOP, padx=10, pady=10)

    def remove_player_and_characters(self, player_name):
        self.player_tracker.remove_player(player_name)
        self.frame_1.pack_forget()
        self.create_page4()

    def create_new_character(self, player_name):
        if len(self.player_tracker.get_players_and_characters()[player_name]) >= 2:
            messagebox.showinfo("Maximum Characters Reached", f"{player_name} already has the maximum number of characters.")
            return

        dialog = customtkinter.CTkInputDialog(text="Enter character name for " + player_name + ":", title="New Character")
        character_name = dialog.get_input()
        if character_name:
            self.player_tracker.add_character(player_name, character_name)
            print("New character", character_name, "added for", player_name)
            self.frame_1.pack_forget()
            self.create_page4()
            
    def add_player_dialog(self):
        dialog = CTkInputDialog(text="Enter player name:", title="Add Player")
        player_name = dialog.get_input()
        if player_name:
            self.player_tracker.add_player(player_name)
            self.frame_1.pack_forget()
            self.create_page4()


    def click_SaveGame(self):
        print("Save progress has been pressed")
        self.save_game()
        
    def save_game(self):
        self.player_tracker.save_to_file("savefile.txt")
        messagebox.showinfo("Save Game", "Game progress saved successfully.")
        
    def create_page5(self):
        pass

app = App()
app.mainloop()
