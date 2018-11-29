#!/usr/bin/env python

# encoding: utf-8

'''

@author: ly

@contact: 1364757394@qq.com

@software: garner

@file: YinyueTai.py

@time: 2018/8/31 10:39

@desc:

'''


from DatabaseManager import OperationDbInterface
from bs4 import BeautifulSoup
import lxml
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import re
import requests
from requests.exceptions import RequestException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from lxml import etree
from time import sleep

headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'Accept-Encoding':'gzip, deflate, sdch',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language':'zh-CN,zh;q=0.8',
    }

class MVList():
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"}

    def get_headers_driver(self):
        desire = DesiredCapabilities.PHANTOMJS.copy()
        headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                   'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,ja;q=0.4',
                   'Cache-Control': 'max-age=0',
                   'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 '
                                 '(KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
                   'Connection': 'keep-alive',
                   'Referer': 'http://www.ziroom.com/?utm_source=pinzhuan&utm_medium=baidu&utm_campaign=biaoti'
                   }
        for key, value in headers.items():
            desire['phantomjs.page.customHeaders.{}'.format(key)] = value
        driver = webdriver.PhantomJS(desired_capabilities=desire,
                                     service_args=['--load-images=yes'])  # 将yes改成no可以让浏览器不加载图片
        return driver


    def download(self,url,name):
        try:
            print(url)
            response = requests.get(url, headers=headers)
            data = response.content
            if data:
                file_path = "/Users/ly/Desktop/mv/" + name + ".mp4"
                if not os.path.exists(file_path):
                    with open(file_path, 'wb') as f:
                        f.write(data)
                        f.close()
                        print("success")
        except Exception:
            print('faile')


    def getUrlList(self,url):
        driver = self.get_headers_driver()
        driver.get(url)
        source = driver.page_source
        content_div = BeautifulSoup(source,'lxml').find('div', class_='fan_cont')
        list_div = BeautifulSoup(str(content_div),'lxml').find('div',class_='mv_list')
        lis = BeautifulSoup(str(list_div),'lxml').find_all('li')
        for li in lis:
            title_div = BeautifulSoup(str(li),'lxml').find('div',class_='mv_title')
            a = BeautifulSoup(str(title_div),'lxml').find('a')
            pre = str(a['href']).strip()
            mv_id = pre.replace('http://v.yinyuetai.com/video/', '')
            url = 'http://v.yinyuetai.com/video/h5/' + mv_id
            print(url)


    def getMvUrl(self,url):
        driver = self.get_headers_driver()
        driver.get(url)
        source = driver.page_source
        content_div = BeautifulSoup(source, 'lxml').find('div', class_='videoBox')
        video_div = BeautifulSoup(str(content_div), 'lxml').find('div', class_='mw-videos-box')
        video_div = BeautifulSoup(str(video_div), 'lxml').find_all('div', class_='video-container')
        print(video_div)
        video = BeautifulSoup(str(video_div),'lxml').find('video',class_='video-stream')
        print(video)


mv = MVList()


list = ['http://www.7xiaofu.com/download/mv/wulianwang.mp4','http://p3zaeayvo.bkt.clouddn.com/crh.mp4','http://www.7xiaofu.com/download/mv/zx2.mp4']
title = ['物联网技术与应用','超融合产品交流','智慧城市大数据解决方案--问答环节']
for i in range(3):
    url = list[i]
    name = title[i]
    mv.download(url,name)

# mv.getMvUrl('http://v.yinyuetai.com/video/h5/3256571')

# for i in range(8):
#     pre = 'http://www.yinyuetai.com/fanclub/mv-all/3261/toNew/'
#     url = pre + str(i+1)
#     mv.getUrlList(url)

# def read_txt(dir):
#     with open(dir,'r') as f:
#         return f.readlines()
#     return ''
#
# text = read_txt('/Users/ly/Desktop/123123123')
# video_div = BeautifulSoup(str(text), 'lxml').find_all('div', class_='video-container')
# for div in video_div:
#     video = BeautifulSoup(str(div),'lxml').find('video',class_='video-stream')
#     print(video['src'])

