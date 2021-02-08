Feature: WebService
  Scenario: POST para dar de alta mascota
    Given Verificamos existencia de Json para POST
    Then Obtenemos una respuesta igual a "200" de "https://petstore.swagger.io/v2/pet/"

  Scenario: GET de Mascota existente
    Given Verificar Respuesta GET de "https://petstore.swagger.io/v2/pet/" con ID "3"
    Then Obtenemos una respuesta igual a "200" de "https://petstore.swagger.io/v2/pet/" con ID "3"

  Scenario: PUT de Mascota existente
    Given Verificamos existencia de Json para PUT
    Then Obtenemos una respuesta igual a "200" de "https://petstore.swagger.io/v2/pet/" para PUT