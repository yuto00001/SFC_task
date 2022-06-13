

# pyxel.btn (外部サイトにリンクしています。)は、引数で指定したキーが押されていればTrue、押されていなければFalseを返します。
# pyxel.KEY_SPACEは、スペースキーに割り当てられた番号を示します。他のキーについては定義ファイル (外部サイトにリンクしています。)の中のKEY_で始まる単語を探してください。
import pyxel

pyxel.init(200,200)

a = 0
direction = 1

def update():
    global a
    global direction
    a += 1 * direction
    if pyxel.btn(pyxel.KEY_SPACE):
        direction *= -1

def draw():
    global a
    pyxel.cls(7)
    pyxel.circ(a, a, 10, 0)

pyxel.run(update, draw)
