import requests
from lxml import etree
class ProxyMetaclass(type):
    def __new__(cls, name,bases,attrs):
        '''
        这里是一个元类实现一个存放所有爬取免费代理方法的方
        法名字的列表
        '''
        attrs['__CrwalFunc__'] = []
        count = 0
        for k,v in attrs.items():
            if 'crawl_' in k:
                attrs['__CrwalFunc__'].append(k)
                count +=1
        attrs['__CrwalCount__'] = count
        return type.__new__(cls,name,bases,attrs)


class FreeProxyGetter(object,metaclass=ProxyMetaclass):

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36',
    }
    def get_raw_proxies(self,callback):
        '''
        通过传入一个字符串的方法名，来调用这个方法，获取代理
        :param callback: 方法名的字符串格式--crawl_66ip
        :return: list-->代理
        '''
        proxies = []
        for proxy in eval('self.{}()'.format(callback)):
            proxies.append(proxy)
        return proxies

    # !!!爬取代理方法，名称统一为crawl_
    def crawl_66ip(self):
        '''
        url:http://www.66ip.cn/
        :return:list[proxy]
        '''
        proxies = []
        base_url = 'http://www.66ip.cn/%s.html'
        for i in range(1, 20):
            response = requests.get(base_url % i, headers=self.headers)
            html = etree.HTML(response.text)
            ips = html.xpath('//tr[position()>1]/td[1]/text()')
            ports = html.xpath('//tr[position()>1]/td[2]/text()')
            if len(ips) == len(ports) and ips and ports:
                for i, ip in enumerate(ips):
                    port = ports[i]
                    yield ip.strip()+':'+port.strip()
    def crawl_ip3366(self):
        '''
        url:http://www.ip3366.net/?stype=1&page=1
        :return: list[proxy]
        '''
        proxies = []
        base_url = 'http://www.ip3366.net/?stype=1&page=%s'
        for i in range(1, 11):
            response = requests.get(base_url % i, headers=self.headers)
            html = etree.HTML(response.text)
            ips = html.xpath('//tr/td[1]/text()')
            ports = html.xpath('//tr/td[2]/text()')
            if len(ips) == len(ports) and ips and ports:
                for i, ip in enumerate(ips):
                    port = ports[i]
                    # print(ip,port)
                    # proxies.append(ip.strip()+':'+port.strip())
                    yield ip.strip() + ':' + port.strip()
if __name__ == '__main__':
    f = FreeProxyGetter()
    print(f.__CrwalFunc__)
