# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 23:53:44 2016

@author: Claudio
"""


from EstruturaDados import SistemaInterligadoNacional
from DicionarioDados import Dicionario
from bs4 import BeautifulSoup


sin = SistemaInterligadoNacional()
dic = Dicionario()



class MapeiaTexto():
      
    def resumo_balanco_energia(self, html_extraido):
        
        from ExtracaoTexto import ExtraiTextoBalancoEnergia        
        
        self.dados = ExtraiTextoBalancoEnergia()    
        
        objeto_bs = BeautifulSoup(html_extraido, 'html.parser')
        
        self.programado = self.dados.sistema_interligado(objeto_bs, 'div', '284', '314')        
        self.verificado =  self.dados.sistema_interligado(objeto_bs, 'div', '377', '314') 
        self.percental_rel_sistema =  self.dados.sistema_interligado(objeto_bs, 'div', '459', '314') 
        
        from ImprimeResultados import ImprimeArquivosTexto   
        
        salva = ImprimeArquivosTexto()
        salva.texto_em_xlsx([self.programado, self.verificado, self.percental_rel_sistema])
    
    
        return self.programado, self.verificado, self.percental_rel_sistema
       
