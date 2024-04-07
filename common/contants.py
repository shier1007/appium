import os

#获取根目录位置
base_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#获取conf的路径
conf=os.path.join(base_dir,'conf')
#获取conf.yaml的路径
conf_yaml=os.path.join(conf,'conf.yaml')
drivers=os.path.join(conf,'dri_conf.yaml')

#获取data的路径
datas=os.path.join(base_dir,'data')
case=os.path.join(datas,'cases.xlsx')

test=os.path.join(base_dir,'testcase')

report_dir=os.path.join(base_dir, 'reports') # reports文件夹路径
reports_html = os.path.join(report_dir, 'reports.html')  # reports文件夹路径