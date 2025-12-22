# 1回分の勝負管理
class GameRound:
    def __init__(self, answer: str):
        self.answer = answer
        self.attempts = []

    def add_attempt(self, guess: str, hit: int, blow: int):
        self.attempts.append({'guess': guess, 'hit': hit, 'blow': blow})