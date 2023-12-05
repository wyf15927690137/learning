import requests


def translate(str):
    url = 'http://shsirdlnx2:8888/jenkinsJob/checkChangelist'
    # url = 'http://shsirdlnx2:8888/jenkinsJob/test'
    data = {'p4_port': 'ssl:p4shanghai:2644',
            'job_user': 'yanfeiw',
            'job_change_list': '377409'
            }
    # 将需要post的内容，以字典的形式记录在data内。
    r = requests.post(url, json=data)
    # r = requests.get(url)


translate("this is a test string")
