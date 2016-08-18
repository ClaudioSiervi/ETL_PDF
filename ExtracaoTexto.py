# -*- coding: utf-8 -*-
"""
Created on Tue Aug 02 17:37:43 2016

@author: Claudio
"""

import re
import string
from etl_pdf import ExtrairTransformarCarregar
#from bs4 import BeautifulSoup
    
    # Página 1
class BalancoEnergia():

     # Extrai a data do arquivo do IPDO
    def data_arquivo_entrada(self, objeto_bs, tag, top_tx):
    # objeto_bs --> objeto beautifulsoup
    # tag       --> tag html buscada
    # top_tx    --> coordenadas do top
    
        tag_encontrada = objeto_bs.find('div', style=re.compile(r''+top_tx))
        conteudo_tag = tag_encontrada.contents
        
        texto_extraido_unicode = ' ' .join(conteudo_tag[0].stripped_strings)
        texto_extraido_str = texto_extraido_unicode.encode('utf-8')
        texto_extraido_str = string.split(texto_extraido_str, ',')
        texto_extraido_str = texto_extraido_str[1]    # Data do IPDO       

        return texto_extraido_str
        
        
    # Extrai os dados do resumo do Balanço de Energia (programado e verificado)
    def resumo_sin(self, objeto_bs, tag, left_tx, top_tx):        
    # objeto_bs --> objeto beautifulsoup
    # tag       --> tag html buscada
    # top_tx    --> coordenadas do top
    
        extrair = ExtrairTransformarCarregar()
        texto_extraido_str = extrair.dados_objeto_bs(objeto_bs, tag, left_tx, top_tx)
        
        return texto_extraido_str
        
        
############################################################################

    # Página 2
class Subsistemas():
    
    
    def fontes(self, objeto_bs, tag, left_tx, top_tx):        
    # objeto_bs --> objeto beautifulsoup
    # tag       --> tag html buscada
    # top_tx    --> coordenadas do top
    
        extrair = ExtrairTransformarCarregar()
        texto_extraido_str = extrair.dados_objeto_bs(objeto_bs, tag, left_tx, top_tx)
        
        texto_extraido_str = string.split(texto_extraido_str, ';')
        
        dim = len(texto_extraido_str)
        fontes_extraidas = texto_extraido_str[1:(dim-2)]  # retira [0]=Produção(MWmed/dia), [dim-1]='Total', [dim]=''        
        
        print 'fontes' 
        print fontes_extraidas
        return fontes_extraidas
    
    
    def producao(self, objeto_bs, tag, left_tx, top_tx):
        
        extrair = ExtrairTransformarCarregar()
        texto_extraido_str = extrair.dados_objeto_bs(objeto_bs, tag, left_tx, top_tx)
        
        texto_extraido_str = string.split(texto_extraido_str, ';')
        
        dim = len(texto_extraido_str)
        producao_extraida = texto_extraido_str[0:(dim-1)]  # retira [dim]=''
        
        return producao_extraida
        
        
    def carga(self, objeto_bs, tag, left_tx, top_tx):
        
        extrair = ExtrairTransformarCarregar()
        texto_extraido_str = extrair.dados_objeto_bs(objeto_bs, tag, left_tx, top_tx)
        
        texto_extraido_str = string.split(texto_extraido_str, ';')
        
        dim = len(texto_extraido_str)
        carga_extraida = texto_extraido_str[0:(dim-1)]  # retira [dim]=''
        
        return carga_extraida

    
    # Energia Natural Afluente
    def ena(self, objeto_bs, tag, left_tx, top_tx):
        
        extrair = ExtrairTransformarCarregar()
        texto_extraido_str = extrair.dados_objeto_bs(objeto_bs, tag, left_tx, top_tx)
        
        texto_extraido_str = string.split(texto_extraido_str, ';')
        
        dim = len(texto_extraido_str)
        ena_extraida = texto_extraido_str[0:(dim-1)]  # retira [dim]=''
        
        return ena_extraida
        
    
    # Energia Armazenada nos Reservatórios
    def ear(self, objeto_bs, tag, left_tx, top_tx):
        
        extrair = ExtrairTransformarCarregar()
        texto_extraido_str = extrair.dados_objeto_bs(objeto_bs, tag, left_tx, top_tx)
        
        texto_extraido_str = string.split(texto_extraido_str, ';')
        
        ear_extraida = texto_extraido_str[0:1]
        
        return ear_extraida