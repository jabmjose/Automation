Tener instalado Python
Tener instalado Java Enviroment Variables

Librerias a tener en cuenta para bajar por pip
- pip install behave
- pip install selenium
- pip install webdriver-manager
- pip install allure-behave
- pip install allure-pytest
- pip install requests
- pip install -U requests
- pip install jsonpath

Hay un .BAT llamado ejecucion, este ejecutara todos los testcases con informe o sin informe.
Además si el usuario lo desea agregando la ruta donde se generan los reportes (reports)
puede ejecutar allure para visualizarlos

Si se abre desde un IDE (como visual studio) allí mediante Gherkin se puede modificar el feature, para variar los escenarios.


Comandos para ejecutar por separado:

- behave features\WebService.feature    (esto para ejecutas el testcase)
- behave -f allure_behave.formatter:AllureFormatter -o reports/ features/WebService.feature (para ejecutar los casos con los reportes)
- allure serve \C:\Users\jblanco\Desktop\Personal\Baufest Automation\Web\reports
