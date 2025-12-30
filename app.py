import tkinter

# NOTE: アプリの土台
root = tkinter.Tk()

# NOTE: アプリのタイトル、画面上のバーに表示
root.title('マイアプリ')

# NOTE: 画面の横*縦のサイズを設定
root.geometry('800x600')

# NOTE: 部品を一つのまとまりとして扱うクラスを作成、それが書かれたtkinter.Frameクラスを継承
class Application(tkinter.Frame):
    
    # NOTE: アプリの土台を受け取っておく
    def __init__(self,root):
        # NOTE: 基底クラス(Tkinter.Frame)のイニシャライザを呼び、アプリの土台を渡す
        super().__init__(root, 
                         width=420, 
                         height=320, 
                         borderwidth = 4, 
                         relief='groove')
        self.pack()
        self.pack_propagate(0)
        self.root = root


# NOTE: アプリ起動(本来はこの前に部品を作成)
root.mainloop()