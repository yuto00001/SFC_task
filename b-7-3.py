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
# スペースキーを押している間は、押し始めたときのマウスカーソルの位置から現在のマウスカーソルの位置まで直線を描きます。
# スペースキーを離すと、離す前の最後の直線が残ります。
# もう一度スペースキーを押すと、また新しい直線を描きます。

import pyxel

pyxel.init(200,200)
pyxel.mouse(True)

x=pyxel.mouse_x
y=pyxel.mouse_y
xx=pyxel.mouse_x
yy=pyxel.mouse_y
hold_key = False

def update():
    global x, y, xx, yy, hold_key
    if pyxel.btn(pyxel.KEY_SPACE):
        if not hold_key:
            xx = pyxel.mouse_x
            yy = pyxel.mouse_y
        x = pyxel.mouse_x
        y = pyxel.mouse_y
        hold_key = True
    if pyxel.btnr(pyxel.KEY_SPACE):
        hold_key = False

def draw():
    global x, y, xx, yy
    global xx, yy
    pyxel.cls(7)
    pyxel.line(x, y, xx, yy, 0)


pyxel.run(update, draw)
# import pyxel

# pyxel.init(200,200)
# pyxel.mouse(True)

# x=pyxel.mouse_x
# y=pyxel.mouse_y
# xx=pyxel.mouse_x
# yy=pyxel.mouse_y

# def update():
#     global x, y, xx, yy
#     if pyxel.btn(pyxel.KEY_SPACE):
#         x = pyxel.mouse_x
#         y = pyxel.mouse_y
#     if pyxel.btnr(pyxel.KEY_SPACE):
#         xx = pyxel.mouse_x
#         yy = pyxel.mouse_y

# def draw():
#     global x, y, xx, yy
#     global xx, yy
#     pyxel.cls(7)
#     pyxel.line(x, y, xx, yy, 0)


# pyxel.run(update, draw)


# import pyxel

# pyxel.init(200,200)
# pyxel.mouse(True)

# x=pyxel.mouse_x
# y=pyxel.mouse_y
# xx=pyxel.mouse_x
# yy=pyxel.mouse_y
# pressing = False
# drawn_line = None

# def update():
#     global x, y, xx, yy, pressing, drawn_line
#     if pyxel.btn(pyxel.KEY_SPACE):
#         drawn_line = None
#         if pressing == False:
#             x = pyxel.mouse_x
#             y = pyxel.mouse_y
#             pressing = True
#         xx = pyxel.mouse_x
#         yy = pyxel.mouse_y

#     if pyxel.btnr(pyxel.KEY_SPACE):
#         pressing = False
#         drawn_line = (x,y,xx,yy)

# def draw():
#     global x, y, xx, yy
#     pyxel.cls(7)

#     if drawn_line:
#         pyxel.line(*drawn_line,0)
#     else:
#         pyxel.line(x, y, xx, yy, 0)

# pyxel.run(update, draw)
