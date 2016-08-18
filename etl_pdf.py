# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 11:03:06 2016

@author: Claudio
"""
### ETL --> Extract, Transform and Load


# Convert pdf to text
# http://stackoverflow.com/questions/5725278/how-do-i-use-pdfminer-as-a-library
import string

class ExtrairTransformarCarregar:
    

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


        
        
        
         
                
                
        
    
