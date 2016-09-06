# -*- coding: utf-8 -*-
"""
Created on Tue Sep 06 11:42:45 2016

@author: Claudio
"""
# Show users
from firebase import firebase
firebase = firebase.FirebaseApplication('https://wesee-dw.firebaseio.com/foo', None)
new_user = 'Cláudio'

result = firebase.post('/users', new_user, {'print': 'pretty'}, {'X_FANCY_HEADER': 'VERY FANCY'})
print result
