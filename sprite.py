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

    def move(self, x, y):
        self.x = x
        self.y = y

    def get_position(self):
        return (self.x, self.y)
    
    def get_charatext(self):
        return self.charatext
    
    def invisible(self, cvs):
        # カードを非表示にする
        cvs.create_rectangle(self.x - 61, self.y - 92, self.x + 60, self.y + 92,
                             fill="#007400", outline="#007400")
    
    def selected(self, cvs):
        self.select = True
        # 選択状態の表示（例: 所定の位置に移動する）
        self.invisible(cvs)
        cvs.create_image(self.x, self.y - 240, image=self.image_card)
    
    def deselected(self, cvs):
        self.select = False
        # 非選択状態の表示（例: 元の位置に戻す）
        self.invisible(cvs)
        cvs.create_image(self.x, self.y + 240, image=self.image_card)
    
    def is_selected(self):
        return self.select