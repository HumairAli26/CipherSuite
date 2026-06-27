import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


import customtkinter as ctk
from tkinter import messagebox
from theme import THEMES
from algorithms.ceaserCipher import ceaser

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
            corner_radius=10,
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
            text = "Input Message",
            font = ("Courier New", 18, "bold"),
            text_color = self.current_theme["text"]
        )
        self.InputLable.pack(
            anchor = "w",
            pady = (4, 5)
        )

        self.input_textbox = ctk.CTkTextbox(
            self.main_frame,
            height = 100,
            corner_radius = 10,
            font = ("consolas", 14),
            border_width = 2,
            border_color = self.current_theme["border"]
        )
        self.input_textbox.pack(
            fill = "x",
            pady = (0, 20)
        )

        self.row_frame = ctk.CTkFrame(
            self.main_frame, 
            fg_color="transparent"
        )
        self.row_frame.pack(
            fill="x", 
            pady=(0, 20)
        )

        self.cipher_lable = ctk.CTkLabel(
            self.row_frame,
            text = "Cipher:",
            font = ("Courier New", 14, "bold"),
            text_color = self.current_theme["text"],
            anchor = "w",
            height = 30
        )
        self.cipher_lable.pack(
            side = "left",
            anchor = "w",
            padx = (0, 10)
        )

        self.cipher_menu = ctk.CTkOptionMenu(
            self.row_frame,
            values = [
                "Ceaser Cipher",
                "Vignere Cipher",
                "XOR Cipher"
            ],
            height = 30
        )
        self.cipher_menu.pack(
            side = "left",
            anchor = "w",
            padx = (0, 25)
        )

        self.shift_lable = ctk.CTkLabel(
            self.row_frame,
            text = "Shift:",
            text_color = self.current_theme["text"],
            font = ("Courier New", 12, "bold"),
            anchor = "w",
            height = 30
        )
        self.shift_lable.pack(
            side = "left",
            anchor = "w",
            padx = (0, 10)
        )

        self.shift_entry = ctk.CTkEntry(
            self.row_frame,
            placeholder_text = "e.g. 3",
            width = 120,
            height = 30
        )
        self.shift_entry.pack(
            side = "left",
            anchor = "w"
        )

        self.encrypt_button = ctk.CTkButton(
            self.row_frame,
            text = "Encrypt",
            font = ("Consolas", 12, "bold"),
            corner_radius = 10,
            height = 30,
            fg_color=self.current_theme["button_bg"],
            hover_color="#1E40AF",
            text_color = self.current_theme["text"],
            command = self.encrypt_text
        )
        self.encrypt_button.pack(
            side = "right",
            anchor = "e"
        )


        self.OutputLable = ctk.CTkLabel(
            self.main_frame,
            text = "Output Message",
            font = ("Courier New", 18, "bold"),
            text_color = self.current_theme["text"]
        )
        self.OutputLable.pack(
            anchor = "w",
            pady = (4, 5)
        )

        self.output_textbox = ctk.CTkTextbox(
            self.main_frame,
            height = 100,
            corner_radius = 10,
            font = ("consolas", 14),
            border_width = 2,
            border_color = self.current_theme["border"]
        )

        self.output_textbox.pack(
            fill = "x",
            pady = (0, 20)
        )

    
    def encrypt_text(self):
        try:
            text = self.input_textbox.get("1.0", "end-1c")
            shift = int(self.shift_entry.get())
            encrypted = ceaser(text, shift)
            self.output_textbox.delete("1.0", "end-1c")
            self.output_textbox.insert("1.0", encrypted)
        except:
            messagebox.showerror(
                "Invalid Shift",
                "Please enter a valid integer for shift value"
            )

    def decrypt_text(self):
        try:
            text = self.input_textbox.get("1.0", "end-1c")
            shift = int(self.shift_entry.get())
            decrypted = ceaser(text, shift)
            self.output_textbox.delete("1.0", "end-1c")
            self.output_textbox.insert("1.0", decrypted)
        except:
            messagebox.showerror(
                "Invalid Shift",
                "Please enter a valid integer for shift value"
            )


if __name__ == "__main__":
    app = CipherApp()
    app.mainloop()