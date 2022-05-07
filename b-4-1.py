import pyxel

pyxel.init(200, 200)
pyxel.cls(7)
for b in range(10, 200, 40):
    for a in range(10, 200, 20):
    # (始点, 終点, 間隔)
        if ((a-10)/20) % 2 == 0:
            pyxel.circ(a, b, 10, 6)
        else:
            pyxel.circ(a, b, 10, 14)
            # pyxel.circ(100, 100, 10, 0)は、座標(100,100)を中心にして半径10の円を0番の色で描きます。
            # pyxel.circ(a, b, 10, 0)
for d in range(30, 200, 40):
    for c in range(10, 200, 20):
    # (始点, 終点, 間隔)
        if ((c-10)/20) % 2 == 0:
            pyxel.circ(c, d, 10,14)
        else:
            pyxel.circ(c, d, 10, 6)
            # pyxel.circ(100, 100, 10, 0)は、座標(100,100)を中心にして半径10の円を0番の色で描きます。
            # pyxel.circ(a, b, 10, 0)
pyxel.show()
