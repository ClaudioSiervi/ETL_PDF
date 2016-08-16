# -*- coding: utf-8 -*-
"""
Created on Mon Aug 01 21:31:22 2016

@author: Claudio
"""

#      tp --> top
#      fl --> left
class DicionarioRegEx:
    
    # Organizar 
    
    geral = {
    'data_ipdo_tp' : 'top:(18[0-9]|19[0-9])px'
    }

    # Página 1
    balanco = {
    'programado_lf' : 'left:(27[0-9]|28[0-9])px',
    'programado_tp' : 'top:(30[0-9]|31[0-9])px',
    'verificado_lf' : 'left:(36[0-9]|37[0-9])px',
    'verificado_tp' : 'top:(30[0-9]|31[0-9])px'
    }
    
    
    sudeste = {
    'fontes_tp' : 'top:(130[5-9]|131[0-5])px', 
    'fontes_lf' : 'left:(38[0-9])px',

    'prod_verif_tp' : 'top:(131[5-9]|132[0-5])px', 
    'prod_verif_lf' : 'left:(47[0-9])px',
    'prod_prog_tp' : 'top:(131[5-9]|132[0-5])px', 
    'prod_prog_lf' : 'left:(51[5-9]|52[0-5])px',

#        'carga_verif_tp' : 'top:(18[0-9]|19[0-9])px', 
#        'carga_verif_lf' : 'left:(27[0-9]|28[0-9])px',
#        'carga_prog_tp' : 'top:(18[0-9]|19[0-9])px', 
#        'carga_prog_lf' : 'left:(27[0-9]|28[0-9])px',

    'ena_tp' : 'top:(47[3-9]|48[0-3])px', 
    'ena_lf' : 'left:(137[7-9]|138[0-8])px',

    'ear_tp' : 'top:(143[0-9])px', 
    'ear_lf' : 'left:(38[0-9])px'
    }

#        self.sul = {
#        'fontes_tp' : 'top:(18[0-9]|19[0-9])px', 
#        'fontes_lf' : 'left:(27[0-9]|28[0-9])px',
#        'prod_verif_tp' : 'top:(18[0-9]|19[0-9])px', 
#        'prod_verif_lf' : 'left:(27[0-9]|28[0-9])px',
#        'prod_prog_tp' : 'top:(18[0-9]|19[0-9])px', 
#        'prod_prog_lf' : 'left:(27[0-9]|28[0-9])px',
#        'carga_verif_tp' : 'top:(18[0-9]|19[0-9])px', 
#        'carga_verif_lf' : 'left:(27[0-9]|28[0-9])px',
#        'carga_prog_tp' : 'top:(18[0-9]|19[0-9])px', 
#        'carga_prog_lf' : 'left:(27[0-9]|28[0-9])px',
#        'ena_tp' : 'top:(18[0-9]|19[0-9])px', 
#        'ena_lf' : 'left:(27[0-9]|28[0-9])px',
#        'ear_tp' : 'top:(18[0-9]|19[0-9])px', 
#        'ear_lf' : 'left:(27[0-9]|28[0-9])px'
#        }
#        
#        self.nordeste = {
#        'fontes_tp' : 'top:(18[0-9]|19[0-9])px', 
#        'fontes_lf' : 'left:(27[0-9]|28[0-9])px',
#        'prod_verif_tp' : 'top:(18[0-9]|19[0-9])px', 
#        'prod_verif_lf' : 'left:(27[0-9]|28[0-9])px',
#        'prod_prog_tp' : 'top:(18[0-9]|19[0-9])px', 
#        'prod_prog_lf' : 'left:(27[0-9]|28[0-9])px',
#        'carga_verif_tp' : 'top:(18[0-9]|19[0-9])px', 
#        'carga_verif_lf' : 'left:(27[0-9]|28[0-9])px',
#        'carga_prog_tp' : 'top:(18[0-9]|19[0-9])px', 
#        'carga_prog_lf' : 'left:(27[0-9]|28[0-9])px',
#        'ena_tp' : 'top:(18[0-9]|19[0-9])px', 
#        'ena_lf' : 'left:(27[0-9]|28[0-9])px',
#        'ear_tp' : 'top:(18[0-9]|19[0-9])px', 
#        'ear_lf' : 'left:(27[0-9]|28[0-9])px'
#        }
#        
#        self.norte = {
#        'fontes_tp' : 'top:(18[0-9]|19[0-9])px', 
#        'fontes_lf' : 'left:(27[0-9]|28[0-9])px',
#        'prod_verif_tp' : 'top:(18[0-9]|19[0-9])px', 
#        'prod_verif_lf' : 'left:(27[0-9]|28[0-9])px',
#        'prod_prog_tp' : 'top:(18[0-9]|19[0-9])px', 
#        'prod_prog_lf' : 'left:(27[0-9]|28[0-9])px',
#        'carga_verif_tp' : 'top:(18[0-9]|19[0-9])px', 
#        'carga_verif_lf' : 'left:(27[0-9]|28[0-9])px',
#        'carga_prog_tp' : 'top:(18[0-9]|19[0-9])px', 
#        'carga_prog_lf' : 'left:(27[0-9]|28[0-9])px',
#        'ena_tp' : 'top:(18[0-9]|19[0-9])px', 
#        'ena_lf' : 'left:(27[0-9]|28[0-9])px',
#        'ear_tp' : 'top:(18[0-9]|19[0-9])px', 
#        'ear_lf' : 'left:(27[0-9]|28[0-9])px'
#        }
#        
#        self.Intercambio = {
#        'norte-imperatriz_tp' : 'top:(18[0-9]|19[0-9])px', 
#        'norte-imperatriz_lf' : 'top:(18[0-9]|19[0-9])px', 
#        'imperatriz-nordeste_tp' : 'left:(27[0-9]|28[0-9])px',
#        'imperatriz-nordeste_lf' : 'left:(27[0-9]|28[0-9])px',
#        'itaipu-sudeste_tp' : 'top:(18[0-9]|19[0-9])px', 
#        'itaipu-sudeste_lf' : 'top:(18[0-9]|19[0-9])px', 
#        'sudeste-imperatriz_tp' : 'left:(27[0-9]|28[0-9])px',
#        'sudeste-imperatriz_lf' : 'left:(27[0-9]|28[0-9])px',
#        'sul-sudeste_tp' : 'top:(18[0-9]|19[0-9])px', 
#        'sul-sudeste_lf' : 'top:(18[0-9]|19[0-9])px', 
#        'internacional-sul_tp' : 'left:(27[0-9]|28[0-9])px',
#        'internacional-sul_lf' : 'left:(27[0-9]|28[0-9])px',
#        }