# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 17:55:41 2016

@author: Claudio
"""

caminho = os.getcwd()
dia = "01"
mes = "08"
ano = "2016"
caminho = str(caminho) + "\Scripts-py\\" + mes +"-" + ano
nome_arquivo_entrada = caminho + '\IPDO-'+str(dia)+ "-" + mes +"-" + ano +"-unlocked.pdf"

from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
import os

# makes a PDF file object
fp = open(nome_arquivo_entrada, 'rb')
# fetch PDF objects from a file stream
parser = PDFParser(fp)
# stores document's structure
document = PDFDocument(parser,password="" )
# check if the document allows text extraction. If not, abort.

if not document.is_extractable:
    raise PDFTextExtractionNotAllowed
    # Create a PDF resource manager object that stores shared resources.
rsrcmgr = PDFResourceManager()
# Create a PDF device object.
device = PDFDevice(rsrcmgr)
# Create a PDF interpreter object.
interpreter = PDFPageInterpreter(rsrcmgr, device)
# Process each page contained in the document.
pages =[]
for page in PDFPage.create_pages(document):
    pages.append(page)
    
    