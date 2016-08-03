# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 23:53:44 2016

@author: Claudio
"""


from bs4 import BeautifulSoup
from ExtracaoTexto import ExtraiTextoBalancoEnergia        
from ImprimeResultados import ImprimeArquivosTexto 

class MapeiaTexto():
      
    def data_relatorio(self, html_extraido):
        
        self.dados = ExtraiTextoBalancoEnergia()    
            
        objeto_bs = BeautifulSoup(html_extraido, 'html.parser')
        
        self.data_arquivo = self.dados.data_arquivo_entrada(objeto_bs, 'div', '189')
        
#        print self.data_arquivo
        salva = ImprimeArquivosTexto()
        salva.data_em_xlsx(self.data_arquivo)
      
      
    def resumo_balanco_energia(self, html_extraido):
                
        self.dados = ExtraiTextoBalancoEnergia()    
        
        objeto_bs = BeautifulSoup(html_extraido, 'html.parser')
        
        self.programado = self.dados.sistema_interligado(objeto_bs, 'div', '284', '314')        
        self.verificado =  self.dados.sistema_interligado(objeto_bs, 'div', '377', '314') 
        self.percental_rel_sistema =  self.dados.sistema_interligado(objeto_bs, 'div', '459', '314') 
        
        salva = ImprimeArquivosTexto()
        salva.texto_em_xlsx([self.programado, self.verificado, self.percental_rel_sistema])
    
#        return self.programado, self.verificado, self.percental_rel_sistema
       
