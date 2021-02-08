@echo Opcion a ejecutar
:Menu
@echo 1. TesCase sin reporte
@echo 2. Tescase con reporte
@echo 3. Salir
@set /p var=
@echo off
if %var%==1 goto :Primero
if %var%==2 goto :Segundo
if %var%==3 goto :Salir
if %var% GTR 3 echo Error
goto :Menu
:Primero
cls 
@echo Se ejecuta TestCase sin reporte
behave features\WebService.feature
goto :Menu
:Segundo
cls 
@echo Se ejecuta TestCase con reporte
behave -f allure_behave.formatter:AllureFormatter -o reports/ features/WebService.feature
@echo Reportes generado en la carpeta reports
goto :Menu
:Salir
@echo Saliendo..
