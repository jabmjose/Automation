from behave import *
import requests
import json
import jsonpath

@given(u'Verificamos existencia de Json')
def Existencia(context):
    context.url = "https://petstore.swagger.io/v2/store/order"
    context.file = open("C:\\Users\\jblanco\\Desktop\\Personal\\Baufest Automation\\WebService\\features\\steps\\FormatoJson.json",'r')
    context.json_input= context.file.read()
    context.request_json = json.loads(context.json_input)
    context.response = requests.post(context.url,context.request_json)
    print(context.response.content)
