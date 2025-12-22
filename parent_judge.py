# Hit & Blow 判定
class ParentJudge:
    @staticmethod
    # 判定を行うメソッド
    def judge(answer: str, guess: str) -> tuple[int, int]:
        # Hit と Blow の数を計算
        hit = sum(a == g for a, g in zip(answer, guess))
        blow = sum(min(answer.count(d), guess.count(d)) for d in set(guess)) - hit
        return hit, blow