# Hit & Blowの全体進行
from parent_judge import ParentJudge
from game_round import GameRound
class GameManager:
    def __init__(self, answer: str):
        self.round = GameRound(answer)
    
    # 予想を処理するメソッド
    def make_guess(self, guess: str):# -> tuple[int, int]:
        hit, blow = ParentJudge.judge(self.round.answer, guess)
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
    
    