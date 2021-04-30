import asyncio
from playwright.sync_api import sync_playwright


class GooglePage:
    def __init__(self):
        playwright = sync_playwright().start()
        self.browser = playwright.chromium.launch(headless=False)
        self.page = self.browser.new_page()

    def go_to_page(self, url):
        self.page.goto(url)

    def search_google(self, name):
        self.page.fill('input[name="q"]', name)
        self.page.click('input[value="Pesquisa Google"]')

    def Validate_search(self):
        answer = self.page.wait_for_selector('text=Facebook – entre ou cadastre-se',timeout=30000,state="visible")
        assert answer
        self.page.close()
