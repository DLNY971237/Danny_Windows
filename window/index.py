import tkinter as tk
from tkinter import ttk

def get_names() -> list[str]:
    with open('names.txt',encoding='utf-8') as file:
        content:str = file.read()
    names:list[str]= content.split()
    return names

class Window(tk.Tk):
    def __init__(self,title:str="Hello! Tikinter!",**kwargs):
        super().__init__(**kwargs)
        #多做一些事
        self.title(title)
        label:ttk.Label= ttk.Label(self,
                                   text="Hello! World!",
                                   font=('Arial',20,'bold'),
                                   foreground='#f00')
        label.pack(padx=30,
                   pady=30)

if __name__ == '__main__':
    names:list[str] = get_names()
    window:Window = Window(title="這是我的第一個GUI程式")
    window.mainloop()