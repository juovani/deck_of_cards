from behave import *
import cards


@Given('I have created a new card object')
def step_impl(context):
    pass


@When('I create the new class')
def step_impl(context):
    new_deck = cards.Deck(52)
    assert new_deck is not None
    context.deck_holder = new_deck


@Then('the number of pips should be recorded')
def step_impl(context):
    assert context.deck_holder.count == 52