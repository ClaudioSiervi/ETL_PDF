# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 22:15:01 2016

@author: Claudio
"""

from etl_pdf import ExtrairTransformarCarregar
from MapeiaTextoExtraido import MapeiaTexto
from ImprimeResultados import ImprimeArquivosTexto
from bs4 import BeautifulSoup

import os

caminho = os.getcwd()
caminho = str(caminho) + '\Scripts-py'
for dia in xrange(1,2):
    if (dia <10):
        nome_arquivo_entrada = caminho + '\IPDO-0'+str(dia)+'-05-2016'
    else:
        nome_arquivo_entrada = caminho + '\IPDO-'+str(dia)+'-05-2016'
        
    #nome_arquivo_entrada = 'IPDO-22-06-2016'
    nome_arquivo_saida = nome_arquivo_entrada + '-unlock.pdf'
    nome_arquivo_entrada = nome_arquivo_entrada + '.pdf'
    
    converte = ExtrairTransformarCarregar()
    converte.desbloqueia(nome_arquivo_entrada, nome_arquivo_saida)
    
    html_extraido = converte.pdf_para_html(nome_arquivo_saida)
    #texto_extraido = converte.pdf_para_texto(nome_arquivo_saida)
    
    objeto_bs = BeautifulSoup(html_extraido, 'html.parser')
    
     ##TODO --> Organizar impressões sequencialmente em um arquivo único
    mapeia = MapeiaTexto()    
    salva = ImprimeArquivosTexto()
    
    salva.data_em_xlsx(mapeia.data_relatorio(objeto_bs)) 
    salva.resumo_balanco_em_xlsx(mapeia.resumo_balanco_energia(objeto_bs))
    
    se = mapeia.balanco_por_subsistema(objeto_bs)        
    
    salva.texto_em_html(html_extraido, 'texto_extraido.html')
    
    
    

  
    
    



#manipula_pdf.salva_texto_em_txt(texto_extraido, 'texto_extraido.txt')
#print(html_extraido.prettify())
