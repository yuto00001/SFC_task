# 1. 青と白の円の大きさを調整して重複円を作る。（for文の数は重複円の数＝５つ）
# 2. if ((a-10)/20) % 2 == 0: を使って、10pixずれた位置に配列する。
# 3. pyxel.circの座標を、(x, a-10, x, x) のようにずらす値を任意の箇所に挿入し、ユニークな模様を生成する
# 4. 結果的に模様同士の重複により、複雑な模様が生まれる。
# デザインの参考は、日本の伝統模様である”青海波(せいがいは)”を用いた。

import pyxel

pyxel.init(200, 200)
pyxel.cls(7)
for b in range(10, 220, 20):
    for a in range(10, 220, 20):
        if ((a-10)/20) % 2 == 0:
            pyxel.circ(b, a, 10, 5)
        else:
            pyxel.circ(b-10, a-10, 10, 5)

for b in range(10, 220, 20):
    for a in range(10, 220, 20):
        if ((a-10)/20) % 2 == 0:
            pyxel.circ(b, a, 8, 7)
        else:
            pyxel.circ(b-10, a, 8, 7)

for b in range(10, 220, 20):
    for a in range(10, 220, 20):
        if ((a-10)/20) % 2 == 0:
            pyxel.circ(b, a, 6, 5)
        else:
            pyxel.circ(b-10, a-10, 6, 5)

for b in range(10, 220, 20):
    for a in range(10, 220, 20):
        if ((a-10)/20) % 2 == 0:
            pyxel.circ(b, a-10, 4, 7)
        else:
            pyxel.circ(b-10, a-10, 4, 7)

for b in range(10, 220, 20):
    for a in range(10, 220, 20):
        if ((a-10)/20) % 2 == 0:
            pyxel.circ(b, a-10, 2, 5)
        else:
            pyxel.circ(b-10, a, 2, 5)

pyxel.show()
