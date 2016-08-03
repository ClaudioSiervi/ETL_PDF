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
        
        
    def texto_em_xlsx(self, texto):
        
        #from openpyxl import Workbook
        from openpyxl import load_workbook  
        import string
        #        try:
        wb = load_workbook('IPDO.xlsx') 
        ws = wb['Tabela1']
        
        [plinha, ulinha] = self.linha_nao_vazia(ws)
        
        prevista = string.split(texto[0],';')  
        verificada = string.split(texto[1],';')
        percent_sin = string.split(texto[2],';')
        
        tam = len(prevista)
        conta_valores = 0
        print tam
        print prevista
        for cont in xrange(1,tam):         
            indice = 'B'+ str(ulinha + cont)            
            ws[indice] = float(prevista[conta_valores])
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
        
        
        