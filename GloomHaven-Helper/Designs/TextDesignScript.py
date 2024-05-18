from customtkinter import*

class text_design():
    def default_text(self, Text, frame, size):
        self.Text = Text
        self.frame = frame
        self.size = size
        font=("Baskerville Old Face", self.size, "bold")
        
        return CTkLabel(
            master=self.frame,
            font=font,
            text=Text,
            text_color="black"
            )