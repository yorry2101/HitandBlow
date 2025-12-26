import tkinter as tk
from tkinter import messagebox
import random
from game_manager import GameManager

class App:
    def __init__(self, root):
        self.root = root
        self.root.geometry(self.get_computer_screen_size())

        self.start_screen = StartScreen(root, self.start_game)

    def get_computer_screen_size(self):
        width = self.root.winfo_screenwidth()
        height = self.root.winfo_screenheight()
        print(f"Screen size: {width}x{height}") # Debug print, 後で消す
        return f"{width}x{height}"

    def start_game(self):
        self.start_screen.destroy()
        self.game_screen = HitAndBlowGUI(self.root, self.back_to_start)

    def back_to_start(self):
        self.game_screen.destroy()
        self.start_screen = StartScreen(self.root, self.start_game)

class StartScreen(tk.Frame):
    def __init__(self, master, start_callback):
        super().__init__(master, bg="#A0522D")
        self.pack(fill="both", expand=True)

        tk.Label(
            self,
            text="Hit & Blow",
            font=("Arial", 60, "bold"),
            fg="gold",
            bg="#A0522D"
        ).pack(pady=150)

        tk.Button(
            self,
            text="START",
            font=("Arial", 30, "bold"),
            bg="#FFD700",
            fg="black",
            height=1,
            width=10,
            command=start_callback
        ).pack()

        # quit button
        tk.Button(
            self,
            text="QUIT",
            font=("Arial", 30, "bold"),
            bg="gray",
            fg="white",
            height=1,
            width=10,
            command=master.quit
        ).pack(pady=20)

class HitAndBlowGUI(tk.Frame):
    def __init__(self, master, back_callback):
        super().__init__(master, bg="#A0522D")
        self.pack(fill="both", expand=True)

        self.back_callback = back_callback
        self.master = master
        self.master.title("Hit & Blow")
        self.master.geometry(self.master.winfo_geometry())
        self.master.configure(bg="#A0522D")

        # 正解をランダム生成（重複なし・4桁）
        self.answer = self.generate_answer()
        self.game_manager = GameManager(self.answer)

        # タイトル
        self.label_title = tk.Label(self,
            text="Hit & Blow !!",
            font=("Arial", 108, "bold"),
            fg="red",
            bg="beige"
        )
        self.label_title.pack(pady=50)
        

        # 説明
        self.label_info = tk.Label(self,
            text="Please enter your thinking 4 Number",
            font=("Arial", 30),
            fg="beige",
            bg="#A0522D"
        )
        self.label_info.pack(pady=5)

        # 入力欄
        self.entry_guess = tk.Entry(self,
            width=30,
            font=("Arial", 16),
            justify="center"
        )
        self.entry_guess.pack(pady=8)

        # 判定ボタン
        self.button_guess = tk.Button(self,
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
        self.label_result = tk.Label(self, font=("Arial", 12))
        self.label_result.pack(pady=5)

        # 履歴表示
        self.text_history = tk.Text(self, height=10, width=30, state="disabled")
        self.text_history.pack(pady=10)

        self.button_quit = tk.Button(
            self,
            text="Quit",
            font=("Arial", 16, "bold"),
            bg="gray",
            fg="white",
            command=self.quit_game
        )

        self.button_quit.place(
            relx=0.98,   # 右端
            rely=0.95,   # 下端
            anchor="se"  # ボタンの右下を基準に配置
        )

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

    def quit_game(self):
        if messagebox.askyesno("Confirmation", "Are you back to Start Screen?"):
            self.back_callback()


if __name__ == "__main__":
    root = tk.Tk()
    App(root)
    root.mainloop()