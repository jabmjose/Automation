- Librerias a tener en cuenta para bajar por pip
Tener instalado Python
- pip install behave
- pip install selenium
- pip install webdriver-manager
- pip install behave allure
- pip install requests
- pip install -U requests
- pip install jsonpath

Comandos:

- behave features\PaginaWeb.feature    (esto para ejecutas el testcase)
- behave -f allure_behave.formatter:AllureFormatter -o reports/ features/PaginaWeb.feature (para ejecutar los casos con los reportes)
- allure serve \C:\Users\jblanco\Desktop\Personal\Baufest Automation\Web\reports