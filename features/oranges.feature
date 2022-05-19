Feature: Orange Basket
    As a farmer,
    I want to carry oranges in a basket,
    So that I do not drop them all.

Scenario Outline: Add oranges to a basket
    Given the basket has <start> oranges
    When <more> oranges are added to the basket
    Then the basket contains <final> oranges

    Examples:
        | start | more | final |
        | 2 | 4 | 6 |
        | 3 | 5 | 8 |
        | 5 | 5 | 10 |

Scenario Outline: Remove oranges from a basket
    Given the basket has <start> oranges
    When <some> oranges are removed from the basket
    Then  the basket contains <final> oranges

    Examples:
        | start | some | final |
        | 6  | 2  | 4  |
        | 8 | 4 | 4 |

