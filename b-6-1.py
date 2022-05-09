# pyxel.run (外部サイトにリンクしています。)を呼び出すと、イベントループの実行が始まります。引数として2つの関数を渡しますが、この2つの関数がイベントループからほぼ一定時間ごとに（標準では毎秒30回）呼び出されます。

# updateは、主に変数の値の更新などプログラム内部の処理を行うための関数です。
# drawは、主に図形の描画を行うための関数です。

# updateとdrawは必ず交互に呼び出されるとは限らず、処理のタイミングによってupdateが複数回呼び出されてからdrawが1回呼び出されることもあります。

# global aは、グローバル変数（関数の外で定義された変数）のaを関数の中でも使うための宣言です。

# while文は、繰り返しを行う条件を指定し、その条件が成り立っている間、同じ処理を繰り返し実行します。

import pyxel
pyxel.init(200,200)
a = 0

while True:
    if a <= 200:
        def update():
            global a
            a += 1
        def draw():
            global a
            pyxel.cls(7)
            pyxel.circ(a+100, a+100, 10, 0)
        pyxel.run(update, draw)
    else:
        a -=200
# pyxel.run (外部サイトにリンクしています。)を呼び出すと、イベントループの実行が始まります。引数として2つの関数を渡しますが、この2つの関数がイベントループからほぼ一定時間ごとに（標準では毎秒30回）呼び出されます。


# import pyxel
# pyxel.init(200,200)
# a = 0

# while True:
#     pyxel.cls(7)
#     pyxel.circ(a, a, 10, 0)
#     pyxel.flip()
#     a += 1