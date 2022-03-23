from features.data.User import User
from features.Page.elements_page.register_elements import RegisterLocations


class RegisterPage:
    def __init__(self, Page):
        self.PAGE = Page

    def fill_fields(self, name):
        user = User(name)
        self.PAGE.fill(RegisterLocations().NAME, name)
        self.PAGE.fill(RegisterLocations().CPF, user.get_value("cpf"))
        self.PAGE.fill(RegisterLocations().EMAIL, user.get_value("email"))
        self.PAGE.fill(RegisterLocations().WHATSAPP, user.get_value("whatsapp"))
        self.PAGE.fill(RegisterLocations().POSTAL_CODE, user.get_value("postalcode"))
        self.search_postal_code()
        self.PAGE.fill(RegisterLocations().NUMBER, user.get_value("number"))
        self.PAGE.fill(RegisterLocations().DETAILS, user.get_value("details"))
        self.choose_the_delivery_method(user.get_value("delivery_method"))
        self.upload_CNH(user.get_value("CNH"))

    def send_register(self):
        self.PAGE.click(RegisterLocations().BUTTON_SEND)

    def search_postal_code(self):
        self.PAGE.click(RegisterLocations().BUTTON_SEACHR_CEP)

    def choose_the_delivery_method(self, method):
        if method == "Moto":
            self.PAGE.click(RegisterLocations().DELIVERY_METHOD_MOTO)
        elif method == "Car":
            self.PAGE.click(RegisterLocations().DELIVERY_METHOD_CAR)
        else:
            self.PAGE.click(RegisterLocations().DELIVERY_METHOD_BY)

    def upload_CNH(self, IMG):
        self.PAGE.set_input_files(RegisterLocations().IMAGE,IMG)

    def validate_awaser_confirm(self):
        text = self.PAGE.text_content(RegisterLocations().TEXT_CONFIRM)
        return text