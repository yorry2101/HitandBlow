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

        self.start_screen = StartScreen(
            root,
            self.show_difficulty_selection
        )

    def get_computer_screen_size(self):
        width = self.root.winfo_screenwidth()
        height = self.root.winfo_screenheight()
        print(f"Screen size: {width}x{height}") # Debug print, 後で消す
        return f"{width}x{height}"

    def show_difficulty_selection(self):
        self.start_screen.destroy()
        self.difficulty_screen = DifficultyScreen(
            self.root,
            self.start_game,
            self.back_to_start_from_difficulty
        )

    def start_game(self, number_of_cards, number_of_correct):
        self.difficulty_screen.destroy()
        self.game_screen = HitAndBlowGUI(
            self.root,
            self.back_to_start_from_game,
            number_of_cards,
            number_of_correct
        )
    
    # ゲーム画面からスタート画面に戻る
    def back_to_start_from_game(self):
        self.game_screen.destroy()
        self.start_screen = StartScreen(
            self.root,
            self.show_difficulty_selection
        )
    
    # diff選択からスタート画面に戻る
    def back_to_start_from_difficulty(self):
        self.difficulty_screen.destroy()
        self.start_screen = StartScreen(
            self.root,
            self.show_difficulty_selection
        )

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
    def __init__(self, master, start_callback, back_callback):
        super().__init__(master, bg="#A0522D")
        self.pack(fill="both", expand=True)
        print("Difficulty screen shown")  # デバッグ用出力

        self.start_callback = start_callback
        self.back_callback = back_callback

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
        
        self.button_return = tk.Button(
            self,
            text="Return",
            font=("Arial", 24, "bold"),
            bg="gray",
            fg="white",
            command=self.return_to_start_screen
        )

        self.button_return.place(
            relx=0.98,   # 右端
            rely=0.95,   # 下端
            anchor="se"  # ボタンの右下を基準に配置
        )

    def select_difficulty(self, number_of_cards, number_of_correct):
        print(f"Selected difficulty: {number_of_cards} cards, {number_of_correct} correct")  # デバッグ用出力
        self.start_callback(number_of_cards, number_of_correct)
    
    def return_to_start_screen(self):
        self.back_callback()
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

        self.game_manager = GameManager()

        # キャンバスの幅を計算
        half = self.number_of_cards // 2
        max_x_hand = 280 + (half - 1) * 150 + 200 if half > 0 else 480
        max_x_select = 280 + (self.number_of_correct - 1) * 150 + 200 if self.number_of_correct > 0 else 480
        self.canvas_width = max(1000, max_x_hand, max_x_select)
        self.canvas_height = 800

        # キャンバス
        self.cvs = tk.Canvas(
            self,
            width=self.canvas_width,
            height=self.canvas_height,
            bg="#007400"
        )
        self.cvs.pack()

        self.y_content_top = 50
        self.y_hit_blow_label = self.y_content_top
        self.select_area_start_x = (self.canvas_width - (self.number_of_correct * 150)) // 2 + 75
        self.y_frame = self.y_content_top + 150
        self.cards_per_row = self.number_of_cards // 2
        self.start_x = (self.canvas_width - (self.cards_per_row * 150)) // 2 + 75
        self.start_y = self.y_frame + 250

        # 手札となるカードをランダムにn枚決定
        card_numbers = self.game_manager.deal_cards(self.number_of_cards)
        print("Card numbers:", card_numbers)  # Debug print
        
        # 選択されたカードのリスト (固定サイズ)
        self.select_cards = [None] * self.number_of_correct

        # 選択中のカードが置かれるスペース
        # number_of_correct枚分のカードフレームを表示
        # 中心に合わせる
        self.card_frames = []
        for i in range(self.number_of_correct):
            x_frame = self.select_area_start_x + i * 150
            frame = CardFrameSprite(self.cvs, x_frame, self.y_frame)
            self.card_frames.append(frame)

        # カード 8or12or16枚表示, 2段表示
        # 中心に合わせる
        self.cards = []
        for i, card_number in enumerate(card_numbers):
            row = i // self.cards_per_row
            col = i % self.cards_per_row
            x_card = self.start_x + col * 150
            y_card = self.start_y + row * 200
            card_sprite = CardSprite(self.cvs, x_card, y_card, card_number)
            self.cards.append(card_sprite)
        
        # 正解カードを手札中からランダムに選択
        self.correct_cards = random.sample(self.cards, self.number_of_correct)
        print("Correct cards:", [card.get_charatext() for card in self.correct_cards])  # Debug print
        
        # クリックイベントのバインド
        self.cvs.bind("<Button-1>", self.on_mouse_clicked)

        # HitとBlowをCanvas内に表示
        # 選択カードエリアの上に中央揃えで表示
        x_offset = 100
        x_hit = self.canvas_width // 2 - x_offset
        x_blow = self.canvas_width // 2 + x_offset
        self.hit_text_id = self.cvs.create_text(
            x_hit,
            self.y_hit_blow_label,
            text="Hit: 0",
            font=("Arial", 20),
            fill="white",
            anchor="center"
        )
        self.blow_text_id = self.cvs.create_text(
            x_blow,
            self.y_hit_blow_label,
            text="Blow: 0",
            font=("Arial", 20),
            fill="white",
            anchor="center"
        )

        # 説明
        self.label_info = tk.Label(self,
            text="Select cards and press JUDGE!",
            font=("Arial", 28),
            fg="beige",
            bg="#A0522D"
        )
        self.label_info.pack(pady=5)

        # 判定ボタン
        self.button_guess = tk.Button(self,
            text="JUDGE!",
            font=("Arial", 30, "bold"),
            bg="#FF6347",
            fg="white",
            activebackground="#FF4500",
            relief="raised",
            bd=4,
            command=self.make_guess
        )
        self.button_guess.pack(pady=10)

        self.button_quit = tk.Button(
            self,
            text="Quit",
            font=("Arial", 24, "bold"),
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
                            card.selected(i, self.select_area_start_x, self.y_frame)
                            break

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

        self.cvs.itemconfig(self.hit_text_id, text=f"Hit: {hit}")
        self.cvs.itemconfig(self.blow_text_id, text=f"Blow: {blow}")

        if hit == self.number_of_correct:
            if messagebox.askyesno("Clear", "Congratulations! Do you want to play again?"):
                self.back_callback()
            else:
                self.master.quit()

    def quit_game(self):
        if messagebox.askyesno("Confirmation", "Are you back to Start Screen?"):
            self.back_callback()


if __name__ == "__main__":
    root = tk.Tk()
    App(root)
    root.mainloop()