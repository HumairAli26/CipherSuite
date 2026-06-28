import os
from tkinter import filedialog

def open_file():
    filepath = filedialog.askopenfilename(title="Select file to send")
    if not filepath:
        print("User cancelled")
        return
    with open(filepath, "r", encoding="utf-8") as f:
        filedata = f.read()
    return filedata
    


def save_file(filedata):
    save_path = filedialog.asksaveasfilename(
        title="Save File As",
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")]
    )
    if not save_path:
        return
    with open(save_path, 'w', encoding="utf-8") as f:
        f.write(filedata)