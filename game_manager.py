# Hit & Blowの全体進行
from parent_judge import ParentJudge
from game_round import GameRound
class GameManager:
    def __init__(self, answer: str):
        self.round = GameRound(answer)

    def make_guess(self, guess: str) -> tuple[int, int]:
        hit, blow = ParentJudge.judge(self.round.answer, guess)
        self.round.add_attempt(guess, hit, blow)
        return hit, blow