import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
import GUIModule0
from datetime import datetime

#class
class Application(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.Mainframe = GUIModule0.G_Frame(self.master)
    
    def module(self,master):
        # 押されているキーを保持するセット
        self.pressed_keys = set()

        # キーが押されたときにセットに追加
        def on_key_press(event):
            self.pressed_keys.add(event.keysym)
            check_key_combination()  # 組み合わせをチェック

        # キーが離されたときにセットから削除
        def on_key_release(event):
            self.pressed_keys.discard(event.keysym)
            check_key_combination()  # 組み合わせをチェック

        # 特定のキーの組み合わせをチェック
        def check_key_combination():
            if "Control_L" in self.pressed_keys and "Shift_L" in self.pressed_keys:
                print("CtrlキーとShiftキーが同時に押されています")
                print(self.oreder_check_num)
                if self.oreder_check_num <= self.order_count-1:
                    self.LT3[self.oreder_check_num].config(fg = "red")
                    self.label1_order[self.oreder_check_num].config(fg = "red")
                    self.oreder_check_num += 1
                    if self.oreder_check_num > 3:
                        self.LT3[self.destroy_count].destroy()
                        self.checkbox1_order[self.destroy_count].destroy()
                        self.label1_order[self.destroy_count].destroy()
                        self.destroy_count += 1
        
        #合計金額算出
        def calculateTest1(self,num):
            self.filename = str(datetime.now().strftime('%Y_%m-%d')) + ".txt"
            tatal_cost = 0
            for i in range(num):
                tatal_cost += self.cost[i]*int(self.EB1[i].get())
                self.label_every_good_cost[i].config(text = str(self.cost[i]*int(self.EB1[i].get())))
                self.num_orders_count[i] += int(self.EB1[i].get())
            #合計金額が0以下の時は処理を飛ばす
            if tatal_cost > 0:
                self.LT2_4.config(text = str(tatal_cost))
                date = str(datetime.now().strftime('%Y_%m-%d__%H-%M-%S'))
                order = f"注文{self.order_count}, {self.goods_name[0]}: {int(self.EB1[0].get())}個, {self.goods_name[1]}: {int(self.EB1[1].get())}個, {self.goods_name[2]}: {int(self.EB1[2].get())}個, {self.goods_name[3]}: {int(self.EB1[3].get())}個, {self.goods_name[4]}: {int(self.EB1[4].get())}個  {date}"
                self.LT3.append(GUIModule0.G_Lab2(self.frame1,order,(6+self.goods_num+self.order_count),0,6))
                var = tk.BooleanVar()
                self.checkbox1_order.append(GUIModule0.G_CB(self.order_frame,var,self.order_count,0))
                self.label1_order.append(GUIModule0.G_Lab2(self.order_frame,order,self.order_count,1,2))
                self.check_vars.append(var)
                self.order_count += 1
                with open(self.filename, "a") as file:
                    file.write(order + "\n")
                self.LT2_4.update_idletasks()
            else:
                pass
        
        #お釣りの算出
        def calulate_order(self):
            received = self.EB2.get()
            cost = self.LT2_4.cget("text")
            self.LT2_6.config(text=str(int(received)-int(cost)))
            self.LT2_6.update()
            print(self.label_every_good_cost)
        
        #商品の個数の増加
        def increasing_goods_count(self,EB):
            num = int(EB.get())
            EB.delete(0, tk.END)
            EB.insert(0,str(num+1))
            EB.update()
        
        #商品の個数の減少
        def decreasing_goods_count(self,EB):
            num = int(EB.get())
            if num > 0:
                EB.delete(0, tk.END)
                EB.insert(0,str(num-1))
                EB.update()
            else:
                pass
        
        #商品の個数のリセット
        def liset_goods_count(self):
            for i in range(self.goods_num):
                self.EB1[i].delete(0, tk.END)
                self.EB1[i].insert(0, "0")
                self.label_every_good_cost[i].config(text="0")
            self.LT2_1[-1] = GUIModule0.G_Lab(self.frame1,str(self.cost[-1]),3+self.goods_num-1,1)
            self.label_every_good_cost[-1].destroy()
            self.label_every_good_cost[-1] = GUIModule0.G_Lab(self.frame1,"0",3+self.goods_num-1,5)
                
        #register_frame
        #キーボード入力の機能の実装
        self.master.bind("<KeyPress>",on_key_press)
        self.master.bind("<KeyRelease>",on_key_release)
        self.frame1 = GUIModule0.G_Frame(self.master)
        self.label1 = GUIModule0.G_Lab(self.frame1,"RegisterApp",0,0)
        self.FCB_frame1_Mainframe = GUIModule0.G_FCB(self.frame1,"Mainframe",self.Mainframe,1,0)
        self.FCB_Mainframe_frame1 = GUIModule0.G_FCB(self.Mainframe,"registerMain",self.frame1,1,0)
        #各目の名前
        self.LT1_2_0 = GUIModule0.G_Lab(self.frame1,"商品名",2,0)
        self.LT1_2_1 = GUIModule0.G_Lab(self.frame1,"価格",2,1)
        self.LT1_2_2 = GUIModule0.G_Lab(self.frame1,"個数",2,2)
        self.LT1_2_3 = GUIModule0.G_Lab(self.frame1,"商品別総価格",2,5)
        self.LT1_2_4 = GUIModule0.G_Lab(self.frame1,"合計額",2,6)
        self.LT1_2_5 = GUIModule0.G_Lab(self.frame1,"受取額",2,7)
        self.LT1_2_6 = GUIModule0.G_Lab(self.frame1,"お釣り",2,8)
        #商品個数入力欄のリスト
        self.EB1 = []
        #商品個数の増加ボタン
        self.FB_increasing = []
        self.FB_decreasing = []
        #各商品の名前
        self.goods_name = ["磯辺","みたらし","こしあん","芋あん","星見スペシャル"]
        self.LT2_0 = []
        #各商品の値段のリスト
        self.cost = [200,200,200,200,500]
        self.LT2_1 = []
        self.label_every_good_cost = []
        #商品の種類数
        self.goods_num = 5
        #注文数
        self.order_count = 1
        self.checkbox1_order = []
        self.label1_order = []
        #注文処理数
        self.oreder_check_num = 0
        self.check_vars = []
        for i in range(len(self.goods_name)):
            self.LT2_0.append(GUIModule0.G_Lab(self.frame1,self.goods_name[i],3+i,0))
            self.LT2_1.append(GUIModule0.G_Lab(self.frame1,str(self.cost[i]),3+i,1))
            #商品個数入力欄
            self.EB1.append(GUIModule0.G_EB(self.frame1,3+i,2))
            self.FB_increasing.append(GUIModule0.G_FB(self.frame1,"+",lambda i=i:increasing_goods_count(self,self.EB1[i]),3+i,3))
            self.FB_decreasing.append(GUIModule0.G_FB(self.frame1,"-",lambda i=i:decreasing_goods_count(self,self.EB1[i]),3+i,4))
            self.label_every_good_cost.append(GUIModule0.G_Lab(self.frame1,"0",3+i,5))
        #商品別金額計算
        self.FB1 = GUIModule0.G_FB(self.frame1,"計算",lambda:calculateTest1(self,self.goods_num),9,6)
        #合計金額表示欄
        self.LT2_4 = GUIModule0.G_Lab(self.frame1,"0",3+self.goods_num,6)
        self.LT3 = []
        #受取金額
        self.EB2 = GUIModule0.G_EB(self.frame1,3+self.goods_num,7)
        #お釣り
        self.LT2_6 = GUIModule0.G_Lab(self.frame1,"0",3+self.goods_num,8)
        self.FB2 = GUIModule0.G_FB(self.frame1,"会計",lambda:calulate_order(self),4+self.goods_num,7)
        #会計入力リセット
        self.FB3 = GUIModule0.G_FB(self.frame1,"会計リセット",lambda:liset_goods_count(self),4+self.goods_num,9)
        #記録用変数
        self.num_orders_count = [0 for i in range(self.goods_num)]
        #消去数
        self.destroy_count = 0
        #oreder_frame
        root_oreder = tk.Tk()
        root_oreder.geometry('1000x800')
        self.order_frame = GUIModule0.G_Frame(root_oreder)
        liset_goods_count(self)
        
        

#def
def change_frame(window):
    window.tkraise()

#main
if __name__ == "__main__":
    root = tk.Tk()
    root.title = "GUIMain"
    root.geometry("1200x1000")
    app = Application(root)
    app.module(root)
    app.mainloop()
