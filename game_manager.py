# Hit & Blowの全体進行
from parent_judge import ParentJudge
from game_round import GameRound
class GameManager:
    def __init__(self, answer: str):
        self.round = GameRound(answer)
    
    # 予想を処理するメソッド
    def make_guess(self, guess: str) -> tuple[int, int]:
        hit, blow = ParentJudge.judge(self.round.answer, guess)
        self.round.add_attempt(guess, hit, blow)
        return hit, blow
    
    # 親に正解の値(4桁)を与えるメソッド
    # randomな値を生成する．
    @staticmethod
    def generate_answer() -> str:
        import random
        digits = list(range(10))
        random.shuffle(digits)
        return ''.join(str(digits[i]) for i in range(4))  # 4桁の数字を返す
    
