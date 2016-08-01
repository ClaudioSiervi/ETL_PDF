# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 11:19:49 2016

@author: Claudio
"""

# Modelagem dos dados do Informativo Preliminar Diário da Operação (IPDO)
#
# Data de Ocorrencia dos Dados     
class Data():
    import datetime
    mylist = []
    today = datetime.date.today()
    mylist.append(today)
#    print mylist[0] # imprime o objeto data, não o container


class Quantidade:
    # Quantidades de diversas medidas apresentadas no IPDO
    def __init__(self):
        self.programada = 0
        self.verificada = 0
        return
        
    

class Energia:
    # Energia Estimada e Verificada por Fonte 
    def __init__(self):
        self.fonte = ''
        self.quantidade = Quantidade()
        self.participacao_relacao_sin = 0
        return
       

class IntercambioInternacional():
    # Intercambio Discretizado
    def __init__(self):
        self.discretizado = IntercambioInternacionalDiscretizado()
        self.total = Quantidade()
        return
        
class IntercambioInternacionalDiscretizado():
     def __init__(self):
        self.importacao = Energia()
        self.exportacao = Energia()
        return
    
    
    
class Subsistema():
    
    def __init__(self):
#        self.nome = nome
#        self.carga = carga
#        self.ghidro = ghidro
#        self.gtermo = gtermo
#        self.geolica = geolica
#        self.gsolar = gsolar
        return
    

class SistemaInterligadoNacional():
    
    def __init__(self,):
        self.data = 0
        self.producao_energia = Energia()
        self.carga = Quantidade()
        self.intercambio_inter = IntercambioInternacional()
        self.subsistema = Subsistema()
        return


#    data = Data()   
#    producao = Energia()
#    intercambio_inter = IntercambioInternacional()
#    
#    
#    
#    producao.quantidade.programada
#    intercambio_inter.exportacao.programada = 100
#    
#    
#    norte = subsistema(nome, 5044, [3546, 1884])
     
    
    
    # Trabalhancom com classes  
# http://pythonclub.com.br/introducao-classes-metodos-python-basico.html   
# https://docs.python.org/3/tutorial/classes.html
    
    
    
    
    
    
    
    
    
    
    
    
    
    

