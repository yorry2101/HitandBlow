# graphic interface for Hit & Blow game
# 内容はまだない
import sys
from game_manager import GameManager
class GraphicInterface:
    def __init__(self, answer: str):
        self.game_manager = GameManager(answer)