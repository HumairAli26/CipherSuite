import tkinter as tk
from theme import THEMES

class CipherApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("CipherSuite")
        self.geometry("900x600")
        self.minsize(700, 500)
        self.current_theme = THEMES["light"]
        self.configure(bg=self.current_theme["bg"])
        self.create_widget()

    def create_widget(self):
        self.header_frame = tk.Frame(
            self, 
            height=70,
            bg = self.current_theme["accent"]
            )
        self.header_frame.pack(fill="x")
        self.title_lable = tk.Label(self.header_frame)
        self.title_lable.config(
            text = "CipherSuite"
        )
        self.title_lable.pack(
            side = "left",
            padx = 20,
            size = 15
            )



if __name__ == "__main__":
    app = CipherApp()
    app.mainloop()