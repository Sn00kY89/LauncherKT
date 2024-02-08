#!/usr/bin/env python3

import tkinter as tk
import webbrowser
import json
import os

# URL del watermark
WATERMARK_URL = "https://github.com/Sn00kY89"

def open_url(url):
    webbrowser.open_new(url)

def open_watermark_url():
    open_url(WATERMARK_URL)

def open_chat_url():
    config_path = os.path.join(os.path.dirname(__file__), "bin", "config.json")
    with open(config_path) as f:
        config = json.load(f)
    chat_url = config.get("url")
    if chat_url:
        open_url(chat_url)

def main():
    root = tk.Tk()
    config_path = os.path.join(os.path.dirname(__file__), "bin", "config.json")
    with open(config_path) as f:
        config = json.load(f)
    
    # Impostazione delle dimensioni della finestra
    window_width = config.get("window_width", 350)
    window_height = config.get("window_height", 175)

    window_title = config.get("window_title")
    root.title(window_title)
    root.geometry(f"{window_width}x{window_height}")  # Imposta le dimensioni della finestra
    root.resizable(False, False)  # Rende la finestra non ridimensionabile

    watermark_text = "© 2024 Sn00kY89, GNU GPL License"

    # Leggi il testo del pulsante dal file di configurazione
    button_text = config.get("button_text", "Apri Chat GPT")

    button = tk.Button(root, text=button_text, command=open_chat_url)
    button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)  # Posiziona il pulsante al centro della finestra

    watermark = tk.Label(root, text=watermark_text, cursor="hand2", fg="blue", underline=True)
    watermark.pack(side=tk.BOTTOM, pady=5)  # Posizionato in basso con una spaziatura di 5 pixel
    watermark.bind("<Button-1>", lambda event: open_watermark_url())

    root.mainloop()

if __name__ == "__main__":
    main()
