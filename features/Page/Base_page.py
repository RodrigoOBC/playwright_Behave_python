from playwright.sync_api import sync_playwright


class BasePage:

    def __init__(self):
        play = sync_playwright().start()
        self.browser = play.chromium.launch(headless=False)

    def page(self):
        return self.browser.new_page()
