# -*- coding: utf-8 -*-
"""
Created on Tue Aug 02 17:37:43 2016

@author: Claudio
"""

import re
import string
from Utilitarios import Ferramentas
from ExpressoesRegulares import DicionarioRegEx, DicionarioStrings
#from etl_pdf import Ferramentas
#from Mapeamento import DicionarioStrings



class ExtrairDados():
    
    # extrai dados de um objeto bs a partir da posição dos elementos da tag desejada
    def dados_objeto_bs(self, objeto_bs, tag, left_tx, top_tx):   
#        import re

        tag_encontrada = objeto_bs.find(tag, style=re.compile(r''+ left_tx+'.*?'+top_tx))             
#        print "tag"
#        print tag_encontrada
        
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
    
    
    # Energia Itaipu    
    def energia_itaipu(self, objeto_bs, tag, left_tx, top_tx):
        
        extrair = ExtrairDados()
        texto_extraido_str = extrair.dados_objeto_bs(objeto_bs, tag, left_tx, top_tx)
        
        print texto_extraido_str
        
        dim = len(texto_extraido_str)
        energia_extraida = texto_extraido_str[0:(dim-1)]  # retira [dim]=''
        
        print energia_extraida
        return energia_extraida
        
    
    # Energia Natural Afluente
    def energia_narutal_afluente(self, objeto_bs, tag, left_tx, top_tx):
        
        extrair = ExtrairDados()
        texto_extraido_str = extrair.dados_objeto_bs(objeto_bs, tag, left_tx, top_tx)
        
        dim = len(texto_extraido_str)
        ena_extraida = texto_extraido_str[0:(dim-1)]  # retira [dim]=''
        
        return ena_extraida
        
        
        
    ## varrer a lista de dados para encontrar o valor ear
    # Energia Armazenada nos Reservatórios
    def energia_armazenada_reservatorio(self, objeto_bs, sub):
#    def energia_armazenada_reservatorio(self, objeto_bs, tag, left_tx, top_tx):    
        
        tag = 'div'        
        dicionario_expressoes = DicionarioRegEx()  
#        dicionario_strings = DicionarioStrings()
        
#        subsistemas = dicionario_strings.subsistemas
        
        sistema_interligado = dicionario_expressoes.sistema_interligado
        
        extrair = ExtrairDados()
        
        ferramenta = Ferramentas()
        
        ear_extraida = {}
        
#        for sub in subsistemas:
        texto_extraido_str = \
                    extrair.dados_objeto_bs(objeto_bs, tag, 
                                sistema_interligado[sub]['ear_lf'], 
                                sistema_interligado[sub]['ear_tp']
                        )
                        
        ear_extraida = {'verificada' : texto_extraido_str[0].replace('.','')}
        print "ear_extraida 1"
        print ear_extraida
        
        eh_numerico = ferramenta.eh_numerico("subsistema", "ear", ear_extraida['verificada'])
        
        if not eh_numerico:
#                print sub
            texto_extraido_str = \
                    extrair.dados_objeto_bs(objeto_bs, tag, 
                                sistema_interligado[sub]['ear1_lf'], 
                                sistema_interligado[sub]['ear1_tp']
                        )
            
            ear_extraida = {'verificada' : texto_extraido_str[0].replace('.','')}
            
            print "ear_extraida 2"
            print ear_extraida
            eh_numerico = ferramenta.eh_numerico("subsistema", "ear", ear_extraida['verificada'])
        
#        print ear_extraida
        return ear_extraida
        
        
        
        
        
    # Intercambio de Energia entre subsistemas   
    def intercambio_entre_subsistemas(self, objeto_bs, tag, left_tx, top_tx):
        
        extrair = ExtrairDados()
        
        texto_extraido_str = extrair.dados_objeto_bs(objeto_bs, tag, left_tx, top_tx)
        
        print "intercambio_extraido"                                       
        print texto_extraido_str 
        intercambio_extraido = texto_extraido_str[0:2]

        return intercambio_extraido

############################################################################
    # Página 3
class VariacaoEnergiaArmazenada():
    
    # Energia Armazenada Máxima
    def capacidade_maxima(self, objeto_bs, tag, left_tx, top_tx):
        
        extrair = ExtrairDados()
        texto_extraido_str = extrair.dados_objeto_bs(objeto_bs, tag, left_tx, top_tx)
        

        dim = len(texto_extraido_str)
        capacidade_maxima_extraida = texto_extraido_str[0:(dim-1)]  # retira [dim]=''
        
        return capacidade_maxima_extraida

    
## TODO implementar extração
############################################################################
    # Página 14
class DemandasMaximas():
    
    # Demanda Máxima instantânea 
    def demanda_instantanea_por_subsistema(self, objeto_bs, tag, left_tx, top_tx):
        
        extrair = ExtrairDados()
        
        texto_extraido_str = extrair.dados_objeto_bs(objeto_bs, tag, left_tx, top_tx)
        
        print texto_extraido_str
    
        if len(texto_extraido_str) == 2:
            texto_extraido_lista = string.split(texto_extraido_str[0], ' ')
                
        elif len(texto_extraido_str) == 3:
            texto_extraido_lista = string.split(texto_extraido_str[1], ' ')
        
        print texto_extraido_lista
        
        if len(texto_extraido_lista) == 4:
            demanda, data = [texto_extraido_lista[0], texto_extraido_lista[3]]
        
        elif len(texto_extraido_lista) == 5:
            demanda, data = [texto_extraido_lista[0], texto_extraido_lista[4]]
            
#        demanda, data = [texto_extraido_lista[0], texto_extraido_lista[3]]
        
        print demanda + '    ' + data
        return demanda, data