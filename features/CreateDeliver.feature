Feature: Create Deliver
  I'm user and want to register a new user
  and validate behave's fields



  Background:
    Given I am main page
    And went the register page

  @RegisterDeliver
  Scenario Outline: Register a new deliver
    When fill the fild with "<name>" datas
    Then the mensager "Recebemos os seus dados. Fique de olho na sua caixa de email, pois e em breve retornamos o contato." is displayed
    Examples:
      | name          | CPF         | email                            | whatsapp    | postalcode | number | details | delivery_method | CNH |
      | Renato Marcos | 01793214719 | renato-mendes76@reisereis.com.br | 22993211693 | 28473970   | 708    | s/n     | Moto            |     |
      | Mário Pedro   | 87429760732 | mario_assis@dosnu.com.br         | 22996852614 | 28473970   | 889    | teste   | Moto            |     |

