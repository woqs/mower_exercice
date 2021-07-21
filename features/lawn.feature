Feature: lawn some file

  Scenario Outline: I lawn
    Given I have a file with
      | boundaries   | starting_position   | directions   |
      | <boundaries> | <starting_position> | <directions> |
    When I run the program
    Then I should have <result> as a result

    Examples:
      | boundaries | starting_position | directions | result |
      | 5 5        | 1 2 N             | GAGAGAGAA  | 1 3 N  |
      | 5 5        | 3 3 E             | AADAADADDA | 5 1 E  |
