# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 18:49:11 2021

@author: Usuario
"""

import tkinter as tk 
import sys
sys.path.insert(1,Datos.py)
import Datos as cl 
import math as mt
import numpy as np
import matplotlib.pyplot as plt
root= tk.Tk()
root.title("Diagramas Txy")
def Tb(A,B,C,P):
        return (B/(A-mt.log10(P)))-C
  
def fases(A):  
        if CheckVar1.get()==1:
            Va1=cl.Met
            Va2=cl.Eta
            Vn1=cl.CH3OH.name
            Vn2=cl.C2H5OH.name
        elif CheckVar2.get()==1:
            Va1=cl.Ben
            Va2=cl.Tol
            Vn1=cl.C6H6.name
            Vn2=cl.C7H8.name
        elif CheckVar3.get()==1:
            Va1=cl.Agu
            Va2=cl.Eti
            Vn1=cl.H2O.name
            Vn2=cl.C2H6O2.name
        elif CheckVar4.get()==1:
            Va1=cl.Tio
            Va2=cl.Iso
            Vn1=cl.C4H4S.name
            Vn2=cl.C5H12.name
        else:
            Va1=cl.Cis
            Va2=cl.But
            Vn1=cl.C4H8.name
            Vn2=cl.C4H10.name
            ()
        P=float(A)
        V1=str(Vn1)
        V2=str(Vn2)
        A=np.array([Va1[0],Va2[0]])
        B=np.array([Va1[1],Va2[1]])
        C=np.array([Va1[2],Va2[2]])
        T=[]
        X=[1,]
        Y=[1,]
        for i in (0,1):
            T.append(Tb(A[i],B[i],C[i],P))
        T=np.linspace(T[0],T[1],50)
        for i in range(1,49):
            K1=10**(A[0]-(B[0]/(T[i]+C[0])))/P
            K2=10**(A[1]-(B[1]/(T[i]+C[1])))/P
            X.insert(i,((1-K2)/(K1-K2)))
            Y.insert(i,(K1*((1-K2)/(K1-K2))))
        X.append(0)
        Y.append(0)
        plt.xlim(0,1)
        plt.plot(X,T)
        plt.plot(Y,T)
        plt.xlabel('X' +' ' + V1)
        plt.ylabel('Temp(°C)')
        plt.title('Sistema'+' '+V1+'/'+V2)
        plt.legend(["Liquid Phase","Vapor Phase"])
        plt.show()
    

HEIGHT=700
WIDHT=800

canvas = tk.Canvas(root,height=HEIGHT,width=WIDHT)
canvas.pack()
frame= tk.Frame(root, bg='pink')
frame.place(relx=0.1, rely=0.1, relwidth=0.8,relheight=0.8)
frame= tk.Frame( )
A=tk.Entry(font=('Modern',15))
Pres= tk.Text(root,font=('Modern',15))
Pres.insert(1.0, "Inserte la Presión del Sistema en mmHg")
Pres.configure(state='disabled')
Sis= tk.Text(root,font=('Modern',15))
Sis.insert(1.0, "Seleccione un Sistema")
Sis.configure(state='disabled')
Button= tk.Button(root,text='Calcular',font=('Modern',15),command=(lambda: fases(A.get())))
CheckVar1 = tk.IntVar(root)
CheckVar2 = tk.IntVar(root)
CheckVar3 = tk.IntVar(root)
CheckVar4 = tk.IntVar(root)
CheckVar5 = tk.IntVar(root)
C1 = tk.Checkbutton(root,text = 'Metanol-Etanol',font=('Modern',15),variable = CheckVar1,onvalue = 1, offvalue = 0, height=5,width = 20)
C2 = tk.Checkbutton(root,text = "Benceno-Tolueno",font=('Modern',15),variable = CheckVar2,onvalue = 1, offvalue = 0, height=5,width = 20)
C3 = tk.Checkbutton(root,text = "Agua-Etilenglicol",font=('Modern',15),variable = CheckVar3,onvalue = 1, offvalue = 0, height=5,width = 20)
C4 = tk.Checkbutton(root,text = "Tiofeno-Isopentano",font=('Modern',15),variable = CheckVar4,onvalue = 1, offvalue = 0, height=5,width = 20)
C5 = tk.Checkbutton(root,text = "Cis 2Buteno-Butano",font=('Modern',15),variable = CheckVar5,onvalue = 1, offvalue = 0, height=5,width = 20)
Pres.place(relx=0.15,rely=0.125, relwidth=0.5, relheight=0.05)
Sis.place(relx=0.35,rely=0.2, relwidth=0.28, relheight=0.05)
C1.place(relx=0.15,rely=0.3, relwidth=0.3, relheight=0.05)
C2.place(relx=0.55,rely=0.3, relwidth=0.3, relheight=0.05)
C3.place(relx=0.15,rely=0.5, relwidth=0.3, relheight=0.05)
C4.place(relx=0.55,rely=0.5, relwidth=0.3, relheight=0.05)
C5.place(relx=0.35,rely=0.65, relwidth=0.3, relheight=0.05)
A.place(relx=0.70,rely=0.125,relwidth=0.1,relheight=0.05)
Button.place(relx=0.44, rely=0.78,relwidth=0.12,relheight=0.05)
root.mainloop()
