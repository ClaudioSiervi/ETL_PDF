# -*- coding: utf-8 -*-
"""
Created on Tue Aug 02 17:37:43 2016

@author: Claudio
"""

import re
import string
#from etl_pdf import Ferramentas
#from Mapeamento import DicionarioStrings



class ExtrairDados():
    
    # extrai dados de um objeto bs a partir da posição dos elementos da tag desejada
    def dados_objeto_bs(self, objeto_bs, tag, left_tx, top_tx):   
#        import re

        tag_encontrada = objeto_bs.find(tag, style=re.compile(r''+ left_tx+'.*?'+top_tx))             
        conteudo_tag = tag_encontrada.contents          
        
        texto_extraido_unicode =''
        tam = len(conteudo_tag)
        for item in xrange(0, tam):
            # extrai o texto do objeto conteudo_tag
            texto_extraido_unicode = texto_extraido_unicode + ';' .join(conteudo_tag[item].stripped_strings)
            texto_extraido_unicode = texto_extraido_unicode + ';'
        
        texto_extraido_str = string.split(texto_extraido_unicode.encode('utf-8'), ';')
        
#        print texto_extraido_str
              
        return texto_extraido_str


############################################################################
     # Página 1
class BalancoEnergeticoResumido():


     # Extrai a data do arquivo do IPDO
    def extrair_data_arquivo_ipdo(self, objeto_bs, tag, top_tx):
    
        tag_encontrada = objeto_bs.find('div', style=re.compile(r''+top_tx))
        conteudo_tag = tag_encontrada.contents
        
        texto_extraido_unicode = ' ' .join(conteudo_tag[0].stripped_strings)
        texto_extraido_str = texto_extraido_unicode.encode('utf-8')
        texto_extraido_str = string.split(texto_extraido_str, ',')
        texto_extraido_str = texto_extraido_str[1]    # Data do IPDO       

        return texto_extraido_str
        
        
    # Extrai os dados do resumo do Balanço de Energia (programado e verificado)
    def extrair_dados_sistema(self, objeto_bs, tag, left_tx, top_tx):        
    
        extrair = ExtrairDados()
        texto_extraido_str = extrair.dados_objeto_bs(objeto_bs, tag, left_tx, top_tx)
        
        return texto_extraido_str

        
############################################################################
    # Página 2
class BalancoEnergeticoDetalhado():
    
    def fontes_energeticas(self, objeto_bs, tag, left_tx, top_tx):    
    # objeto_bs-> objeto beautifulSoup, tag='div', tag_positions -> (top_tx,left_tx)
    
        extrair = ExtrairDados()
        
        fontes_lista = extrair.dados_objeto_bs(objeto_bs, tag, left_tx, top_tx)      
        
        fontes_json ={}

        subsistemas = ['Sudeste', 'Sul', 'Nordeste', 'Norte']        
        #   tratamento de strings    
        posicao = 1
        for item in list(fontes_lista):
            
            if item in subsistemas:      
                fontes_lista.remove(item)
                continue
            
            elif((item == 'Produção (MWmed/dia)') or (item == '')):
                fontes_lista.remove(item)
                continue
            
            elif (item == 'Termo (**)'):
                fontes_lista.remove(item)
                item = 'Termo'
                fontes_lista.insert(posicao, item)
                fontes_json[item] = ""
                continue
            
            posicao += 1
            fontes_json[item] = ""

        fontes_lista_ordenada =[]
        fontes_relatorio = ["Hidro","Termo","Nuclear","Eólica","Solar","Total"]
        
        for fonte_in in fontes_relatorio:
            for fonte in fontes_json:
                if (fonte == fonte_in):
                    fontes_lista_ordenada.append(fonte_in)
            

        return fontes_lista_ordenada, fontes_json   
    
    
    # Produção de energia programada e verificada por subsistema
    def producao(self, objeto_bs, tag, left_tx, top_tx):
        
        extrair = ExtrairDados()
        texto_extraido_str = extrair.dados_objeto_bs(objeto_bs, tag, left_tx, top_tx)
        
        dim = len(texto_extraido_str)
        producao_extraida = texto_extraido_str[0:(dim-1)]  # retira [dim]=''
        
        return producao_extraida
        
        
    # Carga demandada por subsistema    
    def carga(self, objeto_bs, tag, left_tx, top_tx):
        
        extrair = ExtrairDados()
        texto_extraido_str = extrair.dados_objeto_bs(objeto_bs, tag, left_tx, top_tx)
        
        dim = len(texto_extraido_str)
        carga_extraida = texto_extraido_str[0:(dim-1)]  # retira [dim]=''
        
        return carga_extraida

    
    # Energia Natural Afluente
    def ena(self, objeto_bs, tag, left_tx, top_tx):
        
        extrair = ExtrairDados()
        texto_extraido_str = extrair.dados_objeto_bs(objeto_bs, tag, left_tx, top_tx)
        
        dim = len(texto_extraido_str)
        ena_extraida = texto_extraido_str[0:(dim-1)]  # retira [dim]=''
        
        return ena_extraida
        
    ## varrer a lista de dados para encontrar o valor ear
    # Energia Armazenada nos Reservatórios
    def energia_armazenada_reservatorio(self, objeto_bs, tag, left_tx, top_tx):
        
        extrair = ExtrairDados()
        texto_extraido_str = extrair.dados_objeto_bs(objeto_bs, tag, left_tx, top_tx)
        
        print texto_extraido_str
        ear_extraida = texto_extraido_str[0]
        
        return ear_extraida