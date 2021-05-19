import asyncio
from playwright.sync_api import sync_playwright
from .Base_page import BasePage
from features.Page.elements_page.google_elements import google_locations


class GooglePage:
    def __init__(self, Page):
        self.Page = Page

    def go_to_page(self, url):
        self.Page.goto(url)

    def search_google(self, name):
        self.Page.fill(google_locations().CAMPO_BUSCA, name)
        self.Page.press(google_locations().CAMPO_BUSCA, "Enter")

    def Validate_search(self):
        answer = self.Page.wait_for_selector(google_locations().TEXTO_RESULTADO, timeout=10000,
                                             state="visible")
        assert answer

    def screenshot(self, name):
        self.Page.screenshot(path=name, full_page=True)

    def close_brownser(self):
        self.Page.close()
