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
        from DicionarioTexto import Texto
        
        self.dados = ExtraiTextoBalancoEnergia()    
            
        objeto_bs = BeautifulSoup(html_extraido, 'html.parser')
        
        texto = Texto()
        print texto.data_ipdo_top
        self.data_arquivo = self.dados.data_arquivo_entrada(objeto_bs, 'div', texto.data_ipdo_top)
        
#        print self.data_arquivo
        salva = ImprimeArquivosTexto()
        salva.data_em_xlsx(self.data_arquivo)
      
      
    def resumo_balanco_energia(self, html_extraido):
        from DicionarioTexto import Texto
        
        self.dados = ExtraiTextoBalancoEnergia()    
        
        objeto_bs = BeautifulSoup(html_extraido, 'html.parser')
        
#        left_tx = 'left:28[0-5]px'
#        top_tx = 'top:31[0-8]px'
        texto = Texto()
        self.programado = self.dados.sistema_interligado(objeto_bs, 'div',texto.balanco_energ_programado_left , texto.balanco_energ_programado_top)        
        self.verificado =  self.dados.sistema_interligado(objeto_bs, 'div', texto.balanco_energ_verificado_left, texto.balanco_energ_verificado_top) 
#        self.percental_rel_sistema =  self.dados.sistema_interligado(objeto_bs, 'div', '459', '314') 
        
        salva = ImprimeArquivosTexto()
        salva.texto_em_xlsx([self.programado, self.verificado])
        #, self.percental_rel_sistema])
#        return self.programado, self.verificado, self.percental_rel_sistema