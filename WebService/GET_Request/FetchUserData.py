import requests
import json
import jsonpath
"""""
###########Para GET#######################################
#Api URL
url = "https://reqres.in/api/users?page=2"
#url = "https://petstore.swagger.io/v2/pet/1" #Para Ejercicio

#Enviamos la petición del GET
response = requests.get(url)
status = response.status_code

# Muestra el código del Response
print(response)
print("Status Code:",status)
if status == 200:
    print("Respuesta OK")
else:
    print("Respuesta Incorrecta")


# Muestra contenido del Response
print(response.content)

#Parseo de response a formato Json

json_response = json.loads(response.text)

print(json_response)

#Traemos un valor usando jason path
pages = jsonpath.jsonpath(json_response,'total_pages')
print(pages[0])
assert pages[0] == 2

#####################PARA POST################################
url = "https://petstore.swagger.io/v2/pet"
file = open("C:\\Users\\jblanco\\Desktop\\Personal\\Baufest Automation\\WebService\\features\\steps\\FormatoJson.json",'r')
json_input = file.read()
request_json = json.loads(json_input)
headers={'Content-type':'application/json', 'Accept':'application/json'}
response = requests.post(url,request_json,headers=headers)
print(request_json)
print(response.content)
"""""

#####PARA PUT###########################################
url = "https://petstore.swagger.io/v2/pet"
file = open("C:\\Users\\jblanco\\Desktop\\Personal\\Baufest Automation\\WebService\\features\\steps\\FormatoJson.json",'r')
json_input = file.read()
request_json = json.loads(json_input)
print(request_json)
headers = {'Content-type':'application/json'}
response = requests.put(url,request_json,headers=headers)
print(response.content)