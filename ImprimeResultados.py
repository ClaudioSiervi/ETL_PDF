# -*- coding: utf-8 -*-
"""
Created on Tue Aug 02 19:20:17 2016

@author: Claudio
"""

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
        from openpyxl import load_workbook  
        
        #        try:
        wb = load_workbook('IPDO.xlsx') 
        ws = wb['Tabela1']
        
        [plinha, ulinha] = self.linha_nao_vazia(ws)
        ulinha =ulinha+1        
        
        indice = 'A'+str(ulinha)            
        ws[indice] = data
        wb.save('IPDO.xlsx')
        
        
    #texto_em_xlsx
    # balanco_energia_sin
    def resumo_balanco_em_xlsx(self, texto):
        
        #from openpyxl import Workbook
        from openpyxl import load_workbook  
        import string
        #        try:
        wb = load_workbook('IPDO.xlsx') 
        ws = wb['Tabela1']
        
        [plinha, ulinha] = self.linha_nao_vazia(ws)
#        ulinha = ulinha +1
        
        prevista = string.split(texto[0],';')  
        verificada = string.split(texto[1],';')
#        percent_sin = string.split(texto[2],';')
        
        tam = len(prevista)
        conta_valores = 0
        print tam
        print prevista
        for cont in xrange(1,tam):
            letra = self.get_column_letter(cont + 1)
            #print letra
            indice = letra + str(ulinha)            
            ws[indice] = prevista[conta_valores]
#            ws[indice] = float(prevista[conta_valores])            
            conta_valores = conta_valores + 1
        
        tam = len(verificada) + cont
        conta_valores = 0
#        print tam
        print verificada
        for cont in xrange(cont, tam):
            letra = self.get_column_letter(cont + 2)
            #print letra
            indice = letra + str(ulinha)            
            ws[indice] = verificada[conta_valores]
#            ws[indice] = float(verificada[conta_valores])
            conta_valores = conta_valores + 1
              
        
        print conta_valores        
        wb.save('IPDO.xlsx')   # sobrescreve resultados
    #        return plinha, ulinha
#            pass
        ##
            # ------------
#        except:
#            print '------------------------------------------------------------'
#            print 'ERRO: Não foi possível salvar os resultados na planilha.xlsx'
#            print 'A planilha deve estar aberta =)'
#            pass
#            
        
        
        
        
    def linha_nao_vazia(self, ws):
        ######## Encontra a primeira e a ultima linha não vazia
    
        self.tam = ws.max_row + 1
        self.primeira_linha = 0
        self.ultima_linha = 0
        
        for item in xrange(1, self.tam):
            self.celula_valor = ws.cell(row=item, column = 1).value  
            if (self.celula_valor is not None) and (self.primeira_linha == 0):
                self.primeira_linha = item
            elif (self.celula_valor is not None) and (self.primeira_linha is not 0):
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
            
        