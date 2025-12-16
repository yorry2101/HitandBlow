import tkinter as tk
from tkinter import messagebox
from dice_poker_logic import DicePokerGame 

class DicePokerGUI:
    def __init__(self, master):
        self.master = master
        master.title("サイコロポーカーDX")

        self.game = DicePokerGame(bankroll=100)

        bg_color = "#224466"
        fg_color = "#ffffff"
        master.configure(bg=bg_color)

        self.title_label = tk.Label(
            master,
            text="★ サイコロポーカー DX ★",
            font=("Meiryo", 20, "bold"),
            bg=bg_color,
            fg="#ffcc33"
        )
        self.title_label.pack(pady=10)

        self.dice_frame = tk.Frame(master, bg=bg_color)
        self.dice_frame.pack(pady=10)

        self.dice_labels = []
        for _ in range(5):
            lbl = tk.Label(
                self.dice_frame,
                text="-",
                font=("Meiryo", 24, "bold"),
                width=3,
                bg="#446688",
                fg=fg_color,
                relief="ridge",
                bd=3
            )
            lbl.pack(side="left", padx=5)
            self.dice_labels.append(lbl)

        self.bank_label = tk.Label(
            master,
            text=f"所持金: $ {self.game.bankroll}",
            font=("Meiryo", 16),
            bg=bg_color,
            fg=fg_color
        )
        self.bank_label.pack(pady=5)

        self.result_label = tk.Label(
            master,
            text="結果: まだプレイしていません",
            font=("Meiryo", 14),
            bg=bg_color,
            fg=fg_color
        )
        self.result_label.pack(pady=5)

        self.button_frame = tk.Frame(master, bg=bg_color)
        self.button_frame.pack(pady=10)

        self.play_button = tk.Button(
            self.button_frame,
            text="プレイ！",
            font=("Meiryo", 14, "bold"),
            command=self.play_round,
            width=10
        )
        self.play_button.pack(side="left", padx=10)

        self.quit_button = tk.Button(
            self.button_frame,
            text="終了",
            font=("Meiryo", 14),
            command=master.quit,
            width=8
        )
        self.quit_button.pack(side="left", padx=10)

    def play_round(self):
        """ボタンが押されたときに1回分プレイする"""
        dice, hand_name, payoff, bankroll = self.game.play_round()

        for lbl, value in zip(self.dice_labels, dice):
            lbl.config(text=str(value))

        sign = "+" if payoff >= 0 else ""
        self.result_label.config(
            text=f"結果: {hand_name} ({sign}{payoff})"
        )
        self.bank_label.config(
            text=f"所持金: $ {bankroll}"
        )

        if bankroll >= 150:
            messagebox.showinfo("クリア！", "おめでとうございます！所持金が $150 以上になりました。")
            self.play_button.config(state="disabled")
        elif bankroll <= 0:
            messagebox.showinfo("ゲームオーバー", "所持金が 0 以下になりました。")
            self.play_button.config(state="disabled")


def main():
    root = tk.Tk()
    app = DicePokerGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
