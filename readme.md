```
______                        ______             _
| ___ \_                      | ___ \           | |
| |_/ / \__ __   __  _ __   _ | |_/ /___   ___  | |
|  __/|  _// _ \ \ \/ /| | | ||  __// _ \ / _ \ | |
| |   | | | (_) | >  < \ |_| || |  | (_) | (_) || |___
\_|   |_|  \___/ /_/\_\ \__  |\_|   \___/ \___/ \_____\
                       __ / /
                      /___ /
```

### 使用

　　启动过几分钟后就能看到抓取到的代理IP,通过api访问[http://127.0.0.1:5000](http://127.0.0.1:5000/) 查看。

- 爬虫使用

　　如果要在爬虫代码中使用的话， 可以将此api封装成函数直接使用,如demo.py



### 目录说明

- getter：爬取免费代理

- db：代理池(redis存储)

- API：通过网络端口的形式对外提供调用(此处用flask)

- settings : 各种配置

- Scheduler：校验爬取的代理并添加到代理池 
