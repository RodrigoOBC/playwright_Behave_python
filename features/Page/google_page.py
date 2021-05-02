import asyncio
from playwright.sync_api import sync_playwright
from .Base_page import BasePage


class GooglePage:
    def __init__(self, Page):
        self.Page = Page

    def go_to_page(self, url):
        self.Page.goto(url)

    def search_google(self, name):
        self.Page.fill('input[name="q"]', name)
        self.Page.press('input[name="q"]', "Enter")

    def Validate_search(self):
        answer = self.Page.wait_for_selector('text=Amazon.com.br - Tudo para você de A a Z', timeout=30000,
                                             state="visible")
        assert answer

    def screenshot(self, name):
        self.Page.screenshot(path=name, full_page=True)

    def close_brownser(self):
        self.Page.close()
