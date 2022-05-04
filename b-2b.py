import pyxel

pyxel.init(200, 200)
pyxel.cls(7)
for a in range(0, 200, 10):
    # (始点, 終点, 間隔)
    pyxel.line(0, 0+a, 200-a, 0, 0)
    # pyxel.line(0, 0+a, 200, 0, 0)
    # pyxel.line(x始点, y始点, x終点, y終点, 色？)
    # 片方の値を増やしながらもう片方を減らす処理を繰り返す→ペンの回転
    pyxel.flip()
pyxel.show()