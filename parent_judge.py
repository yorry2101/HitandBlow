class ParentJudge:
    @staticmethod
    def judge(answer: str, guess: str) -> tuple[int, int]:
        """
        Hit & Blow の判定を行う
        answer: 正解（例: "1234"）
        guess:  入力（例: "1325"）
        return: (hit, blow)
        """

        # 桁数チェック（必要なら）
        if len(answer) != len(guess):
            raise ValueError("answer と guess の長さが一致していません。")

        # Hit（位置も値も一致）
        hit = sum(a == g for a, g in zip(answer, guess))

        # Blow（値は一致するが位置が違う）
        # 共通文字数を求めてから Hit を引く
        from collections import Counter
        a_cnt = Counter(answer)
        g_cnt = Counter(guess)

        common = sum(min(a_cnt[d], g_cnt[d]) for d in g_cnt)
        blow = common - hit

        return hit, blow