# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 23:46:00 2016

@author: Claudio
"""

# Dicionário de dados do arquivo IPDO disponibilizado pelo ONS
class Dicionario():
    

    
      #Fontes --> carga, ghidro, gtermo, geolica, gsolar        
    def fontes(self):
        self.carga = "Carga"
        self.ghidro = "Geração Hidrelétrica"
        self.gtermo = "Geração Termelétrica"
        self.geolica = "Geração Eólica"
        self.gsolar = "Geração Solar"
        return
    
    def fontes_acronimos(self):
        self.carga = "Carga"
        self.ghidro = "GH"
        self.gtermo = "GT"
        self.geolica = "GE"
        self.gsolar = "GS"
        return
        
    def fontes_intercambio_inter(self):
        self.pa = "Paraguai Acaray"
        self.ur = "Uruguai Rivera"
        self.me = "Melo"
        self.ar = "Argentina"
        self.g1 = "Garabi I"
        self.g2 = "Garabi II"
        self.ug = "Uruguaiana"
        return
        
        
    def __init__(self):
        self.fontes = self.fontes()
        self.fontes_acronimos = self.fontes_acronimos()
        return                
                


## Troca de energia entre os subsistemas
#class Intercambio:
#    N_IMP = 0
#    IMP_NE = 0
#    SE_IMP = 0
#    NE_SE = 0
#    S_SE = 0
#    S_Export = 0