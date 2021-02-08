from behave import *
import requests
import json
import jsonpath


@given(u'Verificar Respuesta GET de "{URL}" con ID "{ID}"')
def Obtencion(context,URL,ID):
    # Api URL
    url = URL + ID
    assert url != ' ' , 'No existe la URL'


@then(u'Obtenemos una respuesta igual a "{valor}" de "{URL}" con ID "{ID}"')
def Respuesta(context,valor,URL,ID):
    # Enviamos la petición del GET
    context.url = URL + ID
    context.response = requests.get(context.url)
    context.status = str(context.response.status_code)
    context.json_response = json.loads(context.response.text)
    context.mensaje = jsonpath.jsonpath(context.json_response,'message')
    #Se verifica si el schema del Json es correcto
    try:
        context.json_response
    except ValueError as err:
        "Formato del Schema incorrecto"

    assert context.status == valor , 'No es la respuesta esperada ' \
                                     + valor +' es un ' + context.status 




