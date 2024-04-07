import yaml
from common import contants
import json
 # 用python读取yaml文件，先用open方法读取文件数据，再通过load方法转成字典，这个load跟json里面的load是相似的
class read_config:
    #读取启动模拟器配置参数
    def get(self):
      #读取配置文件内容并且转换成字典
     re=open(contants.conf_yaml,encoding='utf-8')
     res=yaml.load(re.read(),Loader=yaml.Loader)
     return res

    #获取driver
    def drives(self):
        re = open(contants.drivers, encoding='utf-8')
        res = yaml.load(re.read(), Loader=yaml.Loader)
        return res

re=read_config().get()
print(re)






