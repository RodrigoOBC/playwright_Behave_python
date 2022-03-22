from behave import given, when, then, step
from features.data.User import User



@given(u'I am main page')
def step_impl(context):
    assert True


@given(u'went the register page')
def step_impl(context):
    assert True


@when(u'fill the fild with "{name}" s datas')
def step_impl(context,name):
    assert True

@then(u'the mensager "Recebemos os seus dados. Fique de olho na sua caixa de email, pois e em breve retornamos o contato." is displayed')
def step_impl(context):
    assert True
