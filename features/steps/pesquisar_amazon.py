from behave import given, when, then, step
from features.Page.Base_page import BasePage
from features.Page.google_page import GooglePage
from features.Page.amazon_page import AmazonPage

Page = BasePage().page()
GP = GooglePage(Page)
AP = AmazonPage(Page)


@given('que acesso a pagina do google')
def step_impl(context):
    GP.go_to_page("https://www.google.com/")


@when(u'pesquiso por "Amazon"')
def step_impl(context):
    GP.search_google("Amazon")


@then(u'resultados relacionados ao "Amazon" são exibidos')
def step_impl(context):
    GP.Validate_search()
    GP.screenshot('EvidenciaGoogle.png')


@given(u'que acesso a pagina principal da amazon')
def step_impl(context):
    AP.go_to_page()


@when(u'pesquiso "Livro" na Amazon')
def step_impl(context):
    AP.search_Amazon("Livro")


@then(u'livros vendidos são exibidos')
def step_impl(context):
    AP.Validate_search("Livro")
    AP.screenshot('EvidenciaAmazon.png')
    AP.close_brownser()
