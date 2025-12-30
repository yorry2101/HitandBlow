# Hit & Blowの全体進行
import random
from parent_judge import ParentJudge
from game_round import GameRound
class GameManager:
    def __init__(self):
        self.round = GameRound()
        
        # 0~9と十二支のカードを準備
        self.cards_digits = [str(i) for i in range(10)]
        self.cards_zodiac = ["mouse", "cow", "tiger", "rabbit", "dragon", "snake",
                             "horse", "ram", "monkey", "rooster", "dog", "boar"]
        self.cards = self.cards_digits + self.cards_zodiac

    # 予想を処理するメソッド
    def make_guess(self, guess: list[str], correct_cards: list[str]):# -> tuple[int, int]:
        #hit, blow = ParentJudge.judge(self.round.answer, guess)
        hit, blow = ParentJudge.judge_cards(correct_cards, list(guess))
        self.round.add_attempt(guess, hit, blow)
        #return hit, blow
    
    # 最新のヒット数を取得する関数
    def get_last_hit(self) -> int:
        if self.round.attempts:
            return self.round.attempts[-1]['hit']
        return 0
    
    # 最新のブロー数を取得する関数
    def get_last_blow(self) -> int:
        if self.round.attempts:
            return self.round.attempts[-1]['blow']
        return 0
    
    # 手札となるカードをランダムにn枚決定するメソッド
    def deal_cards(self, n: int) -> list[str]:
        return random.sample(self.cards, n)
    
    # 正解カードを手札中からランダムに選択するメソッド
    def select_correct_cards(self, cards: list[str], n: int) -> list[str]:
        return random.sample(cards, n)
    