# X座標の範囲によって色を変えて円を描きます。
# range(始点, 終点, 間隔)
# pyxel.circ(100, 100, 10, 0)は、座標(100,100)を中心にして半径10の円を0番の色で描きます。
# pyxel.circ(a, b, 10, 0)

# aは、10から200の間を20の間隔で繰り返す。
# aが40より小さい場合、右の円を描く。(a, 10, 10, 2)
# aが40以上かつ100以下の場合、・・
# aが100以上かつ160以下の場合、・・
# aが160以上の場合、・・


import pyxel

pyxel.init(200, 200)
pyxel.cls(7)
for b in range(10, 200, 20):
    for a in range(10, 200, 20):
        if b <= 100-a:
            pyxel.circ(b, a, 10, 2)
        elif b <= 200-a:
            pyxel.circ(b, a, 10, 3)
        elif b <= 300-a:
            pyxel.circ(b, a, 10, 6)
        else:
            pyxel.circ(b, a, 10, 14)
pyxel.show()
