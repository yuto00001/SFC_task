# pyxel.run (外部サイトにリンクしています。)を呼び出すと、イベントループの実行が始まります。引数として2つの関数を渡しますが、この2つの関数がイベントループからほぼ一定時間ごとに（標準では毎秒30回）呼び出されます。

# updateは、主に変数の値の更新などプログラム内部の処理を行うための関数です。
# drawは、主に図形の描画を行うための関数です。

# updateとdrawは必ず交互に呼び出されるとは限らず、処理のタイミングによってupdateが複数回呼び出されてからdrawが1回呼び出されることもあります。

# global aは、グローバル変数（関数の外で定義された変数）のaを関数の中でも使うための宣言です。

# while文は、繰り返しを行う条件を指定し、その条件が成り立っている間、同じ処理を繰り返し実行します。
# ---------------------------------------------------------
# プログラムが最後まで実行されたのちに、再び最初から実行される処理が必要。
# [想定1] while文によって図形の移動を可能にし、その処理自体をfor文で囲み,ひとつの処理として捉え,繰り返す。

# [想定2] while文によって図形の移動を可能にし、その処理自体をもういちどwhile文で囲み,繰り返しを可能にする条件のもと,無限に繰り返す。

# [想定3] if文を使って、aが200を超えたら処理を中断し、aを-200する

# ---------------------------------------------------------
# 無限ループをどう扱うか。ー 扱わない。
# 定義関数(def関数)をどう活かすか。　ー　既に活用済み。
# 変数のスコープ(有効範囲)をどう活かすか。ー　既に活用済み。

# 無限ループのwhile文をきちんと終わらせ、その処理をさらにwhile文で囲うことで、二重構文とする。


# import pyxel
# pyxel.init(200,200)
# a = 0

# def update():
#     global a
#     a += 1

# def draw():
#     global a
#     pyxel.cls(7)
#     pyxel.circ(100+a, 100+a, 10, 0)

# pyxel.run(update, draw)

# if文を使って、aが200を超えたら処理を中断し、aを-200する。という方法を考えたが、pyxel.runがaの総数を取得していない(取得しているのはdef関数)ため、命令が効かないという段階。
import pyxel
pyxel.init(200,200)
a = 0

def update():
    global a
    a += 1

def draw():
    global a
    pyxel.cls(7)
    pyxel.circ(100+a, 100+a, 10, 0)

if a<= 200:
    pyxel.run(update, draw)
else:
    a - 200


# import pyxel

# pyxel.init(200,200)

# a = 0

# while True:
#     pyxel.cls(7)
#     pyxel.circ(a, a, 10, 0)
#     pyxel.flip()
#     a += 1

# ボツ--------------
# import pyxel

# pyxel.init(200,200)

# a = 0

# while True:
#     if a >= 200:
#         pyxel.cls(7)
#         pyxel.circ(a, a, 10, 0)
#         pyxel.flip()
#         a += 1
#     else:
#         break

# --

# import pyxel
# pyxel.init(200,200)
# a = 0

# for i in range(10):
#     while True:
#         if a <= 100:
#             def update():
#                 global a
#                 a += 1
#             def draw():
#                 global a
#                 pyxel.cls(7)
#                 pyxel.circ(a, a, 10, 0)
#             pyxel.run(update, draw)
