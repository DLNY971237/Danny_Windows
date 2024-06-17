from ttkthemes import ThemedTk
import tkinter as tk
from tkinter import ttk, messagebox,Misc
import data
from data import FilterData,Info
from tools import CustomMessagebox



class Window(ThemedTk):
    def __init__(self,theme:str='arc',**kwargs):
        super().__init__(theme=theme,**kwargs)
        self.title('台北市YouBike2.0及時資料')
        try:
            self.__data = data.load_data()
        except Exception as e:
            messagebox.showwarning(title='警告',message=str(e))
        
        self._display_interface()
        
    @property
    def data(self)->list[dict]:
        return self.__data
    

    def _display_interface(self):
        mainFrame = ttk.Frame(borderwidth=1,relief='groove')
        ttk.Label(mainFrame,text="台北市YouBike2.0及時資料",font=('arial',25)).pack(pady=(20,10))
        #=================================
        tableFrame = ttk.Frame(mainFrame)
        columns = ('sna', 'sarea', 'mday','ar','total','rent_bikes','retuen_bikes')
        tree = ttk.Treeview(tableFrame, columns=columns, show='headings')
        # define headings
        tree.heading('sna', text='站點')
        tree.heading('sarea', text='行政區')
        tree.heading('mday', text='時間')
        tree.heading('ar', text='地址')
        tree.heading('total', text='總數')
        tree.heading('rent_bikes', text='可借')
        tree.heading('retuen_bikes', text='可還')

        # 定義欄位寬度
        tree.column('sarea',width=70,anchor=tk.CENTER)
        tree.column('mday',width=120,anchor=tk.CENTER)
        tree.column('ar',minwidth=100)
        tree.column('total',width=50,anchor=tk.CENTER)
        tree.column('rent_bikes',width=50,anchor=tk.CENTER)
        tree.column('retuen_bikes',width=50,anchor=tk.CENTER)

        # bind使用者的事件
        tree.bind('<<TreeviewSelect>>', self.item_selected)


        
        
        # add data to the treeview
        for site in self.data:
            tree.insert('', tk.END,
                        values=(site['sna'],site['sarea'],site['mday'],site['ar'],site['total'],site['rent_bikes'],site['retuen_bikes']))
        
        tree.grid(row=0, column=0, sticky='nsew')

        scrollbar = ttk.Scrollbar(tableFrame, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky='ns')
        tableFrame.pack(expand=True,fill=tk.BOTH,padx=20,pady=20)
        #======================================
        self.pieChartFrame = PieChartFrame(mainFrame)
        self.pieChartFrame.pack(expand=True,fill='both')
        mainFrame.pack(expand=True,fill=tk.BOTH,padx=10,pady=10)

    def item_selected(self,event):
        tree = event.widget
        records:list[list] = []       
        for selected_item in tree.selection():
            item = tree.item(selected_item)            
            record:list = item['values']
            records.append(record)
        self.pieChartFrame.infos = records
        
        
            


class PieChartFrame(ttk.Frame):
    def __init__(self,master:Misc,**kwargs):
        super().__init__(master=master,**kwargs)
        self.configure({'borderwidth':2,'relief':'groove'})
        #self.config({'borderwidth':2,'relief':'groove'})        
        #self['borderwidth'] = 2
        #self['relief'] = 'groove'         

    @property
    def infos(self)->None:
        return None

    @infos.setter
    def infos(self,datas:list[list]) -> None:
        for w in self.winfo_children():
            w.destroy()
            
        for data in datas:
            sitename:str = data[0]
            area:str = data[1]
            info_time:str = data[2]
            address:str = data[3]
            total:int = data[4]
            rents:int = data[5]
            returns:int = data[6]
            oneFrame = ttk.Frame(self)
            ttk.Label(oneFrame,text=area).grid(row=0,column=0)
            oneFrame.pack(side='left')  
        


    
    



def main():
    window = Window(theme='breeze')
    window.mainloop()

if __name__ == '__main__':
    main()