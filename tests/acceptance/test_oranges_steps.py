"""Orange Basket feature tests."""

from pytest_bdd import (
    given,
    scenarios,
    then,
    when,
    parsers
)

from project.oranges import OrangeBasket

scenarios('../../features/oranges.feature')
def test_oranges_to_a_basket():
    """Add oranges to a basket."""


@given(parsers.parse('the basket has {initial:d} oranges'), target_fixture='basket')
def the_basket_has_2_oranges(initial):
    basket = OrangeBasket(initial_count=initial)
    return basket


@when(parsers.parse('{more:d} oranges are added to the basket'))
def oranges_are_added_to_the_basket(basket, more):
    """4 oranges are added to the basket."""
    basket.add(more)

@when(parsers.parse('{some:d} oranges are removed from the basket'))
def oranges_are_removed(basket, some):
    basket.remove(some)

@then(parsers.parse('the basket contains {final:d} oranges'))
def the_basket_contains_6_oranges(basket, final):
    """the basket contains 6 oranges."""
    assert basket.count == final
