# -*- coding: utf-8 -*-
import re


ss = '''【<p>更新:    老婆还是发现了，已挨揍，干脆取匿了</p><p>以下原答案</p><p>不敢不匿，老婆看到会打死我。</p><p>我老婆开车十余年了，近年在我调教下，其实也算不错，除了一些改不了的固有顽疾，还除了平均每年一定要搞一起以上的事故。</p><p>她喜欢开小车，不喜欢开大车。曾经买过最小的车子是smart，就从这里说起吧。有一次她开smart在我前边，我开我车在后面跟着，在车道上正常行驶，这时右边车道一辆雅阁向左变道，也是个愣货，我眼看着他的车从我老婆的车前轮位置一直擦到最后，老婆的小车子从我的角度都已经明显看出来挤得直晃，车子轻嘛。我就在后面一直按喇叭，那个雅阁看到蹭了，就回到了原车道继续开，压根也没停的意思，最神奇的是！我老婆也没停，还开的挺快，眼看就没影了，我赶紧给老婆打电话，打了几个也不接，我在后面实在无奈，追上去把那雅阁别停了。可是别停了以后咋弄啊，天还下着雨我也不愿意下车处理，后面堵了一串车，现场也没有，当事人都没影了，那会也没有行车记录仪，当时脑子都快炸了，被我老婆气的，只能降窗户把那个雅阁骂了一顿，赶紧追老婆去。这期间一直不接电话，半小时后到了地方一问，人压根不知道车子刮擦了，我当时真是，唉，说多了又会被骂，自己憋得特想给自己一刀。</p><p>这些年被我逼着，倒是也能开大点的车子了，因为我经常需要喝酒，她在的时候吃完饭就她开车嘛，所以现在也开过不少车了，MPV，大SUV都能上手，不过有一点，不要心疼自己的后轮，她拐弯不管车子长度的，我的后轮毂没一个好的，全部在马路牙子边上摩擦过，甚至有一次拐弯时还骑到了主辅路之间的隔离带上，后轮都架空了，你还不能说她，还得安慰她。</p><p>你问我坐旁边为什么不提醒她，不敢啊！ 说多了吵架，还有一点，她开车时只要一说话，车速就会降到二十左右，我怕影响交通啊，你不说话她就开的飞快，还是早点到家好，车子嘛，坏了就修，哪有感情重要啊。</p><p>她开车还有一个特点，就是我前边说的顽疾之一，就是路上的坑啊井盖啊从来躲不开，哪怕本来压不到调整方向也要压上去，一个都不放过，她现在开的车子已经先后颠爆了两个轮胎了，你说牛不牛，不过宝马的缺气保用轮胎也确实不咋结实也是了。</p><p>最后说事故，基本一年至少一两次吧，都不严重，而且大多是单方事故，撞停车场柱子啊，蹭墙啊啥的。比如最近的一次，和桥墩子较劲，结果还是桥墩子硬些。</p><figure data-size="normal"><img src="data:image/svg+xml;utf8,&lt;svg xmlns=&#39;http://www.w3.org/2000/svg&#39; width=&#39;1440&#39; height=&#39;1080&#39;&gt;&lt;/svg&gt;" data-caption="" data-size="normal" data-rawwidth="1440" data-rawheight="1080" data-default-watermark-src="https://pic2.zhimg.com/50/v2-3bf5a017f76ea1387fb4373ad142ec00_hd.jpg" class="origin_image zh-lightbox-thumb lazy" width="1440" data-original="https://pic3.zhimg.com/v2-aa3bd0f2e6cea5ba54f66404b8c7c057_r.jpg" data-actualsrc="https://pic3.zhimg.com/50/v2-aa3bd0f2e6cea5ba54f66404b8c7c057_hd.jpg"/></figure><figure data-size="normal"><img src="data:image/svg+xml;utf8,&lt;svg xmlns=&#39;http://www.w3.org/2000/svg&#39; width=&#39;1440&#39; height=&#39;1080&#39;&gt;&lt;/svg&gt;" data-caption="" data-size="normal" data-rawwidth="1440" data-rawheight="1080" data-default-watermark-src="https://pic3.zhimg.com/50/v2-fbe745b0185deee34c3a475bebd1b482_hd.jpg" class="origin_image zh-lightbox-thumb lazy" width="1440" data-original="https://pic4.zhimg.com/v2-62983f2e8c58aec68a993040fe271644_r.jpg" data-actualsrc="https://pic4.zhimg.com/50/v2-62983f2e8c58aec68a993040fe271644_hd.jpg"/></figure><p>这已经好几个月没事了，估计我又该准备和保险公司交流了，祝天下人开车平安。</p>】
<figure data-size="normal"><img class="origin_image zh-lightbox-thumb lazy" data-actualsrc="https://pic3.zhimg.com/50/v2-aa3bd0f2e6cea5ba54f66404b8c7c057_hd.jpg" data-caption="" data-default-watermark-src="https://pic2.zhimg.com/50/v2-3bf5a017f76ea1387fb4373ad142ec00_hd.jpg" data-original="https://pic3.zhimg.com/v2-aa3bd0f2e6cea5ba54f66404b8c7c057_r.jpg" data-rawheight="1080" data-rawwidth="1440" data-size="normal" src="data:image/svg+xml;utf8,&lt;svg xmlns='http://www.w3.org/2000/svg' width='1440' height='1080'&gt;&lt;/svg&gt;" width="1440"/></figure>
<figure data-size="normal"><img class="origin_image zh-lightbox-thumb lazy" data-actualsrc="https://pic4.zhimg.com/50/v2-62983f2e8c58aec68a993040fe271644_hd.jpg" data-caption="" data-default-watermark-src="https://pic3.zhimg.com/50/v2-fbe745b0185deee34c3a475bebd1b482_hd.jpg" data-original="https://pic4.zhimg.com/v2-62983f2e8c58aec68a993040fe271644_r.jpg" data-rawheight="1080" data-rawwidth="1440" data-size="normal" src="data:image/svg+xml;utf8,&lt;svg xmlns='http://www.w3.org/2000/svg' width='1440' height='1080'&gt;&lt;/svg&gt;" width="1440"/></figure>
没有了
'''
# res = ss.replace('<noscript>(.+?)</noscript>', '')
# res = re.sub(r'<noscript>(.+?)</noscript>', "", ss)

# pattern = re.compile(r'<noscript>(.+?)</noscript>')   # 查找数字
# res = pattern.findall(ss)
# for i in res:
#     ss.replace(i, ' ')
# r = ss.find('<noscript>')
# st = r+10
# print(ss[0:st])
# print(ss[ss[st:].find('</noscript>'):len(ss)])

# a = ss.replace("<noscript>", "<!--<noscript>").replace("</noscript>", "</noscript>-->")
# def work(sss):
#     head_num = sss.find('<figure')
#     head_str = sss[:head_num]
#     sea_str = sss[head_num:]
#     jq_num = sea_str.find('</figure>')
#     re_str = sea_str[:jq_num+9]
#     jq = len(re_str)
#     res = '0000000000000测试插入000000000'
#     return head_str+ res +sss[head_num+jq:]
#
# result = work(ss)
# while True:
#     if '<figure' in result:
#         result = work(result)
#     else:
#         print(result)
#         break

tt = '''
<figure><img class="origin_image zh-lightbox-thumb lazy" data-actualsrc="https://pic4.zhimg.com/50/v2-3e96a2d1017560cf88d4b5b839fb39ac_hd.jpg" data-original="https://pic4.zhimg.com/v2-3e96a2d1017560cf88d4b5b839fb39ac_r.jpg" data-rawheight="1920" data-rawwidth="1080" src="data:image/svg+xml;utf8,&lt;svg xmlns='http://www.w3.org/2000/svg' width='1080' height='1920'&gt;&lt;/svg&gt;" width="1080"/></figure>
<figure><img class="origin_image zh-lightbox-thumb lazy" data-actualsrc="https://pic1.zhimg.com/50/v2-27a11aeb3e20c788ab4b80810f8c4e55_hd.jpg" data-original="https://pic1.zhimg.com/v2-27a11aeb3e20c788ab4b80810f8c4e55_r.jpg" data-rawheight="1920" data-rawwidth="1080" src="data:image/svg+xml;utf8,&lt;svg xmlns='http://www.w3.org/2000/svg' width='1080' height='1920'&gt;&lt;/svg&gt;" width="1080"/></figure>
<figure><img class="origin_image zh-lightbox-thumb lazy" data-actualsrc="https://pic4.zhimg.com/50/v2-d24370a3ad75a356cdb33628c3ec3f69_hd.jpg" data-original="https://pic4.zhimg.com/v2-d24370a3ad75a356cdb33628c3ec3f69_r.jpg" data-rawheight="1920" data-rawwidth="1080" src="data:image/svg+xml;utf8,&lt;svg xmlns='http://www.w3.org/2000/svg' width='1080' height='1920'&gt;&lt;/svg&gt;" width="1080"/></figure>
 '''

ttt = '''<figure><img class="origin_image zh-lightbox-thumb lazy" data-actualsrc="https://pic4.zhimg.com/50/v2-d24370a3ad75a356cdb33628c3ec3f69_hd.jpg" data-original="https://pic4.zhimg.com/v2-d24370a3ad75a356cdb33628c3ec3f69_r.jpg" data-rawheight="1920" data-rawwidth="1080" src="data:image/svg+xml;utf8,&lt;svg xmlns='http://www.w3.org/2000/svg' width='1080' height='1920'&gt;&lt;/svg&gt;" width="1080"/></figure>'''



res = ttt.find('data-original')+15
print(ttt[res:].split('"')[0])