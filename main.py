# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 22:15:01 2016

@author: Claudio
"""


from Arquivo import ArquivoIPDO
from ImprimeResultados import ImprimeArquivosTexto

import os

caminho = os.getcwd()
caminho = str(caminho) + '\Scripts-py'

for dia in xrange(22,23):
    if (dia <10):
        nome_arquivo_entrada = caminho + '\IPDO-0'+str(dia)+'-05-2016'
    else:
        nome_arquivo_entrada = caminho + '\IPDO-'+str(dia)+'-05-2016'
     
             ##TODO --> Organizar impressões sequencialmente em um arquivo único
    arquivo_ipdo = ArquivoIPDO(nome_arquivo_entrada)
       
#    print arquivo_ipdo.sudeste
#    print arquivo_ipdo.sul
#    print arquivo_ipdo.nordeste
#    print arquivo_ipdo.norte

   
#    
#    imprime = ImprimeArquivosTexto()
#    
#    imprime.texto_em_html(arquivo_ipdo.html_extraido, 'texto_extraido.html')
#        
#    imprime.data_em_xlsx(arquivo_ipdo.data_relatorio) 
#    imprime.resumo_balanco_em_xlsx(arquivo_ipdo.resumo_balanco_energia)
#    
#    se = arquivo_ipdo.balanco_por_subsistema       
#    
    


  
    
    



#manipula_pdf.salva_texto_em_txt(texto_extraido, 'texto_extraido.txt')
#print(html_extraido.prettify())
