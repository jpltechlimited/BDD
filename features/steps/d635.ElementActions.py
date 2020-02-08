from behave import *


@step('Click on ribbon button "{display_name}"')
def step_impl(context, display_name):
    context.d365Client.ribbon_click_on_button(display_name)
