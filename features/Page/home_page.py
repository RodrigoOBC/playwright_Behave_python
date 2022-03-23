import asyncio
from playwright.sync_api import sync_playwright
from .Base_page import BasePage
from features.Page.elements_page.home_page import homePage


class HomePage:
    def __init__(self, Page):
        self.Page = Page

    def click_register(self):
        self.Page.click(homePage.BUTTON_REGISTER)

    def validate_home_page(self):
        text = self.Page.text_content(homePage.TEXT_HOME)
        return text

    def validate_register_page(self):
        text = self.Page.text_content(homePage.TEXT_REGISTER)
        return text



    def close_brownser(self):
        self.Page.close()
