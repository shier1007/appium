from appium import webdriver
from common.config import read_config

class appiumdriver:
    #定义一个空得driver
    driver=None

    @classmethod
    def get_driver(self):
        try:
            if self.driver is None:
                #启动APP，定义一个driver
                self.driver=webdriver.Remote(read_config().drives(),read_config().get())
        except AssertionError as e:
                self.driver = webdriver.Remote(read_config().drives(), read_config().get())
        return self.driver