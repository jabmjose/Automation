- Librerias a tener en cuenta para bajar por pip
- behave
- selenium
- behave allure

Comandos:

- behave features\PaginaWeb.feature    (esto para ejecutas el testcase)
- behave -f allure_behave.formatter:AllureFormatter -o reports/ features/PaginaWeb.feature (para ejecutar los casos con los reportes)
- allure serve \C:\Users\jblanco\Desktop\Personal\Baufest Automation\Web\reports