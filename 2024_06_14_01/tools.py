from tkinter.simpledialog import Dialog
from tkinter import ttk
from tkinter import Misc
import tkinter as tk
from data import Info
import tkintermapview as tkmap

class CustomMessagebox(Dialog):    
    def __init__(self, parent:Misc, title:str,site:Info):        
        self.site:Info = site
        super().__init__(parent=parent, title=title)

    def body(self, master):
        # 創建對話框主體。返回應具有初始焦點的控件。
        contain_frame = ttk.Frame(master)
        #====================    
        map_frame = ttk.Frame(contain_frame)
        map_widget = tkmap.TkinterMapView(map_frame,
                                         width=800,
                                         height=600,
                                         corner_radius=0
                                         )
        map_widget.pack()
        marker = map_widget.set_position(self.site.lat, self.site.lng,marker=True) #台北市位置
        marker.set_text(f'{sel