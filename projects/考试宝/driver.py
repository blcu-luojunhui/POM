import time

from selenium.webdriver.common.by import By
from ljhSpider.auto_browser import by_selenium


class TestDriver:
    def __init__(self):
        self.browser = by_selenium.SeleniumOri(
            plugin_enable=True,
            incognito_enable=True,
            headless_enable=True
        )

    def init_browser(self, url):
        self.browser.get(url)
        time.sleep(1)
        self.browser.driver.find_element(By.XPATH, r'//p[@class="clearfix"]//span[@class="el-switch__core"]').click()



