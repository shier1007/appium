from common.config import read_config
import threading
from appium import webdriver
class DriverUtil(object):
    '''driver工具类'''

    __instance = None   # 定义一个类属性
    __instance_lock = threading.Lock()  # 加锁

    @classmethod
    def get_driver(cls):
        '''获取driver'''
        with DriverUtil.__instance_lock:
            if not DriverUtil.__instance:
                cls.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', read_config().get())
                return cls.driver
        return DriverUtil.__instance


