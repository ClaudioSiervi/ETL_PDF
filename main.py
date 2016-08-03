# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 22:15:01 2016

@author: Claudio
"""

from etl_pdf import Carregar_Transformar_Extrair
from MapeiaTextoExtraido import MapeiaTexto
from ImprimeResultados import ImprimeArquivosTexto

nome_arquivo_entrada = 'IPDO-11-06-2016'
nome_arquivo_saida = nome_arquivo_entrada + '-unlock.pdf'
nome_arquivo_entrada = nome_arquivo_entrada + '.pdf'

converte = Carregar_Transformar_Extrair()
converte.desbloqueia(nome_arquivo_entrada, nome_arquivo_saida)

html_extraido = converte.pdf_para_html(nome_arquivo_saida)
#texto_extraido = converte.pdf_para_texto(nome_arquivo_saida)


mapeia = MapeiaTexto()
mapeia.resumo_balanco_energia(html_extraido)


salva = ImprimeArquivosTexto()
salva.texto_em_html(html_extraido, 'texto_extraido.html')



#manipula_pdf.salva_texto_em_txt(texto_extraido, 'texto_extraido.txt')
#print(html_extraido.prettify())
