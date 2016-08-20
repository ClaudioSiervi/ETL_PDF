# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 17:16:21 2016

@author: Claudio
"""

dic = {
    'fontes_tp' : 'top:(138[0-9]|139[0-9]|140[0-9]|141[0-9]|142[0-9]|143[0-9])px', 
    'fontes_lf' : 'left:(16[0-9]|17[0-9]|18[0-9]|19[0-9]|20[0-9]|21[0-9]|22[0-9])px',

    'prod_verif_tp' : 'top:(139[0-9]|140[0-9]|141[0-9]|142[0-9]|143[0-9]|144[0-9])px', 
    'prod_verif_lf' : 'left:(27[0-9]|28[0-9]|29[0-9]|29[0-9]|30[0-9]|31[0-9])px',
    'prod_prog_tp' : 'top:(139[0-9]|140[0-9]|141[0-9]|142[0-9]|143[0-9]|144[0-9])px', 
    'prod_prog_lf' : 'left:(32[0-9]|33[0-9]|34[0-9]|35[0-9]|36[0-9])px',

    'carga_verif_tp' : 'top:(143[0-9]|144[0-9]|145[0-9]|146[0-9]|147[0-9]|148[0-9])px', 
    'carga_verif_lf' : 'left:(27[0-9]|28[0-9]|29[0-9]|29[0-9]|30[0-9]|31[0-9])px',
    'carga_prog_tp' : 'top:(143[0-9]|144[0-9]|145[0-9]|146[0-9]|147[0-9]|148[0-9])px', 
    'carga_prog_lf' : 'left:(32[0-9]|33[0-9]|34[0-9]|35[0-9]|36[0-9])px',

    'ena_tp' : 'top:(145[0-9]|146[0-9]|147[0-9]|148[0-9]|149[0-9]|150[0-9])px', 
    'ena_lf' : 'left:(26[0-9]|27[0-9]|28[0-9]|29[0-9]|30[0-9]|31[0-9])px',

    'ear_tp' : 'top:(150[0-9]|151[0-9]|152[0-9]|153[0-9]|154[0-9]|155[0-9])px', 
    'ear_lf' : 'left:(21[0-9]|22[0-9]|23[0-9]|24[0-9]|25[0-9]|26[0-9])px'
    }
    
import os
from bs4 import BeautifulSoup
from etl_pdf import ExtrairTransformarCarregar
from ExtracaoTexto import Subsistemas   

#arquivo_ipdo = ArquivoIPDO(nome_arquivo_entrada)
subsistema = Subsistemas()    
converte = ExtrairTransformarCarregar()
caminho = os.getcwd()

caminho = os.getcwd()
caminho = str(caminho) + '\Scripts-py'

for dia in xrange(22,23):
    if (dia <10):
        nome_arquivo_entrada = caminho + '\IPDO-0'+str(dia)+'-05-2016'
    else:
        nome_arquivo_entrada = caminho + '\IPDO-'+str(dia)+'-05-2016'
        
   # exemplo:  nome_arquivo_entrada = 'IPDO-22-06-2016.pdf'
nome_arquivo_saida = nome_arquivo_entrada + '-unlocked.pdf'
# exemplo:  nome_arquivo_entrada = 'IPDO-22-06-2016.pdf'
nome_arquivo_entrada = nome_arquivo_entrada + '.pdf'

tag='div'

html_extraido = converte.pdf_para_html(nome_arquivo_saida)

objeto_bs = BeautifulSoup(html_extraido, 'html.parser')

producao_vf = subsistema.producao(objeto_bs, tag, dic['prod_verif_lf'], dic['prod_verif_tp'] )
producao_pg = subsistema.producao(objeto_bs, tag, dic['prod_prog_lf'], dic['prod_prog_tp'] )

print 'produção_vf  ->' + str(len(producao_vf)) + str(producao_vf)
print 'produção_pg  ->' + str(len(producao_pg)) + str(producao_pg)

#carga_vf = subsistema.carga(objeto_bs, tag, dic['carga_verif_lf'], dic['carga_verif_tp'] )
#carga_pg = subsistema.carga(objeto_bs, tag, dic['carga_prog_lf'], dic['carga_prog_tp'] )
