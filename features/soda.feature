Feature: soda
Pay coins to withdraw food

Scenario: one soda
    Given 2 coins are added
    When I withdraw a soda
    Then I receive a soda

Scenario: discount1
    Given 4 coins are added
    When I withdraw 1 soda; 1 fruits
    Then I receive 1 soda; 1 fruit

Scenario: discount2
    Given 4 coins are added
    When I withdraw 1 fruits; 1 muesli
    Then I receive 1 fruit; 1 muesli

Scenario: withdrawal
    Given 3 coins are added
    When I return coins
    Then I receive coins
