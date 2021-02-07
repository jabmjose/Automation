Feature: Prueba Sitio Web
  Scenario: Apertura de Pagina
    Given Abrir Explorador Chrome
    When Abrir demoblaze Pagina
    Then Cerrar Pagina

  Scenario: Dar de alta
    Given Abrir Explorador Chrome
    When Abrir demoblaze Pagina
    Then Dar de alta usuario "123" y contraseña "123"
    Then Cerrar Pagina

  Scenario: Logueo y Deslogueo
    Given Abrir Explorador Chrome
    When Abrir demoblaze Pagina
    Then Loguear "1234" "1234"
    Then Desloguear
    Then Cerrar Pagina

  Scenario: Dar de alta producto y verificar
    Given Abrir Explorador Chrome
    When Abrir demoblaze Pagina
    Then Loguear "1234" "1234"
    Then Comprar Laptop
    Then Verificar Carrito
    Then Cerrar Pagina
