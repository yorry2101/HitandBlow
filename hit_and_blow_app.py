# hit and blow_app.py
#from text_interface import TextInterface
from game_manager import GameManager
from graphic_interface import GraphicInterface
import random

if __name__ == "__main__":
    answer = ""
    used = []

    while len(answer) < 4:
        d = random.randint(0, 9)
        if d not in used:
            used.append(d)
            answer += str(d)  # ここでは固定の答えを使用。実際にはランダム生成などが望ましい。
    #interface = TextInterface(answer)
    interface = GraphicInterface(answer)
    interface.start()