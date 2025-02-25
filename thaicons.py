# -*- coding: utf-8 -*-
"""Copy of thaicons.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1PglLfa6mNWohJoWUqHra_BicH88uYN1C
"""

import tkinter as tk
from random import shuffle

# List of Thai consonants and their names
thai_consonants = [
    ("ก", "Gor Gai"), ("\u0e02", "Khor Khai"), ("\u0e04", "Khor Khuat"),
    ("\u0e06", "Khor Rakhang"), ("\u0e07", "Ngor Ngu"), ("\u0e08", "Jor Jan"),
    ("\u0e0a", "Chor Ching"), ("\u0e0d", "Yor Ying"), ("\u0e10", "Dor Chada")
]
shuffle(thai_consonants)

class FlashcardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Thai Consonant Flashcards")

        self.current_index = 0
        self.flipped = False

        self.card_frame = tk.Frame(root, width=300, height=200, bg="white", relief="raised", bd=3)
        self.card_frame.pack(pady=20)

        self.label = tk.Label(self.card_frame, text=thai_consonants[self.current_index][0],
                              font=("Arial", 60), bg="white")
        self.label.pack(expand=True)

        self.card_frame.bind("<Button-1>", self.flip_card)
        self.label.bind("<Button-1>", self.flip_card)

        self.next_button = tk.Button(root, text="Next", command=self.next_card)
        self.next_button.pack(pady=10)

    def flip_card(self, event):
        if self.flipped:
            self.label.config(text=thai_consonants[self.current_index][0])
        else:
            self.label.config(text=thai_consonants[self.current_index][1])
        self.flipped = not self.flipped

    def next_card(self):
        self.current_index = (self.current_index + 1) % len(thai_consonants)
        self.label.config(text=thai_consonants[self.current_index][0])
        self.flipped = False

if __name__ == "__main__":
    root = tk.Tk()
    app = FlashcardApp(root)
    root.mainloop()