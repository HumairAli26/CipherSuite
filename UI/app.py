import customtkinter as ctk
from theme import THEMES

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")


class CipherApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("CipherSuite")
        self.geometry("900x600")
        self.minsize(700, 500)
        self.current_theme = THEMES["light"]
        self.configure(fg_color=self.current_theme["bg"])
        self.create_widgets()

    def create_widgets(self):
        self.header_frame = ctk.CTkFrame(
            self,
            height=70,
            corner_radius=0,
            fg_color=self.current_theme["accent"]
        )
        self.header_frame.pack(fill="x")

        self.title_label = ctk.CTkLabel(
            self.header_frame,
            text="CipherSuite",
            font=("Courier New", 22, "bold", "italic"),
            text_color=self.current_theme["text"],
            fg_color="transparent"
        )
        self.title_label.pack(
            side="left",
            padx=20,
            pady=8
        )

        self.theme_button = ctk.CTkButton(
            self.header_frame,
            text="🌙 Dark",
            width=100,
            height=40,
            corner_radius=20,
            font=("Consolas", 12, "bold"),
            fg_color=self.current_theme["button_bg"],
            hover_color="#1E40AF",
            text_color=self.current_theme["text"]
        )
        self.theme_button.pack(
            side="right",
            padx=20,
            pady=8
        )

        self.main_frame = ctk.CTkFrame(
            self,
            fg_color = "transparent"
        )
        self.main_frame.pack(
            fill = "both",
            expand = "true",
            padx = 20,
            pady = 2
        )

        self.InputLable = ctk.CTkLabel(
            self.main_frame,
            text = "Message",
            font = ("Courier New", 18, "bold"),
            text_color = self.current_theme["text"]
        )
        self.InputLable.pack(
            anchor = "w",
            pady = (2, 2)
        )


if __name__ == "__main__":
    app = CipherApp()
    app.mainloop()