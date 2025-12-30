# 1回分の勝負管理
class GameRound:
    def __init__(self):
        self.attempts = []

    def add_attempt(self, guess: str, hit: int, blow: int):
        self.attempts.append({'guess': guess, 'hit': hit, 'blow': blow})

    def is_correct(self, hit: int, length: int = 4) -> bool:
        return hit == length

    def show_history(self):
        if not self.attempts:
            return
        print(" ---history--- ")
        for i, a in enumerate(self.attempts, 1):
            print(f"  {i}: {a['guess']} -> {a['hit']} Hit {a['blow']} Blow")