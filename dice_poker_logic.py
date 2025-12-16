import random
from collections import Counter

class DicePokerGame:
    def __init__(self, bankroll=100):
        self.bankroll = bankroll 

    def roll_dice(self):
        """サイコロ5個を振る"""
        return [random.randint(1, 6) for _ in range(5)]

    def evaluate_hand(self, dice):
        """
        出目から役と配当を決める。
        戻り値: (役の名前, 配当)
        """
        counts = Counter(dice)
        values = sorted(counts.values(), reverse=True)
        sorted_dice = sorted(dice)

        is_straight = sorted_dice in [list(range(1, 6)), list(range(2, 7))]

        if 5 in values:
            return "Five of a kind", 50
        elif 4 in values:
            return "Four of a kind", 25
        elif 3 in values and 2 in values:
            return "Full house", 15
        elif is_straight:
            return "Straight", 12
        elif 3 in values:
            return "Three of a kind", 8
        elif values.count(2) == 2:
            return "Two pair", 5
        elif 2 in values:
            return "One pair", 2
        else:
            return "Nothing", -5  

    def play_round(self):
        """1回分のゲームを行い、(出目, 役名, 配当, 新しい所持金)を返す"""
        dice = self.roll_dice()
        hand_name, payoff = self.evaluate_hand(dice)
        self.bankroll += payoff
        return dice, hand_name, payoff, self.bankroll
