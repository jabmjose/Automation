@echo Opcion a ejecutar
:Menu
@echo 1. TesCases sin reporte
@echo 2. Tescases con reporte
@echo 3. Ver reporte mediante Allure
@echo 4. Salir
@set /p var=
@echo off
if %var%==1 goto :Primero
if %var%==2 goto :Segundo
if %var%==3 goto :Tercero
if %var%==4 goto :Salir
if %var% GTR 4 echo Error
goto :Menu
:Primero
cls 
@echo Se ejecuta TestCases sin reporte
behave features\WebService.feature
goto :Menu
:Segundo
cls 
@echo Se ejecuta TestCases con reporte
behave -f allure_behave.formatter:AllureFormatter -o reports/ features/WebService.feature
@echo Reportes generado en la carpeta reports
goto :Menu
:Tercero
cls 
@echo Se ejecuta Allure para visualizar reporte ingresa ruta de reporte:
@set /p ruta=
allure serve \ %ruta%
@echo Reportes generado en la carpeta reports
goto :Menu
:Salir
@echo Saliendo..
