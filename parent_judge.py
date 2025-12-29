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
    
    # カード版judgeメソッド
    @staticmethod
    def judge_cards(answer_cards: list[str], guess_cards: list[str]) -> tuple[int, int]:
        """
        Hit & Blow の判定を行う（カード版）
        answer_cards: 正解カードのリスト（例: ["1", "2", "3", "4"]）
        guess_cards:  入力カードのリスト（例: ["1", "3", "2", "5"]）
        return: (hit, blow)
        """

        if len(answer_cards) != len(guess_cards):
            raise ValueError("answer_cards と guess_cards の長さが一致していません。")

        # Hit（位置も値も一致）
        hit = sum(a == g for a, g in zip(answer_cards, guess_cards))

        # Blow（値は一致するが位置が違う）
        from collections import Counter
        a_cnt = Counter(answer_cards)
        g_cnt = Counter(guess_cards)

        common = sum(min(a_cnt[d], g_cnt[d]) for d in g_cnt)
        blow = common - hit

        return hit, blow