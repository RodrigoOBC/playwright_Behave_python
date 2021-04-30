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
        answer = self.page.is_visible('text=Facebook – entre ou cadastre-se')
        assert answer
        self.page.close()


if __name__ == '__main__':
    GP = GooglePage()
    GP.go_to_page('https://www.google.com/')
    GP.search_google('facebook')
