import tkinter as tk
from tkinter import messagebox
import random
from game_manager import GameManager


class HitAndBlowGUI:
    def __init__(self, master):
        master.title("Hit & Blow")
        master.geometry("360x420")
        master.configure(bg="#222222")


        # 正解をランダム生成（重複なし・4桁）
        self.answer = self.generate_answer()
        self.game_manager = GameManager(self.answer)

        # タイトル
        self.label_title = tk.Label(
            text="Hit & Blow",
            font=("Arial", 22, "bold"),
            fg="#FFD700",
            bg="#222222"
        )
        self.label_title.pack(pady=10)

        # 説明
        self.label_info = tk.Label(
            text="4桁の数字を入力してください",
            font=("Arial", 11),
            fg="white",
            bg="#222222"
        )
        self.label_info.pack(pady=5)

        # 入力欄
        self.entry_guess = tk.Entry(
            width=12,
            font=("Arial", 16),
            justify="center"
        )
        self.entry_guess.pack(pady=8)

        # 判定ボタン
        self.button_guess = tk.Button(
            text="判定！",
            font=("Arial", 14, "bold"),
            bg="#FF6347",
            fg="white",
            activebackground="#FF4500",
            relief="raised",
            bd=4,
            command=self.make_guess
        )
        self.button_guess.pack(pady=10)
        
        # 結果表示
        self.label_result = tk.Label(master, text="", font=("Arial", 12))
        self.label_result.pack(pady=5)

        # 履歴表示
        self.text_history = tk.Text(master, height=10, width=30, state="disabled")
        self.text_history.pack(pady=10)

    def generate_answer(self) -> str:
        digits = []
        while len(digits) < 4:
            d = random.randint(0, 9)
            if d not in digits:
                digits.append(d)
        return "".join(str(d) for d in digits)

    def validate_guess(self, guess: str) -> bool:
        return (
            len(guess) == 4 and
            guess.isdigit() and
            len(set(guess)) == 4
        )

    def make_guess(self):
        guess = self.entry_guess.get()

        if not self.validate_guess(guess):
            messagebox.showerror(
                "入力エラー", "4桁の異なる数字を入力してください"
            )
            return

        hit, blow = self.game_manager.make_guess(guess)

        result_text = f"{guess} → {hit} Hit, {blow} Blow"
        self.label_result.config(text=result_text)

        # 履歴に追加
        self.text_history.config(state="normal")
        self.text_history.insert(tk.END, result_text + "\n")
        self.text_history.config(state="disabled")

        # 入力欄クリア
        self.entry_guess.delete(0, tk.END)

        if hit == 4:
            messagebox.showinfo("クリア", "おめでとうございます！正解です！")
            self.master.quit()


if __name__ == "__main__":
    root = tk.Tk()
    app = HitAndBlowGUI(root)
    root.mainloop()