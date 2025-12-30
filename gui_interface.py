import tkinter as tk
from tkinter import messagebox
import random
from game_manager import GameManager
from sprite import CardSprite, CardFrameSprite

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Hit & Blow Game")
        self.root.geometry(self.get_computer_screen_size())

        self.start_screen = StartScreen(root, self.show_difficulty_selection)

    def get_computer_screen_size(self):
        width = self.root.winfo_screenwidth()
        height = self.root.winfo_screenheight()
        print(f"Screen size: {width}x{height}") # Debug print, 後で消す
        return f"{width}x{height}"

    def show_difficulty_selection(self):
        self.start_screen.destroy()
        self.difficulty_screen = DifficultyScreen(self.root, self.start_game)

    def start_game(self, number_of_cards, number_of_correct):
        self.difficulty_screen.destroy()
        self.game_screen = HitAndBlowGUI(self.root, self.back_to_start, number_of_cards, number_of_correct)

    def back_to_start(self):
        self.game_screen.destroy()
        self.start_screen = StartScreen(self.root, self.show_difficulty_selection)

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

class DifficultyScreen(tk.Frame):
    def __init__(self, master, start_callback):
        super().__init__(master, bg="#A0522D")
        self.pack(fill="both", expand=True)
        print("Difficulty screen shown")  # デバッグ用出力

        self.start_callback = start_callback

        tk.Label(
            self,
            text="Select Difficulty",
            font=("Arial", 40, "bold"),
            fg="gold",
            bg="#A0522D"
        ).pack(pady=100)

        # 難易度ボタン
        difficulties = [
            ("EASY", 8, 4),
            ("NORMAL", 12, 5),
            ("HARD", 16, 6)
        ]

        for name, cards, correct in difficulties:
            tk.Button(
                self,
                text=f"{name}\n({cards} cards, {correct} correct)",
                font=("Arial", 20, "bold"),
                bg="#FFD700",
                fg="black",
                height=2,
                width=20,
                command=lambda c=cards, cor=correct: self.select_difficulty(c, cor)
            ).pack(pady=20)

    def select_difficulty(self, number_of_cards, number_of_correct):
        print(f"Selected difficulty: {number_of_cards} cards, {number_of_correct} correct")  # デバッグ用出力
        self.start_callback(number_of_cards, number_of_correct)

class HitAndBlowGUI(tk.Frame):
    def __init__(self, master, back_callback, number_of_cards, number_of_correct):
        super().__init__(master, bg="#A0522D")
        self.pack(fill="both", expand=True)

        self.back_callback = back_callback
        self.master = master
        self.master.title("Hit & Blow")
        self.master.geometry(self.master.winfo_geometry())
        self.master.configure(bg="#A0522D")

        self.number_of_cards = number_of_cards # 手札の枚数
        self.number_of_correct = number_of_correct # 正解の枚数

        # 正解をランダム生成（重複なし・number_of_correct桁）
        self.answer = self.generate_answer()
        self.game_manager = GameManager(self.answer)

        # キャンバスの幅を計算
        half = self.number_of_cards // 2
        max_x_hand = 280 + (half - 1) * 150 + 200 if half > 0 else 480
        max_x_select = 280 + (self.number_of_correct - 1) * 150 + 200 if self.number_of_correct > 0 else 480
        self.canvas_width = max(1000, max_x_hand, max_x_select)
        self.canvas_height = 800

        # キャンバス
        self.cvs = tk.Canvas(self, width=self.canvas_width, height=self.canvas_height, bg="#007400")
        self.cvs.pack()

        self.select_area_start_x = (self.canvas_width - (self.number_of_correct * 150)) // 2 + 75
        self.cards_per_row = self.number_of_cards // 2
        self.start_x = (self.canvas_width - (self.cards_per_row * 150)) // 2 + 75

        # 中心線
        self.cvs.create_line(self.canvas_width//2, 0, self.canvas_width//2, self.canvas_height, fill="white", dash=(4, 2))

        # 手札となるカードをランダムにn枚決定
        card_numbers = self.game_manager.deal_cards(self.number_of_cards)
        print("Card numbers:", card_numbers)  # Debug print
        
        # 選択されたカードのリスト (固定サイズ)
        self.select_cards = [None] * self.number_of_correct

        # 選択中のカードが置かれるスペース
        # number_of_correct枚分のカードフレームを表示
        # 中心に合わせる
        self.card_frames = []
        y_frame = 150
        for i in range(self.number_of_correct):
            x_frame = self.select_area_start_x + i * 150
            frame = CardFrameSprite(self.cvs, x_frame, y_frame)
            self.card_frames.append(frame)

        # カード 8or12or16枚表示, 2段表示
        # 中心に合わせる
        self.cards = []
        for i, card_number in enumerate(card_numbers):
            row = i // self.cards_per_row
            col = i % self.cards_per_row
            x_card = self.start_x + col * 150
            y_card = 400 + row * 200
            card_sprite = CardSprite(self.cvs, x_card, y_card, card_number)
            self.cards.append(card_sprite)
        
        # 正解カードを手札中からランダムに選択
        self.correct_cards = random.sample(self.cards, self.number_of_correct)
        print("Correct cards:", [card.get_charatext() for card in self.correct_cards])  # Debug print
        
        # クリックイベントのバインド
        self.cvs.bind("<Button-1>", self.on_mouse_clicked)
            
        # タイトル
        """
        self.label_title = tk.Label(self,
            text="Hit & Blow !!",
            font=("Arial", 108, "bold"),
            fg="red",
            bg="beige"
        )
        self.label_title.pack(pady=50)
        """

        ## hit と blow を分けて表示
        self.label_hit = tk.Label(self,
            font=("Arial", 20),
            fg="blue",
            bg="beige"
        )
        self.label_hit.pack(pady=50)

        self.label_blow = tk.Label(self,
            font=("Arial", 20),
            fg="green",
            bg="beige"
        )
        self.label_blow.pack(pady=50)

        # 説明
        self.label_info = tk.Label(self,
            text="Please enter your thinking 4 Number",
            font=("Arial", 30),
            fg="beige",
            bg="#A0522D"
        )
        self.label_info.pack(pady=5)

        # 判定ボタン
        self.button_guess = tk.Button(self,
            text="JUDGE!",
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
        #self.label_result = tk.Label(self, font=("Arial", 12))
        #self.label_result.pack(pady=5)

        # 履歴表示
        #self.text_history = tk.Text(self, height=10, width=30, state="disabled")
        #self.text_history.pack(pady=10)

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
    
    def on_mouse_clicked(self, event):
        x_click = event.x
        y_click = event.y
        print(f"Mouse clicked at: ({x_click}, {y_click})")  # デバッグ用出力

        for card in self.cards:
            card_x, card_y = card.get_position()
            print(f"Card position: ({card_x}, {card_y})")  # デバッグ用出力
            if (card_x - 45 <= x_click <= card_x + 45 and
                card_y - 70 <= y_click <= card_y + 70):
                # カードがクリックされた場合の処理
                print(f"Card {card.get_charatext()} clicked") # デバッグ用出力
                if card.is_selected():
                    # 非選択: スロットをNoneにする
                    for i in range(self.number_of_correct):
                        if self.select_cards[i] == card:
                            self.select_cards[i] = None
                            card.deselected()
                            break
                else:
                    # 選択: 空いているスロットを探す
                    for i in range(self.number_of_correct):
                        if self.select_cards[i] is None:
                            self.select_cards[i] = card
                            card.selected(i, self.select_area_start_x)
                            break

    def generate_answer(self) -> str:
        digits = []
        while len(digits) < self.number_of_correct:
            d = random.randint(0, 9)
            if d not in digits:
                digits.append(d)
        return "".join(str(d) for d in digits)

    def validate_guess(self, guess: str) -> bool:
        return (
            len(guess) == self.number_of_correct and
            guess.isdigit() and
            len(set(guess)) == self.number_of_correct
        )

    def make_guess(self):
        print("Making guess...")  # デバッグ用出力
        selected_count = sum(1 for c in self.select_cards if c is not None)
        print(f"Selected cards count: {selected_count}")  # デバッグ用出力
        if selected_count != self.number_of_correct:
            messagebox.showerror("選択エラー", f"{self.number_of_correct}枚のカードを選択してください")
            return

        self.game_manager.make_guess(self.select_cards, self.correct_cards)
        hit = self.game_manager.get_last_hit()
        blow = self.game_manager.get_last_blow()

        self.label_hit.config(text=f"Hit: {hit}")
        self.label_blow.config(text=f"Blow: {blow}")

        if hit == self.number_of_correct:
            messagebox.showinfo("クリア", "おめでとうございます！正解です！")
            self.master.quit()

    def quit_game(self):
        if messagebox.askyesno("Confirmation", "Are you back to Start Screen?"):
            self.back_callback()


if __name__ == "__main__":
    root = tk.Tk()
    App(root)
    root.mainloop()