# Automation
Automatizaciones

1.- Web

Existen 3 carpetas:

- features 
	-PaginaWeb.feature (Aca estan los testcase escritos en Gherkin con sus respectivos escenarios)
	-steps
		-PaginaSteps.py (Aca se encuentran las acciones a realizar enlazadas al feature anterior)
-reports
	Aca van los reportes generados si se hace el llamado del comando para los mismos , considerar vaciar si existen a la hora de hacer una nueva ejecución
	
-venv
	Aca estan las libreriar que se utilizan desde Python
	
Adicionalmente , se deja un archivo BAT (Ejecución.BAT) para realizar la ejecución del TestCase completo
Tambien se deja la carpeta de Allure dónde se encuentra el archivo y librerias para ejecutar el comando
Existe un ReadMe.txt con las librerias a tener en cuenta y los comando a utilizar si se desea ejecutar manualmente

2.- WebService

Existen 3 carpetas:

- features
	-WebService.feature(Aca estan los testcase escritos en Gherkin con sus respectivos escenarios)
	-steps
		-FormatoJsonPOST.json (datos del request para realizar el POST)
		-FormatoJsonPUT.json (datos del request para realizar el PUT)
		-GETSteps.py ( Aca se encuentran las acciones a realizar enlazadas al feature para el Scenario de GET)
		-PUTSteps.py ( Aca se encuentran las acciones a realizar enlazadas al feature para el Scenario de PUT)
		-POSTSteps.py ( Aca se encuentran las acciones a realizar enlazadas al feature para el Scenario de POST)
-reports 
	Aca van los reportes generados si se hace el llamado del comando para los mismos , considerar vaciar si existen a la hora de hacer una nueva ejecución

-venv
	Aca estan las libreriar que se utilizan desde Python
	
Adicionalmente , se deja un archivo BAT (Ejecución.BAT) para realizar la ejecución del TestCase completo
Tambien se deja la carpeta de Allure dónde se encuentra el archivo y librerias para ejecutar el comando
Existe un ReadMe.txt con las librerias a tener en cuenta y los comando a utilizar si se desea ejecutar manualmente
