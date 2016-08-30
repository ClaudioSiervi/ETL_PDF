# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 11:03:06 2016

@author: Claudio
"""
### ETL --> Extract, Transform and Load


# Convert pdf to text
# http://stackoverflow.com/questions/5725278/how-do-i-use-pdfminer-as-a-library
import string

class Ferramentas:
    

    # Desbloqueia um pdf com senha
    # https://lambdafu.net/2011/06/08/remove-password-from-pdf/
    # http://stackoverflow.com/questions/10741600/running-command-lines-within-your-python-script
        
    def desbloqueia(self, entrada, saida):
        # Cria uma versão desbloqueada de PDF com senha
        import os
        os.system('qpdf --decrypt ' + entrada + ' ' + saida)
    
    
    
    def pdf_para_texto(self, path):
    # Converte um arquivo pdf para texto
        from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
        from pdfminer.converter import TextConverter
        from pdfminer.layout import LAParams
        from pdfminer.pdfpage import PDFPage
        from cStringIO import StringIO    
        
        rsrcmgr = PDFResourceManager()
        retstr = StringIO()
        codec = 'utf-8'
        laparams = LAParams()
        device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
        fp = file(path, 'rb')
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        password = ""
        maxpages = 0
        caching = True
        pagenos=set()
    
        for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
            interpreter.process_page(page)
    
        text = retstr.getvalue()
    
        fp.close()
        device.close()
        retstr.close()
        return text
    


    def pdf_para_html(self, path):
        from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
        from pdfminer.converter import HTMLConverter
#        from pdfminer.converter import TextConverter
        from pdfminer.layout import LAParams
        from pdfminer.pdfpage import PDFPage
        from cStringIO import StringIO
#        import re
#        import csv
        
        
        rsrcmgr = PDFResourceManager()
        retstr = StringIO()
        codec = 'utf-8'
        laparams = LAParams()
        device = HTMLConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
        fp = file(path, 'rb')
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        password = ""
        maxpages = 0 #is for all
        caching = True
        pagenos=set()
        for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
            interpreter.process_page(page)
        fp.close()
        device.close()
        str = retstr.getvalue()
        retstr.close()
        return str



    # extrai dados de um objeto bs a partir da posição dos elementos da tag desejada
    def dados_objeto_bs(self, objeto_bs, tag, left_tx, top_tx):   
        import re

        tag_encontrada = objeto_bs.find(tag, style=re.compile(r''+ left_tx+'.*?'+top_tx))             
        conteudo_tag = tag_encontrada.contents          
        
        texto_extraido_unicode =''
        tam = len(conteudo_tag)
        for item in xrange(0, tam):
            # extrai o texto do objeto conteudo_tag
            texto_extraido_unicode = texto_extraido_unicode + ';' .join(conteudo_tag[item].stripped_strings)
            texto_extraido_unicode = texto_extraido_unicode + ';'
        texto_extraido_str = string.split(texto_extraido_unicode.encode('utf-8'), ';')
        print texto_extraido_str         
        
        tam = len(texto_extraido_str)
        texto_utf8 = []
        for item in xrange(0, tam):
            texto_utf8.append(texto_extraido_str[item])
        print texto_utf8
#        print texto.decode('utf-8')
              
        return texto_extraido_str       



        
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
    def retorna_letra_da_coluna(self, col_idx):
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
                       
        
         
                
                
        
    
