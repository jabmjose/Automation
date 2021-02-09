Feature: Prueba Sitio Web
  Scenario: Apertura de Pagina
    Given Abrir Explorador Chrome
    When Abrir demoblaze Pagina
    Then Cerrar Pagina

  Scenario: Dar de alta
    Given Abrir Explorador Chrome
    When Abrir demoblaze Pagina
    Then Dar de alta usuario "Sabueso" y contraseña "Sabueso"
    Then Cerrar Pagina

  Scenario: Logueo y Deslogueo
    Given Abrir Explorador Chrome
    When Abrir demoblaze Pagina
    Then Loguear "Sabueso" "Sabueso"
    Then Desloguear
    Then Cerrar Pagina

  Scenario: Dar de alta producto y verificar
    Given Abrir Explorador Chrome
    When Abrir demoblaze Pagina
    Then Loguear "Sabueso" "Sabueso"
    Then Comprar Laptop
    Then Verificar Carrito
    Then Cerrar Pagina
