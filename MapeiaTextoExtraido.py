# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 23:53:44 2016

@author: Claudio
"""


from EstruturaDados import SistemaInterligadoNacional
from DicionarioDados import Dicionario

    

sin = SistemaInterligadoNacional()
dic = Dicionario()

class MapeiaTexto():
      
    def __init__(self):
        self.balanco_energia = BalancoEnergia()
      
      
class BalancoEnergia():
        
    def __init__(self):
        self.producao_energia =sin.producao_energia.quantidade.programada
#        sin.producao_energia.quantidade.verificada = 11
#        sin.intercambio_inter.total.programada = 1
#        sin.intercambio_inter.total.programada = 3 
#        
#        sin.intercambio_inter.exportacao.fonte = dic.ar
#        sin.intercambio_inter.exportacao.quantidade.programada = 10
#        sin.intercambio_inter.exportacao.quantidade.verificada = 9
        
