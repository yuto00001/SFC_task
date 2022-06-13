# 次のプログラムはマウスカーソルの位置に円を描きます。ウィンドウの中でマウスを動かしてみてください。
# 変数pyxel.mouse_x (外部サイトにリンクしています。)とpyxel.mouse_y (外部サイトにリンクしています。)の値は、マウスカーソルのX座標とY座標になっています。
# passは、何もしないという命令です。この場合はプログラム内部で計算するものが何もないため、draw関数だけで処理しています。
# draw関数の最初でpyxel.clsを呼び出して描画領域を塗りつぶすのをやめると、それまでに描いた図形が全部残るようになります。
# import pyxel

# pyxel.init(200,200)
# pyxel.cls(7)

# def update():
#     pass

# def draw():
#     pyxel.circ(pyxel.mouse_x, pyxel.mouse_y, 0, 0)

# pyxel.run(update, draw)

# ・・・・・・・・・・・・・・・・・・・・・

import pyxel

pyxel.init(200,200)
pyxel.mouse(True)

x=0
y=0

def update():
    global x, y
    if pyxel.btn(pyxel.KEY_SPACE):
        x = pyxel.mouse_x
        y = pyxel.mouse_y

def draw():
    pyxel.cls(7)
    global x, y
    pyxel.line(0, 0, x, y, 0)

pyxel.run(update, draw)
