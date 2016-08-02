# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 22:15:01 2016

@author: Claudio
"""

from etl_pdf import Extrair_Transformar_Carregar
from MapeiaTextoExtraido import MapeiaTexto


nome_arquivo_entrada = 'IPDO-11-06-2016'
nome_arquivo_saida = nome_arquivo_entrada + '-unlock.pdf'
nome_arquivo_entrada = nome_arquivo_entrada + '.pdf'

manipula_pdf = Extrair_Transformar_Carregar()
manipula_pdf.desbloqueia(nome_arquivo_entrada, nome_arquivo_saida)

texto_extraido = manipula_pdf.converte_pdf_para_html(nome_arquivo_saida)

mapeia = MapeiaTexto()
mapeia.resumo_balanco_energia(texto_extraido)

texto_extraido = manipula_pdf.converte_pdf_para_texto(nome_arquivo_saida)
manipula_pdf.salva_texto_em_html(texto_extraido, 'texto_extraido.html')
#  imprimir excel
#


manipula_pdf.salva_texto_em_xlsx()


#manipula_pdf.salva_texto_em_txt(texto_extraido, 'texto_extraido.txt')
#print(html_extraido.prettify())



#for line in texto_extraido:
#    l 
#    

#for line in texto_extraido:
#    print line
    
#with open('texto_extraido.txt') as f:
#    for line in f:
#        line