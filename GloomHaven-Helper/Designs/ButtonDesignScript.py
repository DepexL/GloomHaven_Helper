from customtkinter import*

class btn_design():
    def default_button(self, Text, frame, command, width=None):
        self.Text = Text
        self.frame = frame
        self.command = command
        buttonFont = ("Baskerville Old Face", 18, "bold")
        buttonColor = "#9c4541"

        if width is not None:
            return CTkButton(
                master=self.frame,
                command=self.command,
                font=buttonFont,
                text=Text,
                height=50,
                width=width,
                fg_color=buttonColor,
                hover_color="#79312d"
            )
        else:
            return CTkButton(
                master=self.frame,
                command=self.command,
                font=buttonFont,
                text=Text,
                height=50,
                fg_color=buttonColor,
                hover_color="#79312d"
            )