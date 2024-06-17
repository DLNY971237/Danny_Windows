import tkinter as tk
from tkinter import ttk
from tkinter import Misc
from PIL import Image,ImageTk


class Example(ttk.Frame):
    def __init__(self,master:Misc,**kwargs):
        super().__init__(master=master,**kwargs)
        master.title('Lines')
        self.configure({'borderwidth':2,'relief':'groove'})
        #self.config({'borderwidth':2,'relief':'groove'})        
        #self['borderwidth'] = 2
        #self['relief'] = 'groove' 
        canvas = tk.Canvas(self)
        canvas.create_line(15, 30, 200,30)
        canvas.create_line(300,35, 300, 200,dash=(8,2))
        canvas.create_line(55,85,155,85,105,180,55,85)
        canvas.pack(expand=True,fill='both')      
        self.pack(expand=True,fill='both')

class Example1(ttk.Frame):
    def __init__(self,master:Misc,**kwargs):
        super().__init__(mas