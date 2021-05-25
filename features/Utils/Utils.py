class Utils:
    def __init__(self, Page):
        self.page = Page

    def esperar_elemento_clicavel(self, element, timeout=10000):
        pass

    def esperar_elemento_presente(self, element, timeout=10000):
        return self.page.wait_for_selector(selector=element, timeout=timeout)

    def esperar_elemento_visivel(self, element, timeout=10000):
        return self.page.wait_for_selector(selector=element, timeout=timeout, state="visible")

    def esperar_elemento_invisivel(self, element, timeout=10000):
        pass

    def Validar_URL(self, url, timeout=10000):
        pass

    def scroll_to_element(self, element):
        pass

    def scroll_Up_To_Element(self, element):
        pass

    def scroll_Left_To_Element(self, element):
        pass
