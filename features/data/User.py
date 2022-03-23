class User(object):
    USER_MAP = {
        "Renato Marcos": {
            "cpf": "01793214719",
            "email": "renato-mendes76@reisereis.com.br",
            "whatsapp": "22993211693",
            "postalcode": "28473970",
            "number": "708",
            "details": "s/n",
            "delivery_method": "Moto",
            "CNH": "features/images/upload/cnh-digital.jpg"
        },
        "Mário Pedro": {
            "cpf": "87429760732",
            "email": "mario_assis@dosnu.com.br",
            "whatsapp": "22996852614",
            "postalcode": "28473970",
            "number": "889",
            "details": "teste",
            "delivery_method": "Moto",
            "CNH": "features/images/upload/cnh-digital.jpg"
        },
        "CPF_invalido": {
            "cpf": "874297607A2",
            "email": "mario_assis@dosnu.com.br",
            "whatsapp": "22996852614",
            "postalcode": "28473970",
            "number": "889",
            "details": "teste",
            "delivery_method": "Moto",
            "CNH": "features/images/upload/cnh-digital.jpg"
        },
        "email_invalido": {
            "cpf": "87429760732",
            "email": "mario_assisdosnu.com.br",
            "whatsapp": "22996852614",
            "postalcode": "28473970",
            "number": "889",
            "details": "teste",
            "delivery_method": "Moto",
            "CNH": "features/images/upload/cnh-digital.jpg"
        }
    }

    def __init__(self, user):
        self.user = user

    def get_value(self, attribute):
        return self.USER_MAP[self.user].get(attribute,'erro')


if __name__ == '__main__':
    usuario = User("Renato Marcos")
    print(usuario.get_value("cpf"))