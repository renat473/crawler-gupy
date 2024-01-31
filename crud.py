# -*- coding: utf-8 -*-

def insert(collection, post):
    try:
        collection.insert_one(post)
    except:
        print('Vaga inserida anteriormente')
        return 1

def update(collection, post, ri, pack={}):
    pack['$set'] = post
    try:
        collection.find_one_and_update(ri, pack)
    except:
        print('Falha na atualização')

def remove(collection, dc):
    try:
        collection.delete_one(dc)
        print(dc, ' removed')
    except:
        print('Falha na remoção da vaga')
