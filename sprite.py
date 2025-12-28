# sprite.py
# カードスプライトモジュール
import tkinter as tk

# カードクラス
class CardSprite:

    def __init__(self, cvs, x, y, charatext):
        self.x = x # x座標
        self.y = y # y座標
        self.charatext = charatext # カードの文字内容
        self.select = False # 選択状態

        # 画像の読み込み
        file_image = "images/card_{}.png".format(charatext)
        self.image_card = tk.PhotoImage(file=file_image)

        # カードを描画
        cvs.create_image(self.x, self.y, image=self.image_card)

    def update(self, cvs):
        # 座標の更新
        cvs.create_image(self.x, self.y, image=self.image_card)
    
    def set_x(self, x):
        self.x = x
    
    def set_y(self, y):
        self.y = y
    
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
    
    def get_position(self):
        return (self.x, self.y)
    
    def get_charatext(self):
        return self.charatext
    
    def set_selected(self, select):
        self.select = select
    
    def is_selected(self):
        return self.select