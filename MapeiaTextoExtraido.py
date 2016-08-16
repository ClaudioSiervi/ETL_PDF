# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 23:53:44 2016

@author: Claudio
"""


from bs4 import BeautifulSoup
from ExtracaoTexto import BalancoEnergia, Subsistemas       
from ImprimeResultados import ImprimeArquivosTexto 
from DicionarioTexto import DicionarioRegEx

class MapeiaTexto():
    
    def data_relatorio(self, html_extraido):
        
        objeto_bs = BeautifulSoup(html_extraido, 'html.parser')
        
        dados = BalancoEnergia()    
        dic = DicionarioRegEx()
        self.data_arquivo = dados.data_arquivo_entrada(objeto_bs, 'div', dic.geral['data_ipdo_tp'])
        
        print self.data_arquivo 
        
        ##TODO: Organizar impressões sequencialmente em um arquivo único
        salva = ImprimeArquivosTexto()
        salva.data_em_xlsx(self.data_arquivo)
      
      
      
    # Dados da página 1 
    def resumo_balanco_energia(self, html_extraido):

        objeto_bs = BeautifulSoup(html_extraido, 'html.parser')
        
        dados = BalancoEnergia()
        dic = DicionarioRegEx()
        self.programado = dados.sistema_interligado(objeto_bs, 'div', dic.balanco['programado_lf'] , dic.balanco['programado_tp'])        
        self.verificado = dados.sistema_interligado(objeto_bs, 'div', dic.balanco['verificado_lf'], dic.balanco['verificado_tp']) 
#        self.percental_rel_sistema =  self.dados.sistema_interligado(objeto_bs, 'div', '459', '314')    
        
        ##TODO --> Organizar impressões sequencialmente em um arquivo único
        salva = ImprimeArquivosTexto()
        salva.texto_em_xlsx([self.programado, self.verificado])
#        return self.programado, self.verificado, self.percental_rel_sistema
        
        
        
    def balanco_por_subsistema(self, html_extraido):
        
        objeto_bs = BeautifulSoup(html_extraido, 'html.parser')
        
        dados = Subsistemas()    
        dic = DicionarioRegEx()
        self.data_arquivo = dados.data_arquivo_entrada(objeto_bs, 'div', dic.geral['data_ipdo_tp'])