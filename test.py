import pyxel

pyxel.init(200, 200)
pyxel.cls(7)
for a in range(0, 100, 100):
    pyxel.line(0, 100+a, 100+a, 0, 0)
    pyxel.flip()
pyxel.show()
