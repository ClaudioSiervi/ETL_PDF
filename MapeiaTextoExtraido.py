# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 23:53:44 2016

@author: Claudio
"""


from EstruturaDados import SistemaInterligadoNacional
from DicionarioDados import Dicionario
from bs4 import BeautifulSoup
import re

sin = SistemaInterligadoNacional()
dic = Dicionario()



class MapeiaTexto():
      
        
        
    #def __init__(self, html_extraido, tag, left_num, top_num):
        #self.producao_energia =sin.producao_energia.quantidade.programada
    
    def resumo_balanco_energia(self, texto_extraido):
        
        html_extraido = BeautifulSoup(texto_extraido, 'html.parser')
                                # dados_tabela1(self, html_extraido, tag, left_num, top_num):
        programado = self.dados_extraidos_sistema_interligado(html_extraido, 'div', '284', '314')
        verificado = self.dados_extraidos_sistema_interligado(html_extraido, 'div', '377', '314') 
        percental_rel_sistema = self.dados_extraidos_sistema_interligado(html_extraido, 'div', '459', '314') 
        
        return programado, verificado, percental_rel_sistema
        
        
    # Extrai os dados da operação diária programada e verificada das 
        #tags html do Balanço de Energia
    def dados_extraidos_sistema_interligado(self, html_extraido, tag, left_num, top_num):        
        #tag ='div'
        left = 'left:' + left_num + 'px' #'284px'
        top =  'top:' +  top_num + 'px'  #314px'
        
        tag_encontrada = html_extraido.find(tag, style=re.compile(r''+ left+'.*?'+top))
        conteudo_tag = tag_encontrada.contents
        dados =''
        tam = len(conteudo_tag)
        for item in xrange(0, tam):
            dados = dados + ' ' .join(conteudo_tag[item].stripped_strings)
            dados = dados + ' '
        
        result_str = dados.encode('utf-8')
        print result_str
        
        return result_str        
        #        sin.producao_energia.quantidade.verificada = 11
#        sin.intercambio_inter.total.programada = 1
#        sin.intercambio_inter.total.programada = 3 
#        
#        sin.intercambio_inter.exportacao.fonte = dic.ar
#        sin.intercambio_inter.exportacao.quantidade.programada = 10
#        sin.intercambio_inter.exportacao.quantidade.verificada = 9
