from behave import given, when, then, step
from features.Page.google_page import GooglePage

GP = GooglePage()

@given('que estou na pagina inicial do google')
def step_impl(context):
    GP.go_to_page("https://www.google.com/")

@when('O usuario digita "Facebook" na caixa de pesquisa e aperta ENTER')
def step_impl(context):
    GP.search_google("Facebook")


@then('resultados relacionados ao "Facebook" são exibidos')
def step_impl(context):
    GP.Validate_search()