'''
http://v.yinyuetai.com/video/h5/3256571
http://v.yinyuetai.com/video/h5/3220229
http://v.yinyuetai.com/video/h5/3210096
http://v.yinyuetai.com/video/h5/3108153

http://v.yinyuetai.com/video/h5/3073533
http://v.yinyuetai.com/video/h5/3039990
http://v.yinyuetai.com/video/h5/3027519
http://v.yinyuetai.com/video/h5/2844306
http://v.yinyuetai.com/video/h5/2752809
http://v.yinyuetai.com/video/h5/2752808
http://v.yinyuetai.com/video/h5/2752807
http://v.yinyuetai.com/video/h5/2752731
http://v.yinyuetai.com/video/h5/2752730
http://v.yinyuetai.com/video/h5/2752729
http://v.yinyuetai.com/video/h5/2683770
http://v.yinyuetai.com/video/h5/2683753
http://v.yinyuetai.com/video/h5/2683744
http://v.yinyuetai.com/video/h5/2683730
http://v.yinyuetai.com/video/h5/2626614
http://v.yinyuetai.com/video/h5/2551183
http://v.yinyuetai.com/video/h5/2551173
http://v.yinyuetai.com/video/h5/2546866
http://v.yinyuetai.com/video/h5/2546846
http://v.yinyuetai.com/video/h5/2437962
http://v.yinyuetai.com/video/h5/2430063
http://v.yinyuetai.com/video/h5/2430058
http://v.yinyuetai.com/video/h5/2410246
http://v.yinyuetai.com/video/h5/2387860
http://v.yinyuetai.com/video/h5/2370681
http://v.yinyuetai.com/video/h5/2343333
http://v.yinyuetai.com/video/h5/2343314
http://v.yinyuetai.com/video/h5/2342009
http://v.yinyuetai.com/video/h5/2341988
http://v.yinyuetai.com/video/h5/2338413
http://v.yinyuetai.com/video/h5/2325305
http://v.yinyuetai.com/video/h5/2324240
http://v.yinyuetai.com/video/h5/2274824
http://v.yinyuetai.com/video/h5/2263238
http://v.yinyuetai.com/video/h5/2262326
http://v.yinyuetai.com/video/h5/2258931
http://v.yinyuetai.com/video/h5/2244030
http://v.yinyuetai.com/video/h5/2239773
http://v.yinyuetai.com/video/h5/2230161
http://v.yinyuetai.com/video/h5/2198617
http://v.yinyuetai.com/video/h5/2174732
http://v.yinyuetai.com/video/h5/2069794
http://v.yinyuetai.com/video/h5/2064330
http://v.yinyuetai.com/video/h5/2042283
http://v.yinyuetai.com/video/h5/2042216
http://v.yinyuetai.com/video/h5/2041374
http://v.yinyuetai.com/video/h5/2041234
http://v.yinyuetai.com/video/h5/2039697
http://v.yinyuetai.com/video/h5/2023678
http://v.yinyuetai.com/video/h5/825269
http://v.yinyuetai.com/video/h5/812382
http://v.yinyuetai.com/video/h5/812341
http://v.yinyuetai.com/video/h5/807084
http://v.yinyuetai.com/video/h5/807067
http://v.yinyuetai.com/video/h5/807039
http://v.yinyuetai.com/video/h5/807005
http://v.yinyuetai.com/video/h5/797550
http://v.yinyuetai.com/video/h5/760738
http://v.yinyuetai.com/video/h5/758060
http://v.yinyuetai.com/video/h5/758041
http://v.yinyuetai.com/video/h5/695649
http://v.yinyuetai.com/video/h5/688529
http://v.yinyuetai.com/video/h5/687480
http://v.yinyuetai.com/video/h5/685679
http://v.yinyuetai.com/video/h5/681676
http://v.yinyuetai.com/video/h5/681673
http://v.yinyuetai.com/video/h5/681573
http://v.yinyuetai.com/video/h5/677197
http://v.yinyuetai.com/video/h5/677196
http://v.yinyuetai.com/video/h5/677195
http://v.yinyuetai.com/video/h5/677191
http://v.yinyuetai.com/video/h5/677190
http://v.yinyuetai.com/video/h5/673543
http://v.yinyuetai.com/video/h5/673309
http://v.yinyuetai.com/video/h5/591744
http://v.yinyuetai.com/video/h5/591044
http://v.yinyuetai.com/video/h5/588256
http://v.yinyuetai.com/video/h5/566106
http://v.yinyuetai.com/video/h5/549044
http://v.yinyuetai.com/video/h5/535947
http://v.yinyuetai.com/video/h5/533786
http://v.yinyuetai.com/video/h5/533779
http://v.yinyuetai.com/video/h5/520109
http://v.yinyuetai.com/video/h5/399077
http://v.yinyuetai.com/video/h5/394478
http://v.yinyuetai.com/video/h5/394317
http://v.yinyuetai.com/video/h5/391636
http://v.yinyuetai.com/video/h5/390670
http://v.yinyuetai.com/video/h5/390652
http://v.yinyuetai.com/video/h5/390607
http://v.yinyuetai.com/video/h5/388636
http://v.yinyuetai.com/video/h5/387897
http://v.yinyuetai.com/video/h5/383260
http://v.yinyuetai.com/video/h5/379001
http://v.yinyuetai.com/video/h5/374312
http://v.yinyuetai.com/video/h5/374290
http://v.yinyuetai.com/video/h5/367019
http://v.yinyuetai.com/video/h5/361290
http://v.yinyuetai.com/video/h5/355698
http://v.yinyuetai.com/video/h5/355690
http://v.yinyuetai.com/video/h5/348461
http://v.yinyuetai.com/video/h5/346306
http://v.yinyuetai.com/video/h5/345819
http://v.yinyuetai.com/video/h5/345818
http://v.yinyuetai.com/video/h5/342298
http://v.yinyuetai.com/video/h5/327172
http://v.yinyuetai.com/video/h5/327125
http://v.yinyuetai.com/video/h5/326787
http://v.yinyuetai.com/video/h5/326776
http://v.yinyuetai.com/video/h5/326759
http://v.yinyuetai.com/video/h5/320567
http://v.yinyuetai.com/video/h5/315249
http://v.yinyuetai.com/video/h5/259124
http://v.yinyuetai.com/video/h5/229603
http://v.yinyuetai.com/video/h5/158736
http://v.yinyuetai.com/video/h5/158005
http://v.yinyuetai.com/video/h5/157834
http://v.yinyuetai.com/video/h5/133306
http://v.yinyuetai.com/video/h5/132885
http://v.yinyuetai.com/video/h5/85925
http://v.yinyuetai.com/video/h5/85227
http://v.yinyuetai.com/video/h5/84446
http://v.yinyuetai.com/video/h5/84252
http://v.yinyuetai.com/video/h5/84157
http://v.yinyuetai.com/video/h5/84074
http://v.yinyuetai.com/video/h5/83943
http://v.yinyuetai.com/video/h5/81682
http://v.yinyuetai.com/video/h5/75791
http://v.yinyuetai.com/video/h5/71102
http://v.yinyuetai.com/video/h5/63791
http://v.yinyuetai.com/video/h5/45992
http://v.yinyuetai.com/video/h5/43907
http://v.yinyuetai.com/video/h5/43230
http://v.yinyuetai.com/video/h5/43157
http://v.yinyuetai.com/video/h5/43117
http://v.yinyuetai.com/video/h5/34204
http://v.yinyuetai.com/video/h5/18361
http://v.yinyuetai.com/video/h5/3568
'''
'''
http://hc.yinyuetai.com/uploads/videos/common/86900164CC71FF82DC712A39B0E55A91.mp4?sc=4521e1c57fb5d625&amp;br=781&amp;vid=3256571&amp;aid=3261&amp;area=US&amp;vst=3
http://hc.yinyuetai.com/uploads/videos/common/3307016449C2118C6CE9BAC10AF68D45.mp4?sc=93b7d66a8412b1bc&amp;br=781&amp;vid=3220229&amp;aid=3261&amp;area=US&amp;vst=0
http://hc.yinyuetai.com/uploads/videos/common/584701634D4C1263EE05F01850FD0BD5.mp4?sc=bfea3159b79d8ba2&amp;br=785&amp;vid=3210096&amp;aid=3261&amp;area=US&amp;vst=3
http://hc.yinyuetai.com/uploads/videos/common/CBFD0160318F30A1A4FB75282E184294.mp4?sc=5a6175feca721b5f&amp;br=777&amp;vid=3108153&amp;aid=3261&amp;area=US&amp;vst=0
http://hc.yinyuetai.com/uploads/videos/common/47A6015F4E60D98DEB8CCBDD9B54E7D7.mp4?sc=e7d30450c4633c9b&amp;br=781&amp;vid=3073533&amp;aid=3261&amp;area=US&amp;vst=2
http://hc.yinyuetai.com/uploads/videos/common/612E015E7124F3026DE451DB2FE6EF3D.mp4?sc=b0f2354048e17cb5&amp;br=777&amp;vid=3039990&amp;aid=3261&amp;area=US&amp;vst=3
http://hc.yinyuetai.com/uploads/videos/common/B053015E242B5D70FB7A5A18D89C8C71.mp4?sc=8e8c3dbec66f8d06&amp;br=779&amp;vid=3027519&amp;aid=3261&amp;area=US&amp;vst=3
http://hc.yinyuetai.com/uploads/videos/common/7AAD01590D9DD76D6D2B464FAB695870.mp4?sc=82a6a5a489bce1be&br=752&vid=2752729&aid=3261&area=US&vst=3
http://hc.yinyuetai.com/uploads/videos/common/488701574BA002DE615F95F6E8997726.flv?sc=d5e0768cbcd2e870&br=781&vid=2683770&aid=3261&area=US&vst=3
http://hc.yinyuetai.com/uploads/videos/common/C29401590D9E4CCC379F733147B5E781.mp4?sc=31912dcab32aebd2&br=745&vid=2752730&aid=3261&area=US&vst=3
http://hc.yinyuetai.com/uploads/videos/common/CE6C01590D9F2464BE7B3A6429419578.mp4?sc=0adf05e49343fdfc&br=743&vid=2752731&aid=3261&area=US&vst=3
http://hc.yinyuetai.com/uploads/videos/common/B0A601590D9F9935859F7168D7400323.mp4?sc=285c87ddebc2f418&br=777&vid=2752807&aid=3261&area=US&vst=3
http://hc.yinyuetai.com/uploads/videos/common/B6ED01590DA0269C6C84C6573AC1AE86.mp4?sc=8c76f8c505b62f9e&br=747&vid=2752808&aid=3261&area=US&vst=3
http://hc.yinyuetai.com/uploads/videos/common/0B8A01590DA0D1227880104A4685F0FC.mp4?sc=2de06dc75fa66ab4&br=743&vid=2752809&aid=3261&area=US&vst=3
http://hc.yinyuetai.com/uploads/videos/common/C7E201574B97D9E2C1FE21301150FF10.flv?sc=4069fdd95ea1f0fc&br=780&vid=2683753&aid=3261&area=US&vst=2
http://hc.yinyuetai.com/uploads/videos/common/5A3A01574B8DB3D08AF361054B934A4E.flv?sc=7e296dd5a6422736&br=779&vid=2683744&aid=3261&area=US&vst=2
http://hc.yinyuetai.com/uploads/videos/common/A2CC01574B8835AA5FD0155C2F407794.flv?sc=5ef6befbfa1a790d&br=786&vid=2683730&aid=3261&area=US&vst=2
http://hc.yinyuetai.com/uploads/videos/common/02C301561173181457C13EECFD060E19.flv?sc=52911e83330964fa&br=779&vid=2626614&aid=3261&area=US&vst=3
http://hc.yinyuetai.com/uploads/videos/common/379E01542CF14665BBB84E806E505BDB.flv?sc=b9a54b6fe4e23960&br=780&vid=2551183&aid=3261&area=US&vst=3
http://hc.yinyuetai.com/uploads/videos/common/083401542CEEFC7BCDA3C7D917D7E523.flv?sc=bd538ec8c092c29c&br=784&vid=2551173&aid=3261&area=US&vst=3
http://hc.yinyuetai.com/uploads/videos/common/6441015413F1E4C0CC372801280CCA49.flv?sc=8aa286dbb7904604&br=780&vid=2546866&aid=3261&area=US&vst=3
http://hc.yinyuetai.com/uploads/videos/common/FCB5015413EC18B49ACF65A5093E5E02.flv?sc=8937577ea7bca0a6&br=782&vid=2546846&aid=3261&area=US&vst=3
http://hc.yinyuetai.com/uploads/videos/common/1F1A01516215A9016083C53ACA9F5FA6.flv?sc=1d6fb1a80df890ce&br=779&vid=2437962&aid=3261&area=US&vst=3
http://hc.yinyuetai.com/uploads/videos/common/4C50015137E99C52BBD0C807270CC20A.flv?sc=d8f0b3c953d7b00b&br=776&vid=2430063&aid=3261&area=US&vst=3
http://hc.yinyuetai.com/uploads/videos/common/61F5015137C2705FEEC40C58D3939F54.flv?sc=5066850e864492c5&br=778&vid=2430058&aid=3261&area=US&vst=0
http://hc.yinyuetai.com/uploads/videos/common/65890150CCEE99A0A0572C6E2EC5CEBC.flv?sc=94c75073786040be&br=777&vid=2410246&aid=3261&area=US&vst=2
http://hc.yinyuetai.com/uploads/videos/common/FC0101503B58D2414DEC3A2292B8C26F.flv?sc=bce36d038f56c08c&br=780&vid=2387860&aid=3261&area=US&vst=3
http://hc.yinyuetai.com/uploads/videos/common/40BB014FCAB93AA404F4122A7BB76289.flv?sc=545701fcf0280ecb&br=779&vid=2370681&aid=3261&area=US&vst=3
http://hc.yinyuetai.com/uploads/videos/common/2B96014EF18D3729DA579F14C9D6A9B3.flv?sc=efdf8f19c937cdb3&br=781&vid=2343333&aid=3261&area=US&vst=3
http://hc.yinyuetai.com/uploads/videos/common/7E43014EF183243E916C028B2C60C056.flv?sc=bf37016fe110cab8&br=779&vid=2343314&aid=3261&area=US&vst=3
http://hc.yinyuetai.com/uploads/videos/common/B6A9014EE74F2607F41DEB1478A6547F.flv?sc=983cf6aaf0139936&br=780&vid=2342009&aid=3261&area=US&vst=3
http://hc.yinyuetai.com/uploads/videos/common/7972014EE735838AC1B842A66FE3C0DA.flv?sc=d109ae4f0829b6eb&br=781&vid=2341988&aid=3261&area=US&vst=3
http://hc.yinyuetai.com/uploads/videos/common/1BD8014ED014CB51FCFB6D2876D8B6B9.flv?sc=7027ed252c44ef92&br=779&vid=2338413&aid=3261&area=US&vst=3
http://hc.yinyuetai.com/uploads/videos/common/237D014E695ED7F5D128A2519F533AAF.flv?sc=c08d1ea5e81c97e4&br=778&vid=2325305&aid=3261&area=US&vst=3
http://hc.yinyuetai.com/uploads/videos/common/FCC5014E62749B8DA9EF4C7D3300B174.flv?sc=61057e45e36bcb3a&br=780&vid=2324240&aid=3261&area=US&vst=3
http://hc.yinyuetai.com/uploads/videos/common/9441014CC608B1055FEA4F8CDEB85E89.flv?sc=8258dd1a633dc88c&br=780&vid=2274824&aid=3261&area=US&vst=3
http://hc.yinyuetai.com/uploads/videos/common/F1A0014C5948708B24C03670E38481A2.flv?sc=89879a552b45b0a1&br=779&vid=2263238&aid=3261&area=US&vst=2
http://hc.yinyuetai.com/uploads/videos/common/D54B014C50303BFD9CB359D01B24B858.flv?sc=ca5dc60d00b5903c&br=778&vid=2262326&aid=3261&area=US&vst=3
http://hc.yinyuetai.com/uploads/videos/common/4F03014C361EF45382A3D6B205DB11A3.flv?sc=4a0f229e7f0af838&br=779&vid=2258931&aid=3261&area=US&vst=2
http://hc.yinyuetai.com/uploads/videos/common/5D34014BB58497B7EA2BBA8B239DB3AD.flv?sc=f47558d50f1964e0&br=788&vid=2244030&aid=3261&area=US&vst=3
http://hc.yinyuetai.com/uploads/videos/common/A0C5014B8101E6C85C05122178968995.flv?sc=4354c60828d9a229&br=778&vid=2239773&aid=3261&area=US&vst=2
http://hc.yinyuetai.com/uploads/videos/common/034D014B3695C712D4F47D0BBF38598B.flv?sc=b53c36e73ab027fe&br=779&vid=2230161&aid=3261&area=US&vst=3
http://hc.yinyuetai.com/uploads/videos/common/93CF014A300FAA93A4877AAF2A6CAB50.flv?sc=214b9ce50fb76253&br=777&vid=2198617&aid=3261&area=US&vst=3
http://hc.yinyuetai.com/uploads/videos/common/9A1601497D2CFD160257B14908455DA4.flv?sc=bca4c1fcb40833bf&br=777&vid=2174732&aid=3261&area=US&vst=3
http://hc.yinyuetai.com/uploads/videos/common/03E401467FC9AB66408F910055E24B1E.flv?sc=093d464f6fa424fb&br=746&vid=2069794&aid=3261&area=US&vst=3
http://hc.yinyuetai.com/uploads/videos/common/A94101465AFB0D2254B089DF2332B7DA.flv?sc=7918d326cfdf0a6a&br=778&vid=2064330&aid=3261&area=US&vst=3
http://hc.yinyuetai.com/uploads/videos/common/71E10145AC7CA1155ED983CEFCE8F5CB.flv?sc=20163ee6e00952de&br=778&vid=2042283&aid=3261&area=US&vst=3
http://hc.yinyuetai.com/uploads/videos/common/404C0145AC2CFA6ADA56B4BF60F7AB12.flv?sc=2d092b09e19ae1ed&br=775&vid=2042216&aid=3261&area=US&vst=3
http://hc.yinyuetai.com/uploads/videos/common/6A180145A6F44ECF310345870B8C0265.flv?sc=92fa7575542b9d42&br=777&vid=2041374&aid=3261&area=US&vst=3
http://hc.yinyuetai.com/uploads/videos/common/92DE0145A66CCF4D4B4CB035DDDDB442.flv?sc=929b6ec39ad5dae0&br=779&vid=2041234&aid=3261&area=US&vst=3
http://hc.yinyuetai.com/uploads/videos/common/312A01459BD2456BA615F0150CDEEC68.flv?sc=9f08e9d8277a804d&br=779&vid=2039697&aid=3261&area=US&vst=3
http://hc.yinyuetai.com/uploads/videos/common/C99701452105CF4989657D2D94ABFD65.flv?sc=d689f56f5b239306&br=779&vid=2023678&aid=3261&area=US&vst=3
http://hc.yinyuetai.com/uploads/videos/common/E9690142B81173A465F2FFC0C0B8CB0B.flv?sc=031466237beae016&br=778&vid=825269&aid=3261&area=US&vst=3
http://hc.yinyuetai.com/uploads/videos/common/B8B701425FE51FF43A41CAF56938FBEA.flv?sc=b5e0bb5164ef8847&br=778&vid=812382&aid=3261&area=US&vst=2
http://hc.yinyuetai.com/uploads/videos/common/0DEE01425FC16B3044C32E941929A985.flv?sc=40449d1fc64f48e6&br=788&vid=812341&aid=3261&area=US&vst=2
http://hc.yinyuetai.com/uploads/videos/common/1DB201423B5782F67FF95134CDA45369.flv?sc=ed11187b51514168&br=780&vid=807084&aid=3261&area=US&vst=3
http://hc.yinyuetai.com/uploads/videos/common/78FD01423B3B216D25F7AF2ADF2F3008.flv?sc=9dc0e56adda86a16&br=780&vid=807067&aid=3261&area=US&vst=3
http://hc.yinyuetai.com/uploads/videos/common/C7C401423AFB0B2F04CF75F2C2CBEE40.flv?sc=1703a1c3b96d25c1&br=779&vid=807039&aid=3261&area=US&vst=3
http://hc.yinyuetai.com/uploads/videos/common/397F01423ADBEA6EEA07B55FCC492C95.flv?sc=e495cdb4f7a54f36&br=779&vid=807005&aid=3261&area=US&vst=3
http://hc.yinyuetai.com/uploads/videos/common/58670141F94354B8F1C24FEB5A59F214.flv?sc=9f7c40b678584011&br=773&vid=797550&aid=3261&area=US&vst=0
http://hc.yinyuetai.com/uploads/videos/common/D6480140FD7336D1D788C9443F156BED.flv?sc=dd978c6d05fb22b9&br=778&vid=760738&aid=3261&area=US&vst=3
http://hc.yinyuetai.com/uploads/videos/common/4D290140EF87F7CF4971454B8DDF914F.flv?sc=ee2861e571ad56fb&br=778&vid=758060&aid=3261&area=US&vst=2
http://hc.yinyuetai.com/uploads/videos/common/5C460140EF49B85A7415235F2D23C0DA.flv?sc=65203bd177f5ca9a&br=776&vid=758041&aid=3261&area=US&vst=2
http://hc.yinyuetai.com/uploads/videos/common/A320013F716D5D49F6D7D211B8C14434.flv?sc=35216cdb644b11bb&br=777&vid=695649&aid=3261&area=US&vst=3
http://hc.yinyuetai.com/uploads/videos/common/8C98013F42BC3D4A38E18BC8C64EBBFC.flv?sc=13b93d0750dbd5ab&br=776&vid=688529&aid=3261&area=US&vst=2
http://hc.yinyuetai.com/uploads/videos/common/8859013F41C8BB7252FC8461AB8CF7EC.flv?sc=10288696023d6dba&br=783&vid=687480&aid=3261&area=US&vst=3
http://hc.yinyuetai.com/uploads/videos/common/7F62013F29268E98DF335EBA8281210D.flv?sc=a3d23d710685e288&br=778&vid=685679&aid=3261&area=US&vst=3
http://hc.yinyuetai.com/uploads/videos/common/B42B013F1A10DCD0B7E24175A9380C4F.flv?sc=18242caba899e018&br=779&vid=681676&aid=3261&area=US&vst=2
http://hc.yinyuetai.com/uploads/videos/common/51C6013F19F9F982F699E1478E317908.flv?sc=206aefd752f20e27&br=778&vid=681673&aid=3261&area=US&vst=3
http://hc.yinyuetai.com/uploads/videos/common/AC40013F197C8EE92E34CDAED60341F1.flv?sc=13fb58034e358b2f&br=780&vid=681573&aid=3261&area=US&vst=3
http://hc.yinyuetai.com/uploads/videos/common/154A013EF948396DA91E5813A3F4A0FC.flv?sc=9f74ff3f6b8e0660&br=777&vid=677197&aid=3261&area=US&vst=3
http://hc.yinyuetai.com/uploads/videos/common/1A99013EF9A2DD1DE3F8089D9B74A978.flv?sc=448a5c300c3ebbc4&br=779&vid=677196&aid=3261&area=US&vst=3
http://hc.yinyuetai.com/uploads/videos/common/59AD013EF9CA3B1CF9B99227389E0393.flv?sc=23e55a232eb5f135&br=779&vid=677195&aid=3261&area=US&vst=3
http://hc.yinyuetai.com/uploads/videos/common/D49B013EF9C69097A0BFCF32C5B38436.flv?sc=f2c1875fc0c04586&br=779&vid=677191&aid=3261&area=US&vst=3
http://hc.yinyuetai.com/uploads/videos/common/E37F013EF9CECDF42937F6DB4AA23B69.flv?sc=1659cf441718bed3&br=778&vid=677190&aid=3261&area=US&vst=3
http://hc.yinyuetai.com/uploads/videos/common/BE3A013D8966AC65FA9C550397988E67.flv?sc=8bd1ac03ad2bd1d1&br=1172&vid=673543&aid=3261&area=US&vst=1
http://hc.yinyuetai.com/uploads/videos/common/D92E013EE5440482A612095C9E61AE7B.flv?sc=ae227627919f6955&br=777&vid=673309&aid=3261&area=US&vst=3
http://hc.yinyuetai.com/uploads/videos/common/07F2013C61F435EAE19685100604B4B8.flv?sc=9800a9d79f0ea265&br=778&vid=591744&aid=3261&area=US&vst=3
http://hc.yinyuetai.com/uploads/videos/common/701C013C5D2EE7EA6EC1941366EC971A.flv?sc=9e12bd716d51c2bf&br=778&vid=591044&aid=3261&area=US&vst=3
http://hc.yinyuetai.com/uploads/videos/common/7839013C4C15C2CE752669D9B36EF09A.flv?sc=7a5e67ad4d692e8f&br=778&vid=588256&aid=3261&area=US&vst=3
http://hc.yinyuetai.com/uploads/videos/common/4466013B9B168D8728681C0E4216A329.flv?sc=5f9ed23d521bf314&br=1075&vid=566106&aid=3261&area=US&vst=0
http://hc.yinyuetai.com/uploads/videos/common/A333013F704C141DC2F93762096B62EC.flv?sc=a82d28e819bdd08e&br=775&vid=549044&aid=3261&area=US&vst=0
http://hc.yinyuetai.com/uploads/videos/common/8647013A88DB0D0E3CDB497F88346B2C.flv?sc=fab40b31b863c3c7&br=774&vid=535947&aid=3261&area=US&vst=0
http://hc.yinyuetai.com/uploads/videos/common/BA6A013A73EE336DA688485BD2FA5A9F.flv?sc=ddca1f2ad391ac15&br=778&vid=533786&aid=3261&area=US&vst=2
http://hc.yinyuetai.com/uploads/videos/common/8230013A7745536D436B3F6E40C31ADB.flv?sc=b860033d9ed37c22&br=777&vid=533779&aid=3261&area=US&vst=3
http://hc.yinyuetai.com/uploads/videos/common/B4AD013A11A4BEEBB2255B289E8F96AA.flv?sc=11ca8b69d240b32d&br=777&vid=520109&aid=3261&area=US&vst=0
http://hc.yinyuetai.com/uploads/videos/common/194C0136D2834C8EA8A38E1A8E24C627.flv?sc=cab29ada35ce731b&br=712&vid=399077&aid=3261&area=US&vst=0
http://hc.yinyuetai.com/uploads/videos/common/14420136AEF75556D3697B71131CC396.flv?sc=61c83c95ee1b8e86&br=714&vid=394478&aid=3261&area=US&vst=3
http://hc.yinyuetai.com/uploads/videos/common/E1DA0136AC84F916414415CAEC2E7470.flv?sc=d02e0da8261b2100&br=717&vid=394317&aid=3261&area=US&vst=0
http://hc.yinyuetai.com/uploads/videos/common/FD4B013694A7FCBE94A28EF721EA0381.flv?sc=afe9c539f28308a0&br=713&vid=391636&aid=3261&area=US&vst=2
http://hc.yinyuetai.com/uploads/videos/common/2F66013691312F744F61FF3CE41E8966.flv?sc=f673c58faeefe12f&br=714&vid=390670&aid=3261&area=US&vst=0
http://hc.yinyuetai.com/uploads/videos/common/DB06013690F3901368EEC737D4CD1925.flv?sc=bce49dbee404322e&br=717&vid=390652&aid=3261&area=US&vst=2
http://hc.yinyuetai.com/uploads/videos/common/B235013690F42E5A26A08B1F2F1BA330.flv?sc=286a646b11da1154&br=714&vid=390607&aid=3261&area=US&vst=0
http://hc.yinyuetai.com/uploads/videos/common/1EEC013687E80FC3967BFEF3BE2BBCEB.flv?sc=9e1b1cf6365c45c0&br=714&vid=388636&aid=3261&area=US&vst=2
http://hc.yinyuetai.com/uploads/videos/common/ACBB01365D3069E7ED4A6DB89BF7F2DE.flv?sc=484ed03a2ed2a380&br=713&vid=383260&aid=3261&area=US&vst=0
http://hc.yinyuetai.com/uploads/videos/common/5788013CB4FA2E39D35CBC058765DF30.flv?sc=f1b5a5898304f774&br=780&vid=379001&aid=3261&area=US&vst=3
http://hc.yinyuetai.com/uploads/videos/common/B9A501361919668EA0BF4180A8D08760.flv?sc=92efa30356a8f98d&br=714&vid=374312&aid=3261&area=US&vst=0
http://hc.yinyuetai.com/uploads/videos/common/40F901361953C48BAFC595A2724FCF58.flv?sc=84c51ae16bd0c925&br=714&vid=374290&aid=3261&area=US&vst=0
http://hc.yinyuetai.com/uploads/videos/common/82710135DC317017F4F592D06FB7EBB7.flv?sc=41d7d4d6585dd0a9&br=742&vid=367019&aid=3261&area=US&vst=1
http://hc.yinyuetai.com/uploads/videos/common/A02C0135B018BCF8E35C4CD8F6463731.flv?sc=b6cf8749df36c21e&br=505&vid=361290&aid=3261&area=US&vst=3
http://hc.yinyuetai.com/uploads/videos/common/8F9D013581389A41C77059A959E2084D.flv?sc=f8807e0ad646ce34&br=679&vid=355698&aid=3261&area=US&vst=2
http://hc.yinyuetai.com/uploads/videos/common/F18601358137E887A556ABAA1E83E0F3.flv?sc=406e02b2cb59ff43&br=713&vid=355690&aid=3261&area=US&vst=2
http://hc.yinyuetai.com/uploads/videos/common/169C013555CAA6122636274A25CAE445.flv?sc=312d71716a133e39&br=639&vid=348461&aid=3261&area=US&vst=2
http://hc.yinyuetai.com/uploads/videos/common/98AF013CAC689308E94336CA058798C1.flv?sc=2183a14b638e5772&br=777&vid=346306&aid=3261&area=US&vst=0
http://hc.yinyuetai.com/uploads/videos/common/732E01354141F0A1F344B04B51B1C6A3.flv?sc=85d5472a2d75b38b&br=486&vid=345819&aid=3261&area=US&vst=3
http://hc.yinyuetai.com/uploads/videos/common/ADB4013541410C8443789F93D2478C9A.flv?sc=53dca8430cd84119&br=592&vid=345818&aid=3261&area=US&vst=0
http://hc.yinyuetai.com/uploads/videos/common/2196013532E369BEAD6E43E341B61A98.flv?sc=84bc0aab9e7d251e&br=632&vid=342298&aid=3261&area=US&vst=0
http://hc.yinyuetai.com/uploads/videos/common/7614013454D963BAED8DE545853727BE.flv?sc=58bc2bc6fabd0358&br=714&vid=327172&aid=3261&area=US&vst=2
http://hc.yinyuetai.com/uploads/videos/common/EF9501345467D9630CAA581B34EA851F.flv?sc=c0e553301b3dc5dd&br=716&vid=327125&aid=3261&area=US&vst=2
http://hc.yinyuetai.com/uploads/videos/common/6338013451C1DDA444EE48EFCB8E64B9.flv?sc=2b32c90c8ffed7b0&br=717&vid=326787&aid=3261&area=US&vst=2
http://hc.yinyuetai.com/uploads/videos/common/48580134511DBFD0B6EC4BD667254A13.flv?sc=3eaa2d3893887631&br=718&vid=326776&aid=3261&area=US&vst=2
http://hc.yinyuetai.com/uploads/videos/common/2A30013450F722735570CA7CA8C970FB.flv?sc=cffb8180f4292347&br=716&vid=326759&aid=3261&area=US&vst=2
http://hc.yinyuetai.com/uploads/videos/common/9B4A013423C53D9DC37D692880BA498C.flv?sc=c539e58f6ca0dcff&br=633&vid=320567&aid=3261&area=US&vst=3
http://hc.yinyuetai.com/uploads/videos/common/1E570133FD615157ABB5E65BD164DF7C.flv?sc=cf158285cdddd9f5&br=715&vid=315249&aid=3261&area=US&vst=2
http://hc.yinyuetai.com/uploads/videos/common/2B82013234405854BB0AD5B580EBB8F1.flv?sc=f84654d0f22354f5&br=684&vid=259124&aid=3261&area=US&vst=2
http://hc.yinyuetai.com/uploads/videos/common/783E01318BDBD8DDACC52A9ADC12C8FF.flv?sc=456757aba17a956e&br=684&vid=229603&aid=3261&area=US&vst=2
http://hc.yinyuetai.com/uploads/videos/common/6B34012F247264AF920970744F011026.flv?sc=5a86d83e3094b7d8&br=745&vid=158736&aid=3261&area=US&vst=1
http://hc.yinyuetai.com/uploads/videos/common/26F4012F388AD0C40B47DBAE780A461E.flv?sc=1719de01bebdaad1&br=739&vid=158005&aid=3261&area=US&vst=3
http://hc.yinyuetai.com/uploads/videos/common/81000BCA562FC8895B3623E62CED96DA.flv?sc=258ca046c2807e07&br=698&vid=157834&aid=3261&area=US&vst=0
http://hc.yinyuetai.com/uploads/videos/common/C64D01375F81EFC0F3BD24A4980790CE.flv?sc=495bef8f927b88c2&br=752&vid=133306&aid=3261&area=US&vst=0
http://hc.yinyuetai.com/uploads/videos/common/A10E012E31245AC5B5CFC87739AA2263.flv?sc=91102f89efd7b72d&br=748&vid=132885&aid=3261&area=US&vst=2
http://hc.yinyuetai.com/uploads/videos/common/57B1012BA21F0C655CB007200AE07B5B.flv?sc=a2d253289894a74f&br=760&vid=85925&aid=3261&area=US&vst=0
http://hc.yinyuetai.com/uploads/videos/common/58C4012B92EE88501BDC1C0188EDFDBC.flv?sc=0bde8015cd98268a&br=733&vid=85227&aid=3261&area=US&vst=0
http://hc.yinyuetai.com/uploads/videos/common/F431012B85D38EC78F7A5DB7B431F25E.flv?sc=629006f78f86b573&br=752&vid=84446&aid=3261&area=US&vst=2
http://hc.yinyuetai.com/uploads/videos/common/401BA40DACDBECC5C2FEC93207C53452.flv?sc=b2a610198d8fa94e&br=749&vid=84252&aid=3261&area=US&vst=3
http://hc.yinyuetai.com/uploads/videos/common/739A012B85E8A3DF3A86359E51EC9395.flv?sc=fa07d2e57bb79a10&br=751&vid=84157&aid=3261&area=US&vst=0
http://hc.yinyuetai.com/uploads/videos/common/FA24012B85E9D0C685E927D267644809.flv?sc=f68145f662e77ecb&br=744&vid=84074&aid=3261&area=US&vst=0
http://hc.yinyuetai.com/uploads/videos/common/02E6012B8204589A53D3D49980B9A760.flv?sc=34a5aa25d0c83beb&br=759&vid=83943&aid=3261&area=US&vst=0
http://hc.yinyuetai.com/uploads/videos/common/2FFE012B591F23F23C08EAB426A05760.flv?sc=0bfbf10a4e0080d2&br=746&vid=81682&aid=3261&area=US&vst=0
http://hc.yinyuetai.com/uploads/videos/common/812E0DF65EB6F409D6509DF3A055CCC5.flv?sc=a905fa6220d087a1&br=750&vid=75791&aid=3261&area=US&vst=0
http://hc.yinyuetai.com/uploads/videos/common/9720012AB24F21FF57EDD06ABFE6837B.flv?sc=6f0beb2e37137b9a&br=719&vid=71102&aid=3261&area=US&vst=3
http://hc.yinyuetai.com/uploads/videos/common/45E98A03439ACCB6EC980A4C95C66A9E.flv?sc=0b02bc8d993f38f9&br=1018&vid=63791&aid=3261&area=US&vst=0
http://hc.yinyuetai.com/uploads/videos/common/1DC5014C92F8C9E02930E871C989E8F1.flv?sc=c13ea42a543663b7&br=780&vid=45992&aid=3261&area=US&vst=2
http://hc.yinyuetai.com/uploads/videos/common/D76301286F11CDCFD042AA1DDBDAB597.flv?sc=26319f0244dac4e9&br=825&vid=43907&aid=3261&area=US&vst=0
http://hc.yinyuetai.com/uploads/videos/common/7F26012859AD14AB54D485451814D66F.flv?sc=8f27bf26aef8d604&br=693&vid=43230&aid=3261&area=US&vst=0
http://hc.yinyuetai.com/uploads/videos/common/E37A012859495D637F20172324E2CE9B.flv?sc=95d7043653d65cc3&br=698&vid=43157&aid=3261&area=US&vst=2
http://hc.yinyuetai.com/uploads/videos/common/2D5D0128504DC82670AFF27A0E61E120.flv?sc=4bd22020df702ab4&br=707&vid=43117&aid=3261&area=US&vst=2
http://hc.yinyuetai.com/uploads/videos/common/204D01304C8E6956193973FAFD75DC59.flv?sc=190e04e9d5b228c5&br=749&vid=34204&aid=3261&area=US&vst=0
http://hc.yinyuetai.com/uploads/videos/common/E4A10131DF3B5A9D2111C4FAFD4EB65D.flv?sc=24e22d730dbb8b58&br=692&vid=18361&aid=3261&area=US&vst=0
http://hc.yinyuetai.com/uploads/videos/common/9E9F013690E3E9ACEA2E55CE4505354F.flv?sc=0cb571db00833889&br=714&vid=3568&aid=3261&area=US&vst=0
'''
mv_url_str = '''http://hc.yinyuetai.com/uploads/videos/common/86900164CC71FF82DC712A39B0E55A91.mp4?sc=4521e1c57fb5d625&amp;br=781&amp;vid=3256571&amp;aid=3261&amp;area=US&amp;vst=3***http://hc.yinyuetai.com/uploads/videos/common/3307016449C2118C6CE9BAC10AF68D45.mp4?sc=93b7d66a8412b1bc&amp;br=781&amp;vid=3220229&amp;aid=3261&amp;area=US&amp;vst=0***http://hc.yinyuetai.com/uploads/videos/common/584701634D4C1263EE05F01850FD0BD5.mp4?sc=bfea3159b79d8ba2&amp;br=785&amp;vid=3210096&amp;aid=3261&amp;area=US&amp;vst=3***http://hc.yinyuetai.com/uploads/videos/common/CBFD0160318F30A1A4FB75282E184294.mp4?sc=5a6175feca721b5f&amp;br=777&amp;vid=3108153&amp;aid=3261&amp;area=US&amp;vst=0***http://hc.yinyuetai.com/uploads/videos/common/47A6015F4E60D98DEB8CCBDD9B54E7D7.mp4?sc=e7d30450c4633c9b&amp;br=781&amp;vid=3073533&amp;aid=3261&amp;area=US&amp;vst=2***http://hc.yinyuetai.com/uploads/videos/common/612E015E7124F3026DE451DB2FE6EF3D.mp4?sc=b0f2354048e17cb5&amp;br=777&amp;vid=3039990&amp;aid=3261&amp;area=US&amp;vst=3***http://hc.yinyuetai.com/uploads/videos/common/B053015E242B5D70FB7A5A18D89C8C71.mp4?sc=8e8c3dbec66f8d06&amp;br=779&amp;vid=3027519&amp;aid=3261&amp;area=US&amp;vst=3***http://hc.yinyuetai.com/uploads/videos/common/7AAD01590D9DD76D6D2B464FAB695870.mp4?sc=82a6a5a489bce1be&br=752&vid=2752729&aid=3261&area=US&vst=3***http://hc.yinyuetai.com/uploads/videos/common/488701574BA002DE615F95F6E8997726.flv?sc=d5e0768cbcd2e870&br=781&vid=2683770&aid=3261&area=US&vst=3***http://hc.yinyuetai.com/uploads/videos/common/C29401590D9E4CCC379F733147B5E781.mp4?sc=31912dcab32aebd2&br=745&vid=2752730&aid=3261&area=US&vst=3***http://hc.yinyuetai.com/uploads/videos/common/CE6C01590D9F2464BE7B3A6429419578.mp4?sc=0adf05e49343fdfc&br=743&vid=2752731&aid=3261&area=US&vst=3***http://hc.yinyuetai.com/uploads/videos/common/B0A601590D9F9935859F7168D7400323.mp4?sc=285c87ddebc2f418&br=777&vid=2752807&aid=3261&area=US&vst=3***http://hc.yinyuetai.com/uploads/videos/common/B6ED01590DA0269C6C84C6573AC1AE86.mp4?sc=8c76f8c505b62f9e&br=747&vid=2752808&aid=3261&area=US&vst=3***http://hc.yinyuetai.com/uploads/videos/common/0B8A01590DA0D1227880104A4685F0FC.mp4?sc=2de06dc75fa66ab4&br=743&vid=2752809&aid=3261&area=US&vst=3***http://hc.yinyuetai.com/uploads/videos/common/C7E201574B97D9E2C1FE21301150FF10.flv?sc=4069fdd95ea1f0fc&br=780&vid=2683753&aid=3261&area=US&vst=2***http://hc.yinyuetai.com/uploads/videos/common/5A3A01574B8DB3D08AF361054B934A4E.flv?sc=7e296dd5a6422736&br=779&vid=2683744&aid=3261&area=US&vst=2***http://hc.yinyuetai.com/uploads/videos/common/A2CC01574B8835AA5FD0155C2F407794.flv?sc=5ef6befbfa1a790d&br=786&vid=2683730&aid=3261&area=US&vst=2***http://hc.yinyuetai.com/uploads/videos/common/02C301561173181457C13EECFD060E19.flv?sc=52911e83330964fa&br=779&vid=2626614&aid=3261&area=US&vst=3***http://hc.yinyuetai.com/uploads/videos/common/379E01542CF14665BBB84E806E505BDB.flv?sc=b9a54b6fe4e23960&br=780&vid=2551183&aid=3261&area=US&vst=3***http://hc.yinyuetai.com/uploads/videos/common/083401542CEEFC7BCDA3C7D917D7E523.flv?sc=bd538ec8c092c29c&br=784&vid=2551173&aid=3261&area=US&vst=3***http://hc.yinyuetai.com/uploads/videos/common/6441015413F1E4C0CC372801280CCA49.flv?sc=8aa286dbb7904604&br=780&vid=2546866&aid=3261&area=US&vst=3***http://hc.yinyuetai.com/uploads/videos/common/FCB5015413EC18B49ACF65A5093E5E02.flv?sc=8937577ea7bca0a6&br=782&vid=2546846&aid=3261&area=US&vst=3***http://hc.yinyuetai.com/uploads/videos/common/1F1A01516215A9016083C53ACA9F5FA6.flv?sc=1d6fb1a80df890ce&br=779&vid=2437962&aid=3261&area=US&vst=3***http://hc.yinyuetai.com/uploads/videos/common/4C50015137E99C52BBD0C807270CC20A.flv?sc=d8f0b3c953d7b00b&br=776&vid=2430063&aid=3261&area=US&vst=3***http://hc.yinyuetai.com/uploads/videos/common/61F5015137C2705FEEC40C58D3939F54.flv?sc=5066850e864492c5&br=778&vid=2430058&aid=3261&area=US&vst=0***http://hc.yinyuetai.com/uploads/videos/common/65890150CCEE99A0A0572C6E2EC5CEBC.flv?sc=94c75073786040be&br=777&vid=2410246&aid=3261&area=US&vst=2***http://hc.yinyuetai.com/uploads/videos/common/FC0101503B58D2414DEC3A2292B8C26F.flv?sc=bce36d038f56c08c&br=780&vid=2387860&aid=3261&area=US&vst=3***http://hc.yinyuetai.com/uploads/videos/common/40BB014FCAB93AA404F4122A7BB76289.flv?sc=545701fcf0280ecb&br=779&vid=2370681&aid=3261&area=US&vst=3***http://hc.yinyuetai.com/uploads/videos/common/2B96014EF18D3729DA579F14C9D6A9B3.flv?sc=efdf8f19c937cdb3&br=781&vid=2343333&aid=3261&area=US&vst=3***http://hc.yinyuetai.com/uploads/videos/common/7E43014EF183243E916C028B2C60C056.flv?sc=bf37016fe110cab8&br=779&vid=2343314&aid=3261&area=US&vst=3***http://hc.yinyuetai.com/uploads/videos/common/B6A9014EE74F2607F41DEB1478A6547F.flv?sc=983cf6aaf0139936&br=780&vid=2342009&aid=3261&area=US&vst=3***http://hc.yinyuetai.com/uploads/videos/common/7972014EE735838AC1B842A66FE3C0DA.flv?sc=d109ae4f0829b6eb&br=781&vid=2341988&aid=3261&area=US&vst=3***http://hc.yinyuetai.com/uploads/videos/common/1BD8014ED014CB51FCFB6D2876D8B6B9.flv?sc=7027ed252c44ef92&br=779&vid=2338413&aid=3261&area=US&vst=3***http://hc.yinyuetai.com/uploads/videos/common/237D014E695ED7F5D128A2519F533AAF.flv?sc=c08d1ea5e81c97e4&br=778&vid=2325305&aid=3261&area=US&vst=3***http://hc.yinyuetai.com/uploads/videos/common/FCC5014E62749B8DA9EF4C7D3300B174.flv?sc=61057e45e36bcb3a&br=780&vid=2324240&aid=3261&area=US&vst=3***http://hc.yinyuetai.com/uploads/videos/common/9441014CC608B1055FEA4F8CDEB85E89.flv?sc=8258dd1a633dc88c&br=780&vid=2274824&aid=3261&area=US&vst=3***http://hc.yinyuetai.com/uploads/videos/common/F1A0014C5948708B24C03670E38481A2.flv?sc=89879a552b45b0a1&br=779&vid=2263238&aid=3261&area=US&vst=2***http://hc.yinyuetai.com/uploads/videos/common/D54B014C50303BFD9CB359D01B24B858.flv?sc=ca5dc60d00b5903c&br=778&vid=2262326&aid=3261&area=US&vst=3***http://hc.yinyuetai.com/uploads/videos/common/4F03014C361EF45382A3D6B205DB11A3.flv?sc=4a0f229e7f0af838&br=779&vid=2258931&aid=3261&area=US&vst=2***http://hc.yinyuetai.com/uploads/videos/common/5D34014BB58497B7EA2BBA8B239DB3AD.flv?sc=f47558d50f1964e0&br=788&vid=2244030&aid=3261&area=US&vst=3***http://hc.yinyuetai.com/uploads/videos/common/A0C5014B8101E6C85C05122178968995.flv?sc=4354c60828d9a229&br=778&vid=2239773&aid=3261&area=US&vst=2***http://hc.yinyuetai.com/uploads/videos/common/034D014B3695C712D4F47D0BBF38598B.flv?sc=b53c36e73ab027fe&br=779&vid=2230161&aid=3261&area=US&vst=3***http://hc.yinyuetai.com/uploads/videos/common/93CF014A300FAA93A4877AAF2A6CAB50.flv?sc=214b9ce50fb76253&br=777&vid=2198617&aid=3261&area=US&vst=3***http://hc.yinyuetai.com/uploads/videos/common/9A1601497D2CFD160257B14908455DA4.flv?sc=bca4c1fcb40833bf&br=777&vid=2174732&aid=3261&area=US&vst=3***http://hc.yinyuetai.com/uploads/videos/common/03E401467FC9AB66408F910055E24B1E.flv?sc=093d464f6fa424fb&br=746&vid=2069794&aid=3261&area=US&vst=3***http://hc.yinyuetai.com/uploads/videos/common/A94101465AFB0D2254B089DF2332B7DA.flv?sc=7918d326cfdf0a6a&br=778&vid=2064330&aid=3261&area=US&vst=3***http://hc.yinyuetai.com/uploads/videos/common/71E10145AC7CA1155ED983CEFCE8F5CB.flv?sc=20163ee6e00952de&br=778&vid=2042283&aid=3261&area=US&vst=3***http://hc.yinyuetai.com/uploads/videos/common/404C0145AC2CFA6ADA56B4BF60F7AB12.flv?sc=2d092b09e19ae1ed&br=775&vid=2042216&aid=3261&area=US&vst=3***http://hc.yinyuetai.com/uploads/videos/common/6A180145A6F44ECF310345870B8C0265.flv?sc=92fa7575542b9d42&br=777&vid=2041374&aid=3261&area=US&vst=3***http://hc.yinyuetai.com/uploads/videos/common/92DE0145A66CCF4D4B4CB035DDDDB442.flv?sc=929b6ec39ad5dae0&br=779&vid=2041234&aid=3261&area=US&vst=3***http://hc.yinyuetai.com/uploads/videos/common/312A01459BD2456BA615F0150CDEEC68.flv?sc=9f08e9d8277a804d&br=779&vid=2039697&aid=3261&area=US&vst=3***http://hc.yinyuetai.com/uploads/videos/common/C99701452105CF4989657D2D94ABFD65.flv?sc=d689f56f5b239306&br=779&vid=2023678&aid=3261&area=US&vst=3***http://hc.yinyuetai.com/uploads/videos/common/E9690142B81173A465F2FFC0C0B8CB0B.flv?sc=031466237beae016&br=778&vid=825269&aid=3261&area=US&vst=3***http://hc.yinyuetai.com/uploads/videos/common/B8B701425FE51FF43A41CAF56938FBEA.flv?sc=b5e0bb5164ef8847&br=778&vid=812382&aid=3261&area=US&vst=2***http://hc.yinyuetai.com/uploads/videos/common/0DEE01425FC16B3044C32E941929A985.flv?sc=40449d1fc64f48e6&br=788&vid=812341&aid=3261&area=US&vst=2***http://hc.yinyuetai.com/uploads/videos/common/1DB201423B5782F67FF95134CDA45369.flv?sc=ed11187b51514168&br=780&vid=807084&aid=3261&area=US&vst=3***http://hc.yinyuetai.com/uploads/videos/common/78FD01423B3B216D25F7AF2ADF2F3008.flv?sc=9dc0e56adda86a16&br=780&vid=807067&aid=3261&area=US&vst=3***http://hc.yinyuetai.com/uploads/videos/common/C7C401423AFB0B2F04CF75F2C2CBEE40.flv?sc=1703a1c3b96d25c1&br=779&vid=807039&aid=3261&area=US&vst=3***http://hc.yinyuetai.com/uploads/videos/common/397F01423ADBEA6EEA07B55FCC492C95.flv?sc=e495cdb4f7a54f36&br=779&vid=807005&aid=3261&area=US&vst=3***http://hc.yinyuetai.com/uploads/videos/common/58670141F94354B8F1C24FEB5A59F214.flv?sc=9f7c40b678584011&br=773&vid=797550&aid=3261&area=US&vst=0***http://hc.yinyuetai.com/uploads/videos/common/D6480140FD7336D1D788C9443F156BED.flv?sc=dd978c6d05fb22b9&br=778&vid=760738&aid=3261&area=US&vst=3***http://hc.yinyuetai.com/uploads/videos/common/4D290140EF87F7CF4971454B8DDF914F.flv?sc=ee2861e571ad56fb&br=778&vid=758060&aid=3261&area=US&vst=2***http://hc.yinyuetai.com/uploads/videos/common/5C460140EF49B85A7415235F2D23C0DA.flv?sc=65203bd177f5ca9a&br=776&vid=758041&aid=3261&area=US&vst=2***http://hc.yinyuetai.com/uploads/videos/common/A320013F716D5D49F6D7D211B8C14434.flv?sc=35216cdb644b11bb&br=777&vid=695649&aid=3261&area=US&vst=3***http://hc.yinyuetai.com/uploads/videos/common/8C98013F42BC3D4A38E18BC8C64EBBFC.flv?sc=13b93d0750dbd5ab&br=776&vid=688529&aid=3261&area=US&vst=2***http://hc.yinyuetai.com/uploads/videos/common/8859013F41C8BB7252FC8461AB8CF7EC.flv?sc=10288696023d6dba&br=783&vid=687480&aid=3261&area=US&vst=3***http://hc.yinyuetai.com/uploads/videos/common/7F62013F29268E98DF335EBA8281210D.flv?sc=a3d23d710685e288&br=778&vid=685679&aid=3261&area=US&vst=3***http://hc.yinyuetai.com/uploads/videos/common/B42B013F1A10DCD0B7E24175A9380C4F.flv?sc=18242caba899e018&br=779&vid=681676&aid=3261&area=US&vst=2***http://hc.yinyuetai.com/uploads/videos/common/51C6013F19F9F982F699E1478E317908.flv?sc=206aefd752f20e27&br=778&vid=681673&aid=3261&area=US&vst=3***http://hc.yinyuetai.com/uploads/videos/common/AC40013F197C8EE92E34CDAED60341F1.flv?sc=13fb58034e358b2f&br=780&vid=681573&aid=3261&area=US&vst=3***http://hc.yinyuetai.com/uploads/videos/common/154A013EF948396DA91E5813A3F4A0FC.flv?sc=9f74ff3f6b8e0660&br=777&vid=677197&aid=3261&area=US&vst=3***http://hc.yinyuetai.com/uploads/videos/common/1A99013EF9A2DD1DE3F8089D9B74A978.flv?sc=448a5c300c3ebbc4&br=779&vid=677196&aid=3261&area=US&vst=3***http://hc.yinyuetai.com/uploads/videos/common/59AD013EF9CA3B1CF9B99227389E0393.flv?sc=23e55a232eb5f135&br=779&vid=677195&aid=3261&area=US&vst=3***http://hc.yinyuetai.com/uploads/videos/common/D49B013EF9C69097A0BFCF32C5B38436.flv?sc=f2c1875fc0c04586&br=779&vid=677191&aid=3261&area=US&vst=3***http://hc.yinyuetai.com/uploads/videos/common/E37F013EF9CECDF42937F6DB4AA23B69.flv?sc=1659cf441718bed3&br=778&vid=677190&aid=3261&area=US&vst=3***http://hc.yinyuetai.com/uploads/videos/common/BE3A013D8966AC65FA9C550397988E67.flv?sc=8bd1ac03ad2bd1d1&br=1172&vid=673543&aid=3261&area=US&vst=1***http://hc.yinyuetai.com/uploads/videos/common/D92E013EE5440482A612095C9E61AE7B.flv?sc=ae227627919f6955&br=777&vid=673309&aid=3261&area=US&vst=3***http://hc.yinyuetai.com/uploads/videos/common/07F2013C61F435EAE19685100604B4B8.flv?sc=9800a9d79f0ea265&br=778&vid=591744&aid=3261&area=US&vst=3***http://hc.yinyuetai.com/uploads/videos/common/701C013C5D2EE7EA6EC1941366EC971A.flv?sc=9e12bd716d51c2bf&br=778&vid=591044&aid=3261&area=US&vst=3***http://hc.yinyuetai.com/uploads/videos/common/7839013C4C15C2CE752669D9B36EF09A.flv?sc=7a5e67ad4d692e8f&br=778&vid=588256&aid=3261&area=US&vst=3***http://hc.yinyuetai.com/uploads/videos/common/4466013B9B168D8728681C0E4216A329.flv?sc=5f9ed23d521bf314&br=1075&vid=566106&aid=3261&area=US&vst=0***http://hc.yinyuetai.com/uploads/videos/common/A333013F704C141DC2F93762096B62EC.flv?sc=a82d28e819bdd08e&br=775&vid=549044&aid=3261&area=US&vst=0***http://hc.yinyuetai.com/uploads/videos/common/8647013A88DB0D0E3CDB497F88346B2C.flv?sc=fab40b31b863c3c7&br=774&vid=535947&aid=3261&area=US&vst=0***http://hc.yinyuetai.com/uploads/videos/common/BA6A013A73EE336DA688485BD2FA5A9F.flv?sc=ddca1f2ad391ac15&br=778&vid=533786&aid=3261&area=US&vst=2***http://hc.yinyuetai.com/uploads/videos/common/8230013A7745536D436B3F6E40C31ADB.flv?sc=b860033d9ed37c22&br=777&vid=533779&aid=3261&area=US&vst=3***http://hc.yinyuetai.com/uploads/videos/common/B4AD013A11A4BEEBB2255B289E8F96AA.flv?sc=11ca8b69d240b32d&br=777&vid=520109&aid=3261&area=US&vst=0***http://hc.yinyuetai.com/uploads/videos/common/194C0136D2834C8EA8A38E1A8E24C627.flv?sc=cab29ada35ce731b&br=712&vid=399077&aid=3261&area=US&vst=0***http://hc.yinyuetai.com/uploads/videos/common/14420136AEF75556D3697B71131CC396.flv?sc=61c83c95ee1b8e86&br=714&vid=394478&aid=3261&area=US&vst=3***http://hc.yinyuetai.com/uploads/videos/common/E1DA0136AC84F916414415CAEC2E7470.flv?sc=d02e0da8261b2100&br=717&vid=394317&aid=3261&area=US&vst=0***http://hc.yinyuetai.com/uploads/videos/common/FD4B013694A7FCBE94A28EF721EA0381.flv?sc=afe9c539f28308a0&br=713&vid=391636&aid=3261&area=US&vst=2***http://hc.yinyuetai.com/uploads/videos/common/2F66013691312F744F61FF3CE41E8966.flv?sc=f673c58faeefe12f&br=714&vid=390670&aid=3261&area=US&vst=0***http://hc.yinyuetai.com/uploads/videos/common/DB06013690F3901368EEC737D4CD1925.flv?sc=bce49dbee404322e&br=717&vid=390652&aid=3261&area=US&vst=2***http://hc.yinyuetai.com/uploads/videos/common/B235013690F42E5A26A08B1F2F1BA330.flv?sc=286a646b11da1154&br=714&vid=390607&aid=3261&area=US&vst=0***http://hc.yinyuetai.com/uploads/videos/common/1EEC013687E80FC3967BFEF3BE2BBCEB.flv?sc=9e1b1cf6365c45c0&br=714&vid=388636&aid=3261&area=US&vst=2***http://hc.yinyuetai.com/uploads/videos/common/ACBB01365D3069E7ED4A6DB89BF7F2DE.flv?sc=484ed03a2ed2a380&br=713&vid=383260&aid=3261&area=US&vst=0***http://hc.yinyuetai.com/uploads/videos/common/5788013CB4FA2E39D35CBC058765DF30.flv?sc=f1b5a5898304f774&br=780&vid=379001&aid=3261&area=US&vst=3***http://hc.yinyuetai.com/uploads/videos/common/B9A501361919668EA0BF4180A8D08760.flv?sc=92efa30356a8f98d&br=714&vid=374312&aid=3261&area=US&vst=0***http://hc.yinyuetai.com/uploads/videos/common/40F901361953C48BAFC595A2724FCF58.flv?sc=84c51ae16bd0c925&br=714&vid=374290&aid=3261&area=US&vst=0***http://hc.yinyuetai.com/uploads/videos/common/82710135DC317017F4F592D06FB7EBB7.flv?sc=41d7d4d6585dd0a9&br=742&vid=367019&aid=3261&area=US&vst=1***http://hc.yinyuetai.com/uploads/videos/common/A02C0135B018BCF8E35C4CD8F6463731.flv?sc=b6cf8749df36c21e&br=505&vid=361290&aid=3261&area=US&vst=3***http://hc.yinyuetai.com/uploads/videos/common/8F9D013581389A41C77059A959E2084D.flv?sc=f8807e0ad646ce34&br=679&vid=355698&aid=3261&area=US&vst=2***http://hc.yinyuetai.com/uploads/videos/common/F18601358137E887A556ABAA1E83E0F3.flv?sc=406e02b2cb59ff43&br=713&vid=355690&aid=3261&area=US&vst=2***http://hc.yinyuetai.com/uploads/videos/common/169C013555CAA6122636274A25CAE445.flv?sc=312d71716a133e39&br=639&vid=348461&aid=3261&area=US&vst=2***http://hc.yinyuetai.com/uploads/videos/common/98AF013CAC689308E94336CA058798C1.flv?sc=2183a14b638e5772&br=777&vid=346306&aid=3261&area=US&vst=0***http://hc.yinyuetai.com/uploads/videos/common/732E01354141F0A1F344B04B51B1C6A3.flv?sc=85d5472a2d75b38b&br=486&vid=345819&aid=3261&area=US&vst=3***http://hc.yinyuetai.com/uploads/videos/common/ADB4013541410C8443789F93D2478C9A.flv?sc=53dca8430cd84119&br=592&vid=345818&aid=3261&area=US&vst=0***http://hc.yinyuetai.com/uploads/videos/common/2196013532E369BEAD6E43E341B61A98.flv?sc=84bc0aab9e7d251e&br=632&vid=342298&aid=3261&area=US&vst=0***http://hc.yinyuetai.com/uploads/videos/common/7614013454D963BAED8DE545853727BE.flv?sc=58bc2bc6fabd0358&br=714&vid=327172&aid=3261&area=US&vst=2***http://hc.yinyuetai.com/uploads/videos/common/EF9501345467D9630CAA581B34EA851F.flv?sc=c0e553301b3dc5dd&br=716&vid=327125&aid=3261&area=US&vst=2***http://hc.yinyuetai.com/uploads/videos/common/6338013451C1DDA444EE48EFCB8E64B9.flv?sc=2b32c90c8ffed7b0&br=717&vid=326787&aid=3261&area=US&vst=2***http://hc.yinyuetai.com/uploads/videos/common/48580134511DBFD0B6EC4BD667254A13.flv?sc=3eaa2d3893887631&br=718&vid=326776&aid=3261&area=US&vst=2***http://hc.yinyuetai.com/uploads/videos/common/2A30013450F722735570CA7CA8C970FB.flv?sc=cffb8180f4292347&br=716&vid=326759&aid=3261&area=US&vst=2***http://hc.yinyuetai.com/uploads/videos/common/9B4A013423C53D9DC37D692880BA498C.flv?sc=c539e58f6ca0dcff&br=633&vid=320567&aid=3261&area=US&vst=3***http://hc.yinyuetai.com/uploads/videos/common/1E570133FD615157ABB5E65BD164DF7C.flv?sc=cf158285cdddd9f5&br=715&vid=315249&aid=3261&area=US&vst=2***http://hc.yinyuetai.com/uploads/videos/common/2B82013234405854BB0AD5B580EBB8F1.flv?sc=f84654d0f22354f5&br=684&vid=259124&aid=3261&area=US&vst=2***http://hc.yinyuetai.com/uploads/videos/common/783E01318BDBD8DDACC52A9ADC12C8FF.flv?sc=456757aba17a956e&br=684&vid=229603&aid=3261&area=US&vst=2***http://hc.yinyuetai.com/uploads/videos/common/6B34012F247264AF920970744F011026.flv?sc=5a86d83e3094b7d8&br=745&vid=158736&aid=3261&area=US&vst=1***http://hc.yinyuetai.com/uploads/videos/common/26F4012F388AD0C40B47DBAE780A461E.flv?sc=1719de01bebdaad1&br=739&vid=158005&aid=3261&area=US&vst=3***http://hc.yinyuetai.com/uploads/videos/common/81000BCA562FC8895B3623E62CED96DA.flv?sc=258ca046c2807e07&br=698&vid=157834&aid=3261&area=US&vst=0***http://hc.yinyuetai.com/uploads/videos/common/C64D01375F81EFC0F3BD24A4980790CE.flv?sc=495bef8f927b88c2&br=752&vid=133306&aid=3261&area=US&vst=0***http://hc.yinyuetai.com/uploads/videos/common/A10E012E31245AC5B5CFC87739AA2263.flv?sc=91102f89efd7b72d&br=748&vid=132885&aid=3261&area=US&vst=2***http://hc.yinyuetai.com/uploads/videos/common/57B1012BA21F0C655CB007200AE07B5B.flv?sc=a2d253289894a74f&br=760&vid=85925&aid=3261&area=US&vst=0***http://hc.yinyuetai.com/uploads/videos/common/58C4012B92EE88501BDC1C0188EDFDBC.flv?sc=0bde8015cd98268a&br=733&vid=85227&aid=3261&area=US&vst=0***http://hc.yinyuetai.com/uploads/videos/common/F431012B85D38EC78F7A5DB7B431F25E.flv?sc=629006f78f86b573&br=752&vid=84446&aid=3261&area=US&vst=2***http://hc.yinyuetai.com/uploads/videos/common/401BA40DACDBECC5C2FEC93207C53452.flv?sc=b2a610198d8fa94e&br=749&vid=84252&aid=3261&area=US&vst=3***http://hc.yinyuetai.com/uploads/videos/common/739A012B85E8A3DF3A86359E51EC9395.flv?sc=fa07d2e57bb79a10&br=751&vid=84157&aid=3261&area=US&vst=0***http://hc.yinyuetai.com/uploads/videos/common/FA24012B85E9D0C685E927D267644809.flv?sc=f68145f662e77ecb&br=744&vid=84074&aid=3261&area=US&vst=0***http://hc.yinyuetai.com/uploads/videos/common/02E6012B8204589A53D3D49980B9A760.flv?sc=34a5aa25d0c83beb&br=759&vid=83943&aid=3261&area=US&vst=0***http://hc.yinyuetai.com/uploads/videos/common/2FFE012B591F23F23C08EAB426A05760.flv?sc=0bfbf10a4e0080d2&br=746&vid=81682&aid=3261&area=US&vst=0***http://hc.yinyuetai.com/uploads/videos/common/812E0DF65EB6F409D6509DF3A055CCC5.flv?sc=a905fa6220d087a1&br=750&vid=75791&aid=3261&area=US&vst=0***http://hc.yinyuetai.com/uploads/videos/common/9720012AB24F21FF57EDD06ABFE6837B.flv?sc=6f0beb2e37137b9a&br=719&vid=71102&aid=3261&area=US&vst=3***http://hc.yinyuetai.com/uploads/videos/common/45E98A03439ACCB6EC980A4C95C66A9E.flv?sc=0b02bc8d993f38f9&br=1018&vid=63791&aid=3261&area=US&vst=0***http://hc.yinyuetai.com/uploads/videos/common/1DC5014C92F8C9E02930E871C989E8F1.flv?sc=c13ea42a543663b7&br=780&vid=45992&aid=3261&area=US&vst=2***http://hc.yinyuetai.com/uploads/videos/common/D76301286F11CDCFD042AA1DDBDAB597.flv?sc=26319f0244dac4e9&br=825&vid=43907&aid=3261&area=US&vst=0***http://hc.yinyuetai.com/uploads/videos/common/7F26012859AD14AB54D485451814D66F.flv?sc=8f27bf26aef8d604&br=693&vid=43230&aid=3261&area=US&vst=0***http://hc.yinyuetai.com/uploads/videos/common/E37A012859495D637F20172324E2CE9B.flv?sc=95d7043653d65cc3&br=698&vid=43157&aid=3261&area=US&vst=2***http://hc.yinyuetai.com/uploads/videos/common/2D5D0128504DC82670AFF27A0E61E120.flv?sc=4bd22020df702ab4&br=707&vid=43117&aid=3261&area=US&vst=2***http://hc.yinyuetai.com/uploads/videos/common/204D01304C8E6956193973FAFD75DC59.flv?sc=190e04e9d5b228c5&br=749&vid=34204&aid=3261&area=US&vst=0***http://hc.yinyuetai.com/uploads/videos/common/E4A10131DF3B5A9D2111C4FAFD4EB65D.flv?sc=24e22d730dbb8b58&br=692&vid=18361&aid=3261&area=US&vst=0***http://hc.yinyuetai.com/uploads/videos/common/9E9F013690E3E9ACEA2E55CE4505354F.flv?sc=0cb571db00833889&br=714&vid=3568&aid=3261&area=US&vst=0'''


# mv_url_list = mv_url_str.split('***')
# index = 1
# for url in mv_url_list:
#     name = 'maksim' + str(index)
#     index += 1
#     print(name)
#     mv.download(url, name)

