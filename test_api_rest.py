# -*- coding: utf-8 -*-
"""
Created on Tue Sep 06 11:42:45 2016

@author: Claudio
"""
from firebase import Firebase
f = Firebase('https://wesee-dw.firebaseio.com/teste')
f.post({'text': 'Hello'})
