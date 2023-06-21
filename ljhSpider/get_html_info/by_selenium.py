import undetected_chromedriver as uc
from undetected_chromedriver.options import ChromeOptions
from ljhSpider.api_functions.header_api import header
import platform


class SeleniumOri:
    def __init__(
        self,
        headless_enable=False,
        plugin_enable=False,
        logging_enable=False,
        incognito_enable=False,
        detach_enable=False,
        stealth_enable=False,
    ):
        self.options = ChromeOptions()
        if headless_enable:
            self.options.add_argument("--headless")
        if plugin_enable:
            self.options.add_argument("--disable-images")
            self.options.add_argument("--disable-plugins")
            self.options.add_argument("disable-audio")
            self.options.add_argument("disable-translate")
        # if proxy:
        #     print(1)
        if logging_enable:
            self.options.add_argument("log-level=3")
        if incognito_enable:
            self.options.add_argument("--incognito")
        if detach_enable:
            self.options.add_experimental_option("detach", True)
        if platform.system().lower() == "linux":
            self.options.add_argument("--headless")
            self.options.add_argument("--no-sandbox")
            self.options.add_argument("--disable-gpu")
            self.options.add_argument("--disable-dev-shm-usage")

        self.options.add_argument("user-agent={}".format(header()["User-Agent"]))
        self.driver = uc.Chrome(options=self.options)
        if stealth_enable:
            self.stealth_enable()

    def stealth_enable(self):
        with open("stealth.min.js", "r", encoding="utf-8") as file:
            stealth_min_js = file.read()
        self.browser.execute_cdp_cmd(
            "Page.addScriptToEvaluateOnNewDocument", {"source": stealth_min_js}
        )

    def get(self, url):
        self.driver.get(url)

    def quit(self):
        self.driver.quit()
