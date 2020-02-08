from behave import *


@step('I navigate to "{area}" "{subarea}"')
def step_impl(context, area, subarea):
    context.d365Client.navigate_to_subarea(area, subarea)


@step('Select view "{view}"')
def step_impl(context, view):
    context.d365Client.navigate_switch_to_view(view)
