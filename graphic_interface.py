# graphic interface for Hit & Blow game
# 内容はまだない
import tkinter as tk
from game_manager import GameManager
class GraphicInterface:
    def __init__(self, answer: str):
        self.answer = answer
        self.game = GameManager(answer)

        bg_color = "#224466"
        fg_color = "#ffffff"

        self.title_label = tk.Label(
            text="★ Hit & Blow Game ★",
            font=("Meiryo", 20, "bold"),
            bg=bg_color,
            fg=fg_color
        )

        self.title_label.pack(pady=10)
        self.start_button = tk.Button(
            text="Start Game",
            font=("Meiryo", 16),
            bg="#446688",
            fg=fg_color,
            command=self.start
        )

        self.start_button.pack(pady=20)

        self.answer_label = tk.Label(
            text="Answer: " + self.answer,
            font=("Meiryo", 16),
            bg=bg_color,
            fg=fg_color
        )

        self.answer_label.pack(pady=10)

        self.root = tk.Tk()
        self.root.configure(bg=bg_color)
        self.root.title("Hit & Blow Game")

    def start(self):
        label = tk.Label(self.root, text="Graphic Interface is under construction.")
        label.pack(padx=20, pady=20)
        self.root.mainloop()