# 百度图片下载

## 简介
通过用户ID爬取用户所有投稿视频信息

本程序所采集用户ID为B站UP主[交通事故video](https://space.bilibili.com/28152409/video) 

**宣扬礼让行车正能量&&不规范行车造成的交通事故**

**道路千万条，安全第一条。开车不规范，亲人两行泪。**


## 编写思路
1. 通过Chrome的[Elements](https://developers.google.com/web/tools/chrome-devtools/css/)和[Network](https://developers.google.com/web/tools/chrome-devtools/network/)分析可知：请求用户全部视频时会通过

   ```html
https://image.baidu.com/search/acjson?tn=resultjson_com&catename=pcindexnew&ipn=rj&ct=201326592&is=&fp=result&queryWord=&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&word=python&face=0&istype=2&qc=&nc=1&fr=&pn=0&rn=30
   ```

   其中**word**为搜索关键字，**rn**为请求返回的图片数**[每页返回的图片数量，可设上限值为60]**，并且可以通过测试可知**pn的关系**如下：
```html
   ∵第一页pn为0
   ∵第二页pn为30
   ∵第三页pn为60

   ∴f(n) = f(n-1)*30
```



2. 遍历返回的json数据，可以获取图片的**weight**和**height**属性
   
3. 直接通过**搜索的关键字**建立新的目录并存放于程序运行的当前目录

4. 请求的图片通过```random.randint(1000000,9999990)```和```time.time()```组合命名防止重复**[懒]**


## 使用教程
1.在main中填写用户id和爬取的线程数

```python
     # 设置搜索关键字
    search_work = 'apple'

    # 设置需要下载图片的页数
    pages = 3
```

>**注意**
>
>>此处没做异常处理



## 功能

* [x] 通过用户输入关键字自动下载图片
* [x] 下载的图片数量可控



## 完整代码
完整版源代码存放在[github](https://github.com/Bqrookie/project)上，有需要的可以下载
项目持续更新，欢迎您[star本项目](https://github.com/Bqrookie/project)

## Lincense
 [The MIT License (MIT)](http://opensource.org/licenses/MIT)

