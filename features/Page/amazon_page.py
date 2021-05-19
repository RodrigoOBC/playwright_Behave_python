import asyncio
from playwright.sync_api import sync_playwright
from features.Page.elements_page.amazon_elements import Amazon_Locations

class AmazonPage:
    def __init__(self, Page):
        self.Page = Page

    def go_to_page(self):
        self.Page.click(Amazon_Locations().LINK_AMAZON)

    def search_Amazon(self, name):
        self.Page.fill(Amazon_Locations().CAIXA_PESQUISA, name)
        self.Page.press(Amazon_Locations().CAIXA_PESQUISA, 'Enter')

    def Validate_search(self,text):
        answer = self.Page.text_content(Amazon_Locations().PESQUISA_RESULTADO, timeout=10000)
        assert answer == f'"{text}"'

    def screenshot(self, name):
        self.Page.screenshot(path=name, full_page=True)

    def close_brownser(self):
        self.Page.close()
