# wifiRecord

## 简介
手上有几个wifi账号，写着txt感觉不方便，所以写了一个小工具，专门处理wifi的，其实也就是增删改查

## 编写思路
1. wifi资料入库
2. 通过gui来操作

## 技术路线
* tkinter
* ttk

## 使用教程
根据自己情况修改```db_sql.py```里面的```init_config```配置即可，数据库可以使用```wps.sql```生成[因为还没看到数据库，感觉好乱]
```python
def init_config():
    config = {
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'root',
        'passwd': 'root',
        'db': 'wps',
        'charset': 'utf8',
    }

    db = MySQLdb.connect(host=config['host'],
                         port=config['port'],
                         user=config['user'],
                         passwd=config['passwd'],
                         db=config['db'],
                         charset=config['charset']
                         )

    return db
````
## 功能
* [x] 通过gui对wifi资料增删改查

## 完整代码
完整版源代码存放在[github](https://github.com/Bqrookie/project)上，有需要的可以下载
项目持续更新，欢迎您[star本项目](https://github.com/Bqrookie/project)

## Lincense
 [The MIT License (MIT)](http://opensource.org/licenses/MIT)

