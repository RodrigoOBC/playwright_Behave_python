import asyncio
from playwright.sync_api import sync_playwright
from features.Utils.Utils import Utils
from features.Page.elements_page.amazon_elements import Amazon_Locations


class AmazonPage:
    def __init__(self, Page):
        self.Page = Page
        self.UT = Utils(self.Page)

    def go_to_page(self):
        elemento = self.UT.esperar_elemento_presente(Amazon_Locations().LINK_AMAZON)
        elemento.click()

    def search_Amazon(self, name):
        elemento = self.UT.esperar_elemento_presente(Amazon_Locations().CAIXA_PESQUISA)
        elemento.fill(name)
        elemento.press('Enter')

    def Validate_search(self, text):
        answer = self.UT.esperar_elemento_presente(Amazon_Locations().PESQUISA_RESULTADO)
        assert answer.text_content() == f'"{text}"'

    def screenshot(self, name):
        self.Page.screenshot(path=name, full_page=True)

    def close_brownser(self):
        self.Page.close()
