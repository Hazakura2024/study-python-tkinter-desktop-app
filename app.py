import tkinter

# NOTE: 部品を一つのまとまりとして扱うクラスを作成、それが書かれたtkinter.Frameクラスを継承
class Application(tkinter.Frame):
    
    # NOTE: アプリの土台を受け取っておく
    # NOTE: root=Noneで任意とし、エラーを防止
    def __init__(self,root=None):
        # NOTE: 基底クラス(Tkinter.Frame)のイニシャライザを呼び、アプリの土台を渡す
        super().__init__(root, 
                         width=380, 
                         height=280, 
                         borderwidth = 1, 
                         # NOTE: 枠線の立体感を出す
                         relief='groove')
        self.root = root
        # NOTE: 作った部品を、親ウィンドウの中に「上から下に」配置する。grid()なら「マス目状に」
        self.pack()
        # NOTE: Tkinterは気を利かせて、**「あれ？中身はボタン1つだけなんだ。じゃあ親のサイズもボタンにぴったり合うまで小さくしてあげよう！」**と、380x280の指定を無視してギュッと縮めてしまいます。
        # NOTE: 親（Frame）が、中身（ボタンなど）のサイズに合わせて勝手に縮むのを禁止する
        self.pack_propagate(0)
        self.create_widgets()
        
    # NOTE: ウィジェットを作成する処理を一つにまとめる
    def create_widgets(self):
        # NOTE: 終了ボタンを作成
        quit_btn = tkinter.Button(self)
        # NOTE: ボタンに表示する文字を設定
        quit_btn['text'] = '閉じる'
        # NOTE: ボタンを押されたら実行される処理
        quit_btn['command'] = self.root.destroy
        
        # NOTE: 中央に配置
        quit_btn.pack(side='bottom')



# NOTE: アプリの土台
root = tkinter.Tk()

# NOTE: アプリのタイトル、画面上のバーに表示
root.title('マイアプリ')

# NOTE: 画面の横*縦のサイズを設定
root.geometry('400x300')

# NOTE: アプリのインスタンス化
app = Application(root=root)

# NOTE: アプリ起動(本来はこの前に部品を作成)
app.mainloop()