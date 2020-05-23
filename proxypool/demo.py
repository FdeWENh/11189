import requests
'''
1.部署好代理池
2.打开redis
3.配置好settings
在你的项目中加上这个函数获取代理
'''
def get_proxies(self):
    '''
    从代理池中获取代理
    :return: {}
    '''
    print('开始初始化代理！')
    try:
        proxy = requests.get('http://localhost:5000/get').text
        # print(proxy)
        return {'http': proxy}
    except Exception:
        return None


