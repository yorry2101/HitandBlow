# text interface for Hit & Blow game
import sys
from game_manager import GameManager
class TextInterface:
    def __init__(self, answer: str):
        self.game_manager = GameManager(answer)

    def start(self):
        print("=== Hit & Blow ゲームへようこそ！ ===")
        print("4桁の数字を当ててください。各桁の数字は0-9で、重複はありません。")
        print("終了するには 'exit' と入力してください。")

        while True:
            guess = input("あなたの予想を入力してください: ")
            if guess.lower() == 'exit':
                print("ゲームを終了します。ありがとうございました！")
                sys.exit()

            if not self.validate_guess(guess):
                print("無効な入力です。4桁の異なる数字を入力してください。")
                continue

            hit, blow = self.game_manager.make_guess(guess)
            print(f"結果: {hit} Hit, {blow} Blow")

            if hit == 4:
                print("おめでとうございます！正解です！")
                break

    def validate_guess(self, guess: str) -> bool:
        return (
            len(guess) == 4 and
            guess.isdigit() and
            len(set(guess)) == 4
        )
