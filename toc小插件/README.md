# 百度图片下载

## 简介
发现github的markdown语法不会自动生成目录，就自己写了一个很粗糙的

## 编写思路
1. 通过读取md文件，统计```#```的数量
2. 通过字符串拼接来生成目录格式  

## 使用教程
1.在main中填写用户id和爬取的线程数

```python
   with open('your.md', 'rb') as f:
    content = f.readlines()
```

>**注意**
>
>>全部都没做异常处理

## 功能

* [x] 很粗糙的生成目录格式

## 补充
* [ ] Gui
* [ ] 文件备份、撤销功能

## 完整代码
完整版源代码存放在[github](https://github.com/Bqrookie/project)上，有需要的可以下载
项目持续更新，欢迎您[star本项目](https://github.com/Bqrookie/project)

## Lincense
 [The MIT License (MIT)](http://opensource.org/licenses/MIT)

