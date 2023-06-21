from gne import GeneralNewsExtractor


class ParseNews:
    def __init__(self):
        self.extractor = GeneralNewsExtractor()

    def parse(self, html):
        result = self.extractor.extract(html)
        return result
