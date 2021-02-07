Feature: WebService
  Scenario: POST para dar de alta mascota
    Given Verificamos existencia de Json

  Scenario: GET de Mascota existente
    Given Verificar Respuesta GET de "https://petstore.swagger.io/v2/pet/" con ID "3"
    Then Obtenemos una respuesta igual a "200" de "https://petstore.swagger.io/v2/pet/" con ID "3"