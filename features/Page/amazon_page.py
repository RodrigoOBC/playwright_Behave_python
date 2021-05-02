import asyncio
from playwright.sync_api import sync_playwright


class AmazonPage:
    def __init__(self, Page):
        self.Page = Page

    def go_to_page(self):
        self.Page.click('text=Amazon.com.br - Tudo para você de A a Z')

    def search_Amazon(self, name):
        self.Page.fill('input[id="twotabsearchtextbox"]', name)
        self.Page.press('input[id="twotabsearchtextbox"]', 'Enter')

    def Validate_search(self,text):
        answer = self.Page.text_content('span[class="a-color-state a-text-bold"]', timeout=10000)
        assert answer == f'"{text}"'

    def screenshot(self, name):
        self.Page.screenshot(path=name, full_page=True)

    def close_brownser(self):
        self.Page.close()
