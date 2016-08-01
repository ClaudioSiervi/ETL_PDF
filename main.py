# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 22:15:01 2016

@author: Claudio
"""

from etl_pdf import Extrair_Transformar_Carregar
from MapeiaTextoExtraido import MapeiaTexto


nome_arquivo_entrada = 'IPDO-22-06-2016'
nome_arquivo_saida = nome_arquivo_entrada + '-unlock.pdf'
nome_arquivo_entrada = nome_arquivo_entrada + '.pdf'

manipula_pdf = Extrair_Transformar_Carregar()
manipula_pdf.desbloqueia(nome_arquivo_entrada, nome_arquivo_saida)

texto_extraido = manipula_pdf.convert_pdf_to_html(nome_arquivo_saida)


#texto_extraido = manipula_pdf.converte_para_texto(nome_arquivo_saida)
#manipula_pdf.salva_texto_em_txt(texto_extraido, 'texto_extraido.html')
#
#

from bs4 import BeautifulSoup

html_extraido = BeautifulSoup(texto_extraido, 'html.parser')

manipula_pdf.salva_texto_em_txt(texto_extraido, 'texto_extraido.html')
print(html_extraido.prettify())

#texto_extraido2 = ' '.join(html_extraido.body.stripped_strings)
#texto_extraido3 = str(texto_extraido2.encode('utf-8'))





#mapeia = MapeiaTexto()
#mapeia.balanco_energia
#
#import String 
#
#
#for line in texto_extraido:
#    l 
#    

#for line in texto_extraido:
#    print line
    
#with open('texto_extraido.txt') as f:
#    for line in f:
#        line