# pyxel.run (外部サイトにリンクしています。)を呼び出すと、イベントループの実行が始まります。引数として2つの関数を渡しますが、この2つの関数がイベントループからほぼ一定時間ごとに（標準では毎秒30回）呼び出されます。

# updateは、主に変数の値の更新などプログラム内部の処理を行うための関数です。
# drawは、主に図形の描画を行うための関数です。

# updateとdrawは必ず交互に呼び出されるとは限らず、処理のタイミングによってupdateが複数回呼び出されてからdrawが1回呼び出されることもあります。

# global aは、グローバル変数（関数の外で定義された変数）のaを関数の中でも使うための宣言です。

# while文は、繰り返しを行う条件を指定し、その条件が成り立っている間、同じ処理を繰り返し実行します。
# （ヒント：どちら方向に動いているかを覚えておく変数が必要になります。）
# ---------------------------------------------------------

# 変数を二つ用意する？。＋方向に進む変数のaが２００の位置に達した時、ー方向に進む変数をaが０になるまで繰り返す、というイメージ。

import pyxel
pyxel.init(200,200)
a = 0

def update():
    global a
    a += 1

def update_minus():
    global a
    a -= 1

# def update_total():
#     global a

def draw():
    global a
    pyxel.cls(7)
    a %= 200
    pyxel.circ(a, a, 10, 0)

pyxel.run(update, draw)
# pyxel.run(update_minus, draw)

# pyxel.run(update_total, draw)
