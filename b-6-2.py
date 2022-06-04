# pyxel.run (外部サイトにリンクしています。)を呼び出すと、イベントループの実行が始まります。引数として2つの関数を渡しますが、この2つの関数がイベントループからほぼ一定時間ごとに（標準では毎秒30回）呼び出されます。

# updateは、主に変数の値の更新などプログラム内部の処理を行うための関数です。
# drawは、主に図形の描画を行うための関数です。

# updateとdrawは必ず交互に呼び出されるとは限らず、処理のタイミングによってupdateが複数回呼び出されてからdrawが1回呼び出されることもあります。

# global aは、グローバル変数（関数の外で定義された変数）のaを関数の中でも使うための宣言です。

# while文は、繰り返しを行う条件を指定し、その条件が成り立っている間、同じ処理を繰り返し実行します。

# （ヒント：円が回っているように見えますが、練習問題 B-6-1の位置と方向をずらして4個の円を描いているだけです。まず(100,0)から(200,100)へ繰り返し移動する円を描き、それから残りの3個を考えましょう。）
# ---------------------------------------------------------

# このアニメーションは、図形が領域内をバウンドしているわけではない。四つの箇所で同様の動きをする処理が互いの始点終点と重なり合い、あたかも図形が方向を変えて動いているかのように錯覚してしまうだけ。結局は始点と終点の二点間を移動しているに過ぎない。


import pyxel
pyxel.init(200,200)
a = 0

def update():
    global a
    a += 1

def draw():
    global a
    pyxel.cls(7)
    a %= 100
    pyxel.circ(100+a, a, 10, 0)
    pyxel.circ(200-a, 100+a, 10, 0)
    pyxel.circ(100-a, 200-a, 10, 0)
    pyxel.circ(a, 100-a, 10, 0)

pyxel.run(update, draw)