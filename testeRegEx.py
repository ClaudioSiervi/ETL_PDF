# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 17:16:21 2016

@author: Claudio
"""

                # norte
fontes = {
    'fontes_tp' : 'top:(107[0-9]|108[0-9]|109[0-9])px', 
    'fontes_lf' : 'left:(6[0-9]|7[0-9]|8[0-9]|9[0-9])px',
}
producao = {
    'prod_verif_tp' : 'top:(110[0-9]|111[0-9]|112[0-9])px', 
    'prod_verif_lf' : 'left:(16[0-9]|17[0-9])px',
    'prod_prog_tp' : 'top:(110[0-9]|111[0-9]|112[0-9])px',  
    'prod_prog_lf' : 'left:(20[0-9]|21[0-9]|22[0-9])px',
    }
carga = { 
    'carga_verif_tp' : 'top:(114[0-9]|115[0-9])px', 
    'carga_verif_lf' : 'left:(16[0-9]|17[0-9])px',
    'carga_prog_tp' : 'top:(114[0-9]|115[0-9])px', 
    'carga_prog_lf' : 'left:(20[0-9]|21[0-9])px',
}
ena = {
    'ena_tp' : 'top:(115[0-9]|116[0-9]|117[0-9])px', 
    'ena_lf' : 'left:(14[0-9]|15[0-9]|16[0-9])px',
}
ear = {
    'ear_tp' : 'top:(120[0-9]|121[0-9]|122[0-9]|123[0-9])px', 
    'ear_lf' : 'left:(10[0-9]|11[0-9]|12[0-9])px',
    }

dic ={ }
dic.update(fontes)
dic.update(producao)
dic.update(carga)
dic.update(ena)
dic.update(ear)

    
import os
from bs4 import BeautifulSoup
from etl_pdf import Ferramentas
from ExtracaoTexto import Subsistemas   

#arquivo_ipdo = ArquivoIPDO(nome_arquivo_entrada)
subsistema = Subsistemas()    
converte = Ferramentas()
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

fontes = subsistema.fontes(objeto_bs, tag, dic['fontes_lf'], dic['fontes_tp'] )

#print fontes

producao_vf = subsistema.producao(objeto_bs, tag, dic['prod_verif_lf'], dic['prod_verif_tp'] )
producao_pg = subsistema.producao(objeto_bs, tag, dic['prod_prog_lf'], dic['prod_prog_tp'] )


print 'produção_vf  ->' + str(len(producao_vf)) + str(producao_vf)
print 'produção_pg  ->' + str(len(producao_pg)) + str(producao_pg)

if ((len(producao_vf)==5) & (len(producao_pg)==5)):
    carga_vf = [producao_vf.pop()]
    carga_pg = [producao_pg.pop()]

    print 'carga_vf  ->' + str(len(carga_vf)) + '- ' + str(carga_vf)
    print 'carga_pg  ->' + str(len(carga_pg)) + '- ' + str(carga_pg)
   
elif ((len(producao_vf)==4) & (len(producao_pg)==4)):  
    carga_vf = subsistema.producao(objeto_bs, tag, dic['carga_verif_lf'], dic['carga_verif_tp'] )
    carga_pg = subsistema.producao(objeto_bs, tag, dic['carga_prog_lf'], dic['carga_prog_tp'] )
    
    print '5'
    print 'carga_vf  ->' + str(len(carga_vf)) + str(carga_vf)
    print 'carga_pg  ->' + str(len(carga_pg)) + str(carga_pg)
    
else:
    print 'Erro ao ler a carga.'
    print 'O arquivo deve ter mudado de estrutura.'


ena_vf = subsistema.ena(objeto_bs, tag, dic['ena_lf'], dic['ena_tp'] )
print 'ena_vf -->' + str(ena_vf)

ear_vf = subsistema.ear(objeto_bs, tag, dic['ear_lf'], dic['ear_tp'] )
print 'ear_vf -->' + str(ear_vf)
#carga_vf = subsistema.carga(objeto_bs, tag, dic['carga_verif_lf'], dic['carga_verif_tp'] )
#carga_pg = subsistema.carga(objeto_bs, tag, dic['carga_prog_lf'], dic['carga_prog_tp'] )
