from behave import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

@given(u'Abrir Explorador Chrome')
def AbrirExplorador(self):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"]) #Se agrega debido a que no se corre como admin asi no tira error por cmd
    self.driver = webdriver.Chrome(ChromeDriverManager().install(),options=options) #Colocar la ruta dónde esta el webdriver de chrome

@when(u'Abrir demoblaze Pagina')
def AbrirPagina(context):
    context.driver.get("https://www.demoblaze.com/index.html")
    context.driver.maximize_window()
    time.sleep(3)


@then(u'Cerrar Pagina')
def CerrarPagina(context):
    context.driver.close()
    context.driver.quit()


@then(u'Dar de alta usuario "{nombre}" y contraseña "{clave}"')
def DarAltaUsuario(context,nombre,clave):
    context.signin2 = context.driver.find_element_by_id("signin2")
    context.signin2.click()
    time.sleep(3)

    context.signusername = context.driver.find_element_by_id("sign-username")
    context.signusername.send_keys(nombre)
    time.sleep(3)

    context.signpassword = context.driver.find_elements_by_id("sign-password")
    context.signpassword[0].send_keys(clave)
    time.sleep(3)

    context.singup = context.driver.find_element_by_xpath("/html/body/div[2]/div/div/div[3]/button[2]")
    context.singup.click()
    time.sleep(2)
    try:
        if context.singup.text == "This user already exist.":
            print("")

    except:
        pass

@then('Loguear "{user}" "{password}"')
def Logueo(context,user,password):
    context.login2 = context.driver.find_element_by_id("login2")
    context.login2.click()
    time.sleep(3)
    context.loginusername = context.driver.find_elements_by_id("loginusername")
    context.loginusername[0].send_keys(user)
    time.sleep(3)
    context.loginpassword = context.driver.find_elements_by_id("loginpassword")
    context.loginpassword[0].send_keys(password)
    time.sleep(3)
    context.Logueo = context.driver.find_element_by_xpath("/html/body/div[3]/div/div/div[3]/button[2]")
    context.Logueo.click()
    time.sleep(5)

@then('Desloguear')
def Deslogueo(context):
    context.Logout = context.driver.find_elements_by_id("logout2")
    context.Logout[0].click()
    time.sleep(3)

@then('Comprar Laptop')
def ComprarLaptop(context):
    context.producto = context.driver.find_elements_by_css_selector("#tbodyid > div:nth-child(9) > div > div > h4 > a")
    context.producto[0].click()
    time.sleep(3)
    context.click_add = context.driver.find_elements_by_css_selector("#tbodyid > div.row > div > a")
    context.click_add[0].click()
    try:
        if context.click_add[0].text == "Product added":
            print("Se agregó correctamente")

    except:
        pass

@then('Verificar Carrito')
def VerificarCarrito(context):
    context.cart = context.driver.find_element_by_xpath("/html/body/nav/div/div/ul/li[4]/a")
    context.cart.click()
    time.sleep(6)

