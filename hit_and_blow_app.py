# hit and blow_app.py
#from text_interface import TextInterface
from game_manager import GameManager
from graphic_interface import GraphicInterface
if __name__ == "__main__":
    answer = "1234"  # ここでは固定の答えを使用。実際にはランダム生成などが望ましい。
    #interface = TextInterface(answer)
    interface = GraphicInterface(answer)
    interface.start()