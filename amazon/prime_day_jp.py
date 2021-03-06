import numpy as np
import pandas as pd
import requests, lxml
from lxml import etree
import re, time, random, datetime, time


class AmazonGoods:
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763"
    }
    proxies = {
        "http": "http://114.239.3.156:9999",
    }

    url_base = "https://www.amazon.co.jp"
    s = requests.Session()
    s.get(url=url_base, headers=headers, proxies=proxies, verify=False)

    def __init__(self):
        self.goods_list = []

    def get_goods(self, url):

        res = self.s.get(url, headers=self.headers, proxies=self.proxies, verify=False)
        time.sleep(10)
        if res.status_code != 200:
            print("请求出错，状态码为：%s" % res.status_code)
            # print(res.text)
            return
        print(res.text)
        res_html = etree.HTML(res.text)

        # for each in res_html.xpath("//div[@class='a-row dealContainer dealTile']")[:3]:
        for each in res_html.xpath("//div[@class='a-section a-spacing-none tallCellView gridColumn4 singleCell']"):
            try:
                pic_url = each.xpath(".//a[@id='dealImage']/@href")
                print(pic_url)
            except:
                pic_url = None
            try:
                price = each.xpath(".//span[@class='a-size-medium inlineBlock unitLineHeight dealPriceText']/text()")
            except:
                price = None
            try:
                percent = each.xpath(".//span[class='a-size-mini a-color-secondary inlineBlock unitLineHeight']/text()")
            except:
                percent = None
            try:
                total = each.xpath(".//span[@class='a-size-mini a-color-secondary inlineBlock unitLineHeight']/text()")
            except:
                total = None
            try:
                end_time = each.xpath(".//span[@class='a-size-mini a-color-secondary inlineBlock unitLineHeight']/text()")
            except:
                end_time = None
            now_time = time.time()

            self.goods_list.append([pic_url, price, percent, total, end_time, now_time])
            print(self.goods_list[-1])


if __name__ == '__main__':
    jp = AmazonGoods()
    url = 'https://www.amazon.co.jp/b/ref=gbps_ftr_m-8_80f5_page_2?_encoding=UTF8&node=3959621051&pf_rd_p=aefa1709-255d-4840-931a-0a5d8c4b80f5&pf_rd_s=merchandised-search-8&pf_rd_t=101&pf_rd_i=3959621051&pf_rd_m=AN1VRQENFRJN5&pf_rd_r=5X74YF6W6A158HYC5HAN&gb_f_ALLDEALS=dealStates:AVAILABLE%252CWAITLIST%252CWAITLISTFULL%252CEXPIRED%252CSOLDOUT,dealTypes:LIGHTNING_DEAL%252CBEST_DEAL,page:2,sortOrder:BY_SCORE,enforcedCategories:3828871%252C14304371,dealsPerPage:40&ie=UTF8'
    jp.get_goods(url)