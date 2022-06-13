import pyxel
# 別の変数bを使うことと、bがY座標の変化を示すことに注意しなさい。
pyxel.init(201, 201)
pyxel.cls(7)
for b in range(0, 201, 20):
# (始点, 終点, 間隔)
    for a in range(0, 201, 20):
        pyxel.line(0+a, 0, 0+b, 201, 0)
        # pyxel.line(x始点, y始点, x終点, y終点, 色？)
        # pyxel.circ(100, 100, 10, 0)は、座標(100,100)を中心にして半径10の円を0番の色で描きます。
        # pyxel.circ(a, b, 10, 0)
pyxel.show()
