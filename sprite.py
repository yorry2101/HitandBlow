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
        self.id = cvs.create_image(self.x, self.y, image=self.image_card)

    def update(self, cvs):
        print(f"Updating card {self.charatext} to position ({self.x}, {self.y})")  # デバッグ用出力
        # 座標の更新
        cvs.coords(self.id, self.x, self.y)
        cvs.update()
    
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
        cvs.itemconfig(self.id, state='hidden')
    
    def selected(self, cvs):
        print(f"Selecting card {self.charatext}")  # デバッグ用出力
        self.select = True
        # 選択状態の表示（例: 所定の位置に移動する）
        self.move(self.x, self.y - 240)
        self.update(cvs)
    
    def deselected(self, cvs):
        print(f"Deselecting card {self.charatext}")  # デバッグ用出力
        self.select = False
        # 非選択状態の表示（例: 元の位置に戻す）
        self.move(self.x, self.y + 240)
        self.update(cvs)
    
    def is_selected(self):
        return self.select