# -*- coding: utf-8 -*-
"""
Created on Tue Aug 02 19:20:17 2016

@author: Claudio
"""
from openpyxl import load_workbook
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
        
        [plinha, ulinha] = self.linha_nao_vazia(ws)
        ulinha =ulinha+1        
        
        indice = 'A'+str(ulinha)            
        ws[indice] = data
        wb.save('IPDO.xlsx')
        
        
        
    # Imprime o resumo do balanço energético    
    def resumo_balanco_em_xlsx(self, texto):
        #        try:
        wb = load_workbook('IPDO.xlsx') 
        ws = wb['Tabela1']
        
        [primeira_linha, ultima_linha] = self.linha_nao_vazia(ws)
        
        energia_prevista = string.split(texto[0],';')  
        energia_verificada = string.split(texto[1],';')
        
        num_elementos_prevista = len(energia_prevista) # Número de elementos do resumo
        conta_valores = 0
        print num_elementos_prevista
        print energia_prevista
        
        for conta_coluna_pg in xrange(1, num_elementos_prevista):
            letra = self.get_column_letter(conta_coluna_pg + 1)
            indice = letra + str(ultima_linha)            
            ws[indice] = energia_prevista[conta_valores]       
            conta_valores = conta_valores + 1
        
        num_elementos_verificada = len(energia_verificada) + conta_coluna_pg
        print conta_coluna_pg        
        print num_elementos_verificada
        conta_valores = 0       
        
        for conta_coluna_vf in xrange(conta_coluna_pg, num_elementos_verificada):
            letra = self.get_column_letter(conta_coluna_vf + 2)
            indice = letra + str(ultima_linha)            
            ws[indice] = energia_verificada[conta_valores]
            conta_valores = conta_valores + 1
        
        print energia_verificada       
        print conta_valores              
        
        wb.save('IPDO.xlsx')   # sobrescreve resultados
    #        return plinha, ulinha

#        except:
#            print '------------------------------------------------------------'
#            print 'ERRO: Não foi possível salvar os resultados na planilha.xlsx'               
        
        
    def balanco_energia_detalhado_em_xlsx(self, data):
    
        wb = load_workbook('IPDO.xlsx') 
        ws = wb['BalançoEnergéticoDetalhado']
        
        [plinha, ulinha] = self.linha_nao_vazia(ws)
        ulinha =ulinha+1        
        
        indice = 'A'+str(ulinha)            
        ws[indice] = data
        
        wb.save('IPDO.xlsx')
        

        
    def linha_nao_vazia(self, ws):
        ######## Encontra a primeira e a ultima linha não vazia
    
        tam = ws.max_row + 1
        self.primeira_linha = 0
        self.ultima_linha = 0
        
        for item in xrange(1, tam):
            celula_valor = ws.cell(row=item, column = 1).value  
            if (celula_valor is not None) and (self.primeira_linha == 0):
                self.primeira_linha = item
            elif (celula_valor is not None) and (self.primeira_linha is not 0):
                self.ultima_linha = item
                                
            if (self.ultima_linha == 0):
                self.ultima_linha = self.primeira_linha
                      
        return self.primeira_linha, self.ultima_linha     
        

    
    # http://openpyxl.readthedocs.io/en/2.3.3/_modules/openpyxl/utils.html    
    def get_column_letter(self, col_idx):
        """Convert a column number into a column letter (3 -> 'C')
    
        Right shift the column col_idx by 26 to find column letters in reverse
        order.  These numbers are 1-based, and can be converted to ASCII
        ordinals by adding 64.
    
        """
        # these indicies corrospond to A -> ZZZ and include all allowed
        # columns
        if not 1 <= col_idx <= 18278:
            raise ValueError("Invalid column index {0}".format(col_idx))
        letters = []
        while col_idx > 0:
            col_idx, remainder = divmod(col_idx, 26)
            # check for exact division and borrow if needed
            if remainder == 0:
                remainder = 26
                col_idx -= 1
            letters.append(chr(remainder+64))
        return ''.join(reversed(letters))
            
        