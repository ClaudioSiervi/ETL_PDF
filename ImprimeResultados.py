# -*- coding: utf-8 -*-
"""
Created on Tue Aug 02 19:20:17 2016

@author: Claudio
"""
from openpyxl import load_workbook
#from Arquivo import ArquivoIPDO
from etl_pdf import Ferramentas
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
        self.arquivo_texto = open(nome_arquivo_saida, "w")
        self.status_escrita = self.arquivo_texto.write(texto)
        self.arquivo_texto.close()
        
        
    # Imprime a data do IPDO    
    def data_em_xlsx(self, data):
        
        #        try:
        wb = load_workbook('IPDO.xlsx') 
        ws = wb['Tabela1']
        
        ferramenta = Ferramentas()
        [plinha, ulinha] = ferramenta.linha_nao_vazia(ws)
        ulinha =ulinha+1        
        
        indice = 'A'+str(ulinha)            
        ws[indice] = data
        wb.save('IPDO.xlsx')
        
        
        
    # Imprime o resumo do balanço energético    
    def resumo_balanco_em_xlsx(self, texto):
        #        try:
        wb = load_workbook('IPDO.xlsx') 
        ws = wb['Tabela1']
        
        ferramenta = Ferramentas()
        [primeira_linha, ultima_linha] = ferramenta.linha_nao_vazia(ws)
        
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
    #        return plinha, ulinha

#        except:
#            print '------------------------------------------------------------'
#            print 'ERRO: Não foi possível salvar os resultados na planilha.xlsx'               
        
        
        
    @classmethod
    def balanco_energia_detalhado_em_xlsx(self, data):
    
        wb = load_workbook('IPDO.xlsx') 
        ws = wb['BalançoEnergéticoDetalhado']
        
        
        [primeira_linha, ultima_linha] = self.linha_nao_vazia(ws)
        
        energia_prevista = string.split(texto[0],';')  
        energia_verificada = string.split(texto[1],';')
        
        num_elementos_prevista = len(energia_prevista) # Número de elementos do resumo
        conta_valores = 0
        
        for conta_coluna_pg in xrange(1, num_elementos_prevista):
            letra = self.retorna_letra_da_coluna(conta_coluna_pg + 1)
            indice = letra + str(ultima_linha)            
            ws[indice] = energia_prevista[conta_valores]       
            conta_valores = conta_valores + 1
        
        wb.save('IPDO.xlsx')
        

        

        