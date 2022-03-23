

class Utils(object):
    def __init__(self,Page):
        self.Page = Page

    def go_to_page(self, url):
        self.Page.goto(url)