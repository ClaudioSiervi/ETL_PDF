# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 11:03:06 2016

@author: Claudio
"""
### ETL --> Extract, Transform and Load



# Convert pdf to text
# http://stackoverflow.com/questions/5725278/how-do-i-use-pdfminer-as-a-library


def converte_pdf_para_texto(path):
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


# Unlock pdf
# https://lambdafu.net/2011/06/08/remove-password-from-pdf/
# http://stackoverflow.com/questions/10741600/running-command-lines-within-your-python-script

def desbloqueia_pdf(entrada, saida):
    # Cria uma versão desbloqueada do PDF
    import os
    os.system('qpdf --decrypt ' + entrada + ' ' + saida)



# Geração, Carga e Intercambio por Subsistema    
def pag_1(texto):
    # SUBSISTEMAS:  Sudeste|Sul|Nordeste|Norte|Itaipu
    # FONTES:       Ghidro|Gtermo|Geólica|Gsolar|Carga
    # INTERCÂMBIOS: N=>IMP|IMP=>NE|SE=>IMP|NE=>SE|S=>SE|S=>Export
    
    Sudeste = Subsistema
    Sudeste.Carga = 100
    
    texto
        
# Trabalhancom com classes  
# http://pythonclub.com.br/introducao-classes-metodos-python-basico.html    
class Subsistema(object):
    
    def __init__(self, nome, carga, ghidro, gtermo, geolica, gsolar):
        self.nome = nome
        self.carga = carga
        self.ghidro = ghidro
        self.gtermo = gtermo
        self.geolica = geolica
        self.gsolar = gsolar


# Troca de energia entre os subsistemas
class Intercambio:
    N_IMP = 0
    IMP_NE = 0
    SE_IMP = 0
    NE_SE = 0
    S_SE = 0
    S_Export = 0



#----------------------------------------------------------------



nome_arquivo_entrada = 'IPDO-11-06-2016'
nome_arquivo_saida = nome_arquivo_entrada + '-unlock.pdf'
nome_arquivo_entrada = nome_arquivo_entrada + '.pdf'

desbloqueia_pdf(nome_arquivo_entrada, nome_arquivo_saida)

texto_extraido = converte_pdf_para_texto(nome_arquivo_saida)

pag_1(texto_extraido)

arquivo_texto = open('texto_extraido.txt', "w")
arquivo_texto.write(texto_extraido)
arquivo_texto.close()

