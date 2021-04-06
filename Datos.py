# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 13:25:00 2021

@author: Usuario
"""
import numpy as np

class Compound:
    def __init__(self, name, A, B, C):
        self.name= name
        self.A = A
        self.B = B
        self.C = C
    def elementos(self):
        return np.array([self.A,self.B,self.C]) 

CH3OH = Compound('Metanol',8.07240,1574.990,238.870)  
C2H5OH = Compound('Etanol', 8.21330,1652.050,231.480)
C6H6 = Compound('Benceno',6.90565,1211.033, 220.790)
C7H8 = Compound('Tolueno',6.95464, 1344.800, 219.482)
H2O= Compound('Agua', 8.140191,1810.94, 244.485)
C2H6O2 = Compound('Etilenglicol',8.79450, 2615.400, 244.910)
C4H4S = Compound('Tiofeno', 6.95926, 1246.020, 221.350)
C5H12 = Compound('Isopentano',6.83315, 1040.730, 235.445)
C4H8 = Compound('Cis 2-Buteno', 6.86926, 960.100, 237.000)
C4H10 = Compound('Butano',6.80896, 935.860, 238.730)


Met=CH3OH.elementos()
Eta=C2H5OH.elementos()
Ben=C6H6.elementos()
Tol=C7H8.elementos() 
Agu=H2O.elementos()
Eti=C2H6O2.elementos()
Tio=C4H4S.elementos()
Iso=C5H12.elementos()
Cis=C4H8.elementos()
But=C4H10.elementos()
     

