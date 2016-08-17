# -*- coding: utf-8 -*-
"""
Created on Tue Aug 02 17:37:43 2016

@author: Claudio
"""

import re
import string
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
    
        tag_encontrada = objeto_bs.find(tag, style=re.compile(r''+ left_tx+'.*?'+top_tx))
        conteudo_tag = tag_encontrada.contents
        texto_extraido_unicode =''
        tam = len(conteudo_tag)
        for item in xrange(0, tam):
            texto_extraido_unicode = texto_extraido_unicode + ';' .join(conteudo_tag[item].stripped_strings)
            texto_extraido_unicode = texto_extraido_unicode + ';'
        
        texto_extraido_str = texto_extraido_unicode.encode('utf-8')
        
#        print texto_extraido_str
        return texto_extraido_str       


    # Página 2
class Subsistemas():
    
    def fontes(self, objeto_bs, tag, left_tx, top_tx):        
    # objeto_bs --> objeto beautifulsoup
    # tag       --> tag html buscada
    # top_tx    --> coordenadas do top
    
        tag_encontrada = objeto_bs.find(tag, style=re.compile(r''+ left_tx+'.*?'+top_tx))
        conteudo_tag = tag_encontrada.contents
        texto_extraido_unicode =''
        tam = len(conteudo_tag)
        for item in xrange(0, tam):
            texto_extraido_unicode = texto_extraido_unicode + ';' .join(conteudo_tag[item].stripped_strings)
            texto_extraido_unicode = texto_extraido_unicode + ';'
        
        texto_extraido_str = texto_extraido_unicode.encode('utf-8')
        
        dim = len(texto_extraido_str)
        # retira [0]=Produção(MWmed/dia), [dim-1]='Total', [dim]='' 
        self.fontes = texto_extraido_str[1:(dim-2)]       
        
        print 'fontes' 
        print texto_extraido_str
        return texto_extraido_str
        