# -*- coding: utf-8 -*-
"""
Created on Tue Aug 02 19:20:17 2016

@author: Claudio
"""
from openpyxl import load_workbook
#from Arquivo import ArquivoIPDO
from Utilitarios import Ferramentas
#from openpyxl import Workbook
import string

class ImprimeArquivosTexto():
    
    
    
    def texto_em_txt(self, texto, nome_arquivo_saida):
    # Salva o texto extraído do pdf em um arquivo texto
        self.arquivo_texto = open(nome_arquivo_saida, "w")
        self.status_escrita = self.arquivo_texto.write(texto)
        self.arquivo_texto.close()
        
        
    def texto_em_html(self, texto, nome_arquivo_saida):
    # Salva o texto extraído do pdf em um arquivo texto
        arquivo_texto = open(nome_arquivo_saida, "w")
        self.status_escrita = arquivo_texto.write(texto)
        arquivo_texto.close()
        

    # Imprime o resumo do balanço energético    
    def balanco_energia_resumido_em_xlsx(self, geral, balanco_detalhado):
        
        
#        try:
        wb = load_workbook('IPDO.xlsx') 
        ws = wb['Tabela1']
        
        ferramenta = Ferramentas()
        [primeira_linha, ultima_linha] = ferramenta.linha_nao_vazia(ws)
        ultima_linha = ultima_linha + 1        
        
        indice = 'A'+str(ultima_linha)            
        ws[indice] = geral["data_arquivo"]
        
        num_elementos_pg = len(balanco_detalhado["programada"]) # Número de elementos do resumo
        conta_valores = 0
        
        for conta_coluna_pg in xrange(1, num_elementos_pg):
            letra = ferramenta.retorna_letra_da_coluna(conta_coluna_pg + 1)
            indice = letra + str(ultima_linha)            
            ws[indice] = balanco_detalhado["programada"][conta_valores]       
            conta_valores = conta_valores + 1
        
        num_elementos_vf = len(balanco_detalhado["verificada"]) + conta_coluna_pg
        conta_valores = 0       
        
        for conta_coluna_vf in xrange(conta_coluna_pg, num_elementos_vf):
            letra = ferramenta.retorna_letra_da_coluna(conta_coluna_vf + 2)
            indice = letra + str(ultima_linha)            
            ws[indice] = balanco_detalhado["verificada"][conta_valores]
            conta_valores = conta_valores + 1                
        
        wb.save('IPDO.xlsx')   # sobrescreve resultados
 
#        except:
#            print '------------------------------------------------------------'
#            print 'ERRO: Não foi possível salvar os resultados na planilha.xlsx'               
        
        
        
    @classmethod
    def balanco_energia_detalhado_em_xlsx(self):
        
        from Arquivo import Arquivo_IPDO        
        arquivo_ipdo = Arquivo_IPDO()
        
        sudeste = arquivo_ipdo('sudeste').carga_vf
        subsistema.producao_pg = sudeste[3]
        subsistema.producao_vf = sudeste[4]        
        subsistema.carga_vf = sudeste[5]     
        subsistema.carga_pg = sudeste[6]
        subsistema.energia_natural_afluente = sudeste[7]
        subsistema.energia_armazenada_reservatorio = sudeste[8]
        
        
        wb = load_workbook('IPDO.xlsx')
        ws = wb['BalancoEnergeticoDetalhado']
        
        ferramenta = Ferramentas()
        [primeira_linha, ultima_linha] = ferramenta.linha_nao_vazia(ws)
        
        
#        sul = arquivo_ipdo.sul
#        nordeste = arquivo_ipdo.nordeste
#        norte = arquivo_ipdo.norte
#        
#        nome_subistema, qtd_fontes, fontes, producao_vf, producao_pg, \
#                carga_vf, carga_pg, energia_natural_afluente_vf, \
#                energia_armazenada_reservatorio_vf
        
        
        energia_prevista = string.split(texto[0],';')  
        energia_verificada = string.split(texto[1],';')
        
        num_elementos_prevista = len(energia_prevista) # Número de elementos do resumo
        conta_valores = 0
        
        for conta_coluna_pg in xrange(1, num_elementos_prevista):
            letra = ferramenta.retorna_letra_da_coluna(conta_coluna_pg + 1)
            indice = letra + str(ultima_linha)            
            ws[indice] = energia_prevista[conta_valores]       
            conta_valores = conta_valores + 1
        
        num_elementos_verificada = len(energia_verificada) + conta_coluna_pg
        conta_valores = 0       
        
        for conta_coluna_vf in xrange(conta_coluna_pg, num_elementos_verificada):
            letra = ferramenta.retorna_letra_da_coluna(conta_coluna_vf + 2)
            indice = letra + str(ultima_linha)            
            ws[indice] = energia_verificada[conta_valores]
            conta_valores = conta_valores + 1                
        
        wb.save('IPDO.xlsx')   # sobrescreve resultados

        

        