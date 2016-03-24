#!/usr/bin/python
#coding: utf-8

import requests


datadict = {'navn': "Therese", "kommentar": "Jeg vil også kommentere!"}

r = requests.post("http://127.0.0.1:5000/new-comment", data=datadict)

if r:
    print( r.text)


# GET Request
r = requests.get("http://vg.no")

if r:
    print( r.text )