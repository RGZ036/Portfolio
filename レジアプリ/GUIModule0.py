import tkinter as tk
import tkinter.ttk as ttk

#class
class G_Frame(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.grid(row=0, column=0, sticky="nsew", pady=20)

class G_Frame1(tk.Frame):
    def __init__(self,master,row,column):
        super().__init__(master=master)
        self.grid(row=0, column=0, sticky="nsew", pady=20)

#FCB = FrameChangeButton
class G_FCB(ttk.Button):
    def __init__(self,master,text,master2,row,column):
        super().__init__(master=master,text=text,command=lambda: change_frame(master2))
        self.grid(row=row, column=column)

#FB = FunctionButton
class G_FB(ttk.Button):
    def __init__(self,master,text,command,row,column):
        super().__init__(master=master,width=20,text=text,command=command)
        self.grid(row=row, column=column)

class G_Lab(tk.Label):
    def __init__(self,master,text,row,column):
        self.text = text
        super().__init__(master=master,text=self.text,font=(25))
        self.grid(row=row, column=column)
    def __str__(self):
        return self.text

class G_Lab1(tk.Label):
    def __init__(self,master,text,height,width,row,column):
        super().__init__(master=master,text=text,height=height,width=width)
        self.grid(row=row, column=column)

class G_Lab2(tk.Label):
    def __init__(self,master,text,row,column,columnspan):
        super().__init__(master=master,text=text,font=(25))
        self.grid(row=row, column=column,columnspan=columnspan)
    

class Pl_Lab(tk.Label):
    def __init__(self,master,text,x,y):
        super().__init__(master=master,text=text)
        self.place(x=x,y=y)

class Pl_FB(tk.Button):
    def __init__(self,master,text,x,y):
        super().__init__(master=master,text=text)
        self.place(x=x,y=y)

class G_Can(tk.Canvas):
    def __init__(self,master,bg,height,width,row,column):
        super().__init__(master=master,bg=bg,height=height,width=width)
        self.grid(row=row, column=column)
        
class G_EB(tk.Entry):
    def __init__(self,master,row,column):
        super().__init__(master=master,font=15)
        self.grid(row=row, column=column)

class G_CB(tk.Checkbutton):
    def __init__(self,master,check_var,row,column):
        super().__init__(master=master,variable=check_var)
        self.grid(row=row,column=column)

#def
def change_frame(window):
    window.tkraise()

