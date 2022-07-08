import requests


def translate(str):
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rul'  # 链接
    data = {'i': str,
            # 'from': 'AUTO',
            # 'to': 'AUTO',
            # 'smartresult': 'dict',
            # 'client': 'fanyideskweb',
            'doctype': 'json',
            # 'version': '2.1',
            # 'keyfrom': 'fanyi.web',
            # 'action': 'FY_BY_REALTIME',
            # 'typoResult': 'false'
            }
    # 将需要post的内容，以字典的形式记录在data内。
    r = requests.post(url, data=data)
    print('---------------------')
    print(r)
    print('---------------------')
    # post需要输入两个参数，一个url，一个是data，返回的是一个Response对象
    answer = r.json()  # 转型

    print('---------------------')
    print(answer)
    print('---------------------')

    result = answer['translateResult'][0][0]['tgt']  # 筛选
    print(" Translate the input:" + str + " The translation is:" + result + '\n')


translate("我还不如跟石像聊天呢！")
