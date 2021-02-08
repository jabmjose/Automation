from behave import *
import requests
import json
import jsonpath
import os

@given(u'Verificamos existencia de Json para POST')
def Existencia(context):
    context.file = open("features//steps//FormatoJsonPOST.json",'r','r')
    

@then(u'Obtenemos una respuesta igual a "{Respuesta}" de "{URL}"')
def ObtenerPOST(context,Respuesta,URL):
    context.url = URL
    context.file = open("features//steps//FormatoJsonPOST.json",'r')
    context.json_input = context.file.read()
    context.request_json = json.loads(context.json_input)
    context.headers={'Content-type':'application/json', 'Accept':'application/json'}
    context.response = requests.post (url=context.url,json=context.request_json,headers=context.headers)
    assert context.response.status_code == int(Respuesta) ,"El status code es diferente a 200 es: " + str(context.response.status_code)