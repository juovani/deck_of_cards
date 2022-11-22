Feature: testing all domino classes
  Scenario: test that pips are recorded correctly
    Given I have created a new card object
    When I create the new class
    Then the number of pips should be recorded