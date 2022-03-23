from behave import given, when, then, step
import time
from features.Page.Base_page import BasePage
from features.Page.utils import Utils
from unittest import TestCase
from features.Page.home_page import HomePage
from features.Page.register_page import RegisterPage

Page = BasePage().page()


@given(u'I am main page')
def step_impl(context):
    Utils(Page).go_to_page('https://buger-eats.vercel.app/')
    TestCase().assertEqual(HomePage(Page).validate_home_page(), "Seja um parceiro entregador pela Buger Eats")


@given(u'went the register page')
def step_impl(context):
    HomePage(Page).click_register()
    TestCase().assertEqual(HomePage(Page).validate_register_page(), "Cadastre-se para  fazer entregas")


@when(u'fill the fild with "{name}" datas')
def step_impl(context, name):
    RegisterPage(Page).fill_fields(name)
    RegisterPage(Page).send_register()


@then(
    u'the mensager "Recebemos os seus dados. Fique de olho na sua caixa de email, pois e em breve retornamos o contato." is displayed')
def step_impl(context):
    TestCase().assertEqual(RegisterPage(Page).validate_awaser_confirm(),
                           "Recebemos os seus dados. Fique de olho na sua caixa de email, pois e em breve retornamos o contato.")
