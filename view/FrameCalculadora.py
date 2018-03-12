# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 05:34:47 2018

@author: nildo
"""

from tkinter import *
from model.Calculadora import Calculadora

class FrameCalculadora(Frame):
    def __init__(self, master):
        self.master = master
        self.initComponents()
        
    def initComponents(self):
        super().__init__(self.master)
        self.master["pady"] = 5
        self.master["padx"] = 5
        self.master.title("Calculadora simples")
        self.master.resizable(False, False)
        self.master.focus_force()
        self.pack()
        
        self.frame0 = Frame(self.master, pady=5, padx=5)
        self.frame1 = Frame(self.master)
        self.frame2 = Frame(self.master)
        self.frame3 = Frame(self.master)
        self.frame4 = Frame(self.master)
        self.frame5 = Frame(self.master)
        
        self.frame0.pack()
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack()
        self.frame5.pack()
        
        self.entrada = StringVar()
        self.fonte = ["Courier New", 14]
        
        self.entry = Entry(self.frame0)
        self.entry["width"] = 19
        self.entry["state"] = DISABLED
        self.entry["textvariable"]= self.entrada
        self.entry["font"] = self.fonte+["bold"]
        self.entry["justify"] = RIGHT
        self.entry.pack()
        
        self.btnAbreParenteses = Button(self.frame1)
        self.btnAbreParenteses["text"]   = "("
        self.btnAbreParenteses["font"]   = self.fonte
        self.btnAbreParenteses["width"]  = 4
        self.btnAbreParenteses["height"] = 2
        self.btnAbreParenteses["command"] = self.btnAbreParentesesAction
        self.btnAbreParenteses.pack(side=LEFT)
        
        self.btnFechaParenteses = Button(self.frame1)
        self.btnFechaParenteses["text"]   = ")"
        self.btnFechaParenteses["font"]   = self.fonte
        self.btnFechaParenteses["width"]  = 4
        self.btnFechaParenteses["height"] = 2
        self.btnFechaParenteses["command"] = self.btnFechaParentesesAction
        self.btnFechaParenteses.pack(side=LEFT)
        
        self.btnBack = Button(self.frame1)
        self.btnBack["text"]   = "<<"
        self.btnBack["font"]   = self.fonte
        self.btnBack["width"]  = 4
        self.btnBack["height"] = 2
        self.btnBack["command"]= self.btnBackAction
        self.btnBack.pack(side=LEFT)
        
        self.btnClear = Button(self.frame1)
        self.btnClear["text"]   = "C"
        self.btnClear["font"]   = self.fonte
        self.btnClear["width"]  = 4
        self.btnClear["height"] = 2
        self.btnClear["command"] = self.btnClearAction
        self.btnClear.pack(side=LEFT)
        
        self.btn7 = Button(self.frame2)
        self.btn7["text"]   = "7"
        self.btn7["font"]   = self.fonte
        self.btn7["width"]  = 4
        self.btn7["height"] = 2
        self.btn7["command"]=self.btn7Action
        self.btn7.pack(side=LEFT)
        
        self.btn8 = Button(self.frame2)
        self.btn8["text"]   = "8"
        self.btn8["font"]   = self.fonte
        self.btn8["width"]  = 4
        self.btn8["height"] = 2
        self.btn8["command"]=self.btn8Action
        self.btn8.pack(side=LEFT)
        
        self.btn9 = Button(self.frame2)
        self.btn9["text"]   = "9"
        self.btn9["font"]   = self.fonte
        self.btn9["width"]  = 4
        self.btn9["height"] = 2
        self.btn9["command"]=self.btn9Action
        self.btn9.pack(side=LEFT)
        
        self.btnDiv = Button(self.frame2)
        self.btnDiv["text"]   = "/"
        self.btnDiv["font"]   = self.fonte
        self.btnDiv["width"]  = 4
        self.btnDiv["height"] = 2
        self.btnDiv["command"]=self.btnDivAction
        self.btnDiv.pack(side=LEFT)
        
        self.btn6 = Button(self.frame3)
        self.btn6["text"]   = "6"
        self.btn6["font"]   = self.fonte
        self.btn6["width"]  = 4
        self.btn6["height"] = 2
        self.btn6["command"]=self.btn6Action
        self.btn6.pack(side=LEFT)
        
        self.btn5 = Button(self.frame3)
        self.btn5["text"]   = "5"
        self.btn5["font"]   = self.fonte
        self.btn5["width"]  = 4
        self.btn5["height"] = 2
        self.btn5["command"]=self.btn5Action
        self.btn5.pack(side=LEFT)
        
        self.btn4 = Button(self.frame3)
        self.btn4["text"]   = "4"
        self.btn4["font"]   = self.fonte
        self.btn4["width"]  = 4
        self.btn4["height"] = 2
        self.btn4["command"]=self.btn4Action
        self.btn4.pack(side=LEFT)
        
        self.btnMul = Button(self.frame3)
        self.btnMul["text"]   = "*"
        self.btnMul["font"]   = self.fonte
        self.btnMul["width"]  = 4
        self.btnMul["height"] = 2
        self.btnMul["command"]=self.btnMulAction
        self.btnMul.pack(side=LEFT)
        
        self.btn1 = Button(self.frame4)
        self.btn1["text"]   = "1"
        self.btn1["font"]   = self.fonte
        self.btn1["width"]  = 4
        self.btn1["height"] = 2
        self.btn1["command"]=self.btn1Action
        self.btn1.pack(side=LEFT)
        
        self.btn2 = Button(self.frame4)
        self.btn2["text"]   = "2"
        self.btn2["font"]   = self.fonte
        self.btn2["width"]  = 4
        self.btn2["height"] = 2
        self.btn2["command"]=self.btn2Action
        self.btn2.pack(side=LEFT)
        
        self.btn3 = Button(self.frame4)
        self.btn3["text"]   = "3"
        self.btn3["font"]   = self.fonte
        self.btn3["width"]  = 4
        self.btn3["height"] = 2
        self.btn3["command"]=self.btn3Action
        self.btn3.pack(side=LEFT)
        
        self.btnSub = Button(self.frame4)
        self.btnSub["text"]   = "-"
        self.btnSub["font"]   = self.fonte
        self.btnSub["width"]  = 4
        self.btnSub["height"] = 2
        self.btnSub["command"]=self.btnSubAction
        self.btnSub.pack(side=LEFT)
        
        self.btn0 = Button(self.frame5)
        self.btn0["text"]   = "0"
        self.btn0["font"]   = self.fonte
        self.btn0["width"]  = 4
        self.btn0["height"] = 2
        self.btn0["command"]=self.btn0Action
        self.btn0.pack(side=LEFT)
        
        self.btnPonto = Button(self.frame5)
        self.btnPonto["text"]   = "."
        self.btnPonto["font"]   = self.fonte
        self.btnPonto["width"]  = 4
        self.btnPonto["height"] = 2
        self.btnPonto["command"]=self.btnPontoAction
        self.btnPonto.pack(side=LEFT)
        
        self.btnIgual = Button(self.frame5)
        self.btnIgual["text"]   = "="
        self.btnIgual["font"]   = self.fonte
        self.btnIgual["width"]  = 4
        self.btnIgual["height"] = 2
        self.btnIgual["command"]=self.btnIgualAction
        self.btnIgual.pack(side=LEFT)
        
        self.btnAdd = Button(self.frame5)
        self.btnAdd["text"]   = "+"
        self.btnAdd["font"]   = self.fonte
        self.btnAdd["width"]  = 4
        self.btnAdd["height"] = 2
        self.btnAdd["command"]=self.btnAddAction
        self.btnAdd.pack(side=LEFT)
        
    def btnClearAction(self):
        self.entrada.set("")
        
    def btnBackAction(self):
        self.entrada.set((self.entry.get()[:-1]))
        
    def btnAbreParentesesAction(self):
        self.entrada.set(self.entry.get() + '(')
    
    def btnFechaParentesesAction(self):
        self.entrada.set(self.entry.get() + ')')

    def btn7Action(self):
        self.entrada.set(self.entry.get() + '7')
        
    def btn8Action(self):
        self.entrada.set(self.entry.get() + '8')
        
    def btn9Action(self):
        self.entrada.set(self.entry.get() + '9')
    
    def btnDivAction(self):
        self.entrada.set(self.entry.get() + '/')
    
    def btn6Action(self):
        self.entrada.set(self.entry.get() + '6')
        
    def btn5Action(self):
        self.entrada.set(self.entry.get() + '5')
    
    def btn4Action(self):
        self.entrada.set(self.entry.get() + '4')
        
    def btnMulAction(self):
        self.entrada.set(self.entry.get() + '*')
    
    def btn1Action(self):
        self.entrada.set(self.entry.get() + '1')
    
    def btn2Action(self):
        self.entrada.set(self.entry.get() + '2')
    
    def btn3Action(self):
        self.entrada.set(self.entry.get() + '3')
    
    def btnSubAction(self):
        self.entrada.set(self.entry.get() + '-')
    
    def btn0Action(self):
        self.entrada.set(self.entry.get() + '0')
    
    def btnPontoAction(self):
        self.entrada.set(self.entry.get() + '.')
        
    def btnIgualAction(self):
        calc = Calculadora()
        resultado = calc.calcular(self.entry.get())
        self.entrada.set(resultado)
    
    def btnAddAction(self):
        self.entrada.set(self.entry.get() + '+')
    
def show():
    tk = Tk()
    calc = FrameCalculadora(tk)
    tk.mainloop()