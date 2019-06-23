# 谷歌翻译小工具

## 简介
谷歌翻译小工具

## 编写思路
1. 通过读取谷歌翻译的接口来编写的 

## 使用教程
Translation类默认中译英，英译中需要带参数
```python
class Translation:

    def __init__(self, query, flag=False):
        """
        默认就是中文翻译成英文
        :param query: 翻译的文字
        :param flag: False就是中译英 True就是英译中
        """
        # 默认就是中文=>英文
        self.flag = flag
        self.query = query
```

## 功能

* [x] 中英互译【其他语种的已经备份好，随时可以添加】

    ```sl=en 需要翻译的语种  tl=zh-CN 目标语种 tkk参数采用大神写好的加密脚本```

## 补充
* [ ] 多语种翻译和gui没做

## 完整代码
完整版源代码存放在[github](https://github.com/Bqrookie/project)上，有需要的可以下载
项目持续更新，欢迎您[star本项目](https://github.com/Bqrookie/project)

## Lincense
 [The MIT License (MIT)](http://opensource.org/licenses/MIT)

