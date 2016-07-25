# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 11:03:06 2016

@author: Claudio
"""
# Convert pdf to text
# http://stackoverflow.com/questions/5725278/how-do-i-use-pdfminer-as-a-library

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from cStringIO import StringIO

def convert_pdf_to_txt(path):
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


# Unlock pdf
# https://lambdafu.net/2011/06/08/remove-password-from-pdf/

def unlock_pdf(entrada, saida):
    import os
    os.system('qpdf --decrypt ' + entrada + ' ' + saida)

#----------------------------------------------------------------

nome_arquivo_entrada = 'IPDO-11-06-2016'
nome_arquivo_saida = nome_arquivo_entrada + '-unlock.pdf'
nome_arquivo_entrada = nome_arquivo_entrada + '.pdf'

unlock_pdf(nome_arquivo_entrada, nome_arquivo_saida)

texto_extraido = convert_pdf_to_txt(nome_arquivo_saida)

arquivo_texto = open('texto_extraido.txt', "w")
arquivo_texto.write(texto_extraido)
arquivo_texto.close()

