import re

import requests
from lxml import etree


def gufengmh(mhname):
    try:
        global xq, header
        url = "https://m.gufengmh.com/search/?keywords="
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
        }
        # mhname = input("请在下方输入漫画名称：\n")
        request_mhurl = url + mhname
        res = requests.get(request_mhurl, headers=header)
        tree = etree.HTML(res.content)
        xq = tree.xpath('//*[@id="update_list"]/div/div/div[1]/a/@href')
        zxz = tree.xpath('//*[@id="update_list"]/div/div/a/text()')  # 最新章节
        mz = tree.xpath('//*[@id="update_list"]/div/div/div/a/text()')  # 漫画名称
        fm = tree.xpath('//*[@id="update_list"]//div/a/mip-img/@src')  # 封面
        zz = tree.xpath('//*[@id="update_list"]//div/p[1]/text()')  # 作者
        bq = tree.xpath('//*[@id="update_list"]//div/p[2]/span/text()')  # 标签
        gxsj = tree.xpath('//*[@id="update_list"]//div/p[3]/span/text()')  # 更新时间
        json = []
        for (m, x, f, z, b, g, zx) in zip(mz, xq, fm, zz, bq, gxsj, zxz):
            json.append({'name': m, 'url': x, 'cover': f, 'author': z, 'tag': b, 'time': g, 'latest': zx})
        print(json)
        return json
    except:
        return ''


def nr(url):
    try:
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
        }
        res = requests.get(url, headers=header, timeout=5)
        tree = etree.HTML(res.content)
        mz = tree.xpath('//*[@class="Drama autoHeight"]/li/a/span/text()')
        js = tree.xpath('//*[@class="Drama autoHeight"]/li/a/@href')
        jj = tree.xpath('/html/body/div[3]/p/text()')[0].strip()  # 简介
        # zt = tree.xpath('//ul[@class="detail-list cf"]/li[1]/span[1]/a/text()')[0]
        sj = tree.xpath('/html/body/div[3]/div[1]/div/dl[4]/dd/text()')[0]  # 时间
        mzz = tree.xpath('/html/body/div[3]/div[1]/h1/text()')[0]  # 漫画名称
        fm = tree.xpath('//*[@id="Cover"]/mip-img/@src')[0]  # 封面
        zz = tree.xpath('/html/body/div[3]/div[1]/div/dl[2]/dd/text()')[0]  # 作者
        bq = tree.xpath('/html/body/div[3]/div[1]/div/dl[3]/dd/text()')[0]  # 标签
        mzjs = {'data': {'time': sj, 'introduce': jj, 'name': mzz, 'cover': fm, 'author': zz, 'tag': bq}}
        mzjss = []
        for (m, j) in zip(mz, js):
            mzjss.append({'num': m, 'url': 'gfmh' + j})
        mzjs['list'] = mzjss
        print(mzjs)
        return mzjs
    except:
        return 'null'


def gk(urll):  # 给集数地址，获取地址
    try:
        url = "https://m.gufengmh.com" + urll.replace('gfmh', '')
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3676.400 QQBrowser/10.4.3469.400"
        }
        yss = requests.get(url, headers=header, timeout=5).text
        ys = re.findall('<script>;var chapterImages..*?;var pageTitle', yss, re.S)[0]
        tpurl1 = re.findall('"(\d{4,}.*?.jpg)"', ys, re.S)
        tpurl2 = re.findall('chapterPath = "(.*?)";', ys, re.S)[0]
        tpurl = []
        for i in tpurl1:
            tpurl.append('https://res.gufengmh.com/' + tpurl2 + i)
        tpurll = []
        for i in tpurl:
            tpurll.append({'img': i})
        tpurl = {'list': tpurll}
        print(tpurl)
        return tpurl
    except:
        return ''


if __name__ == "__main__":
    gufengmh('斗破苍穹')
    nr('https://m.gufengmh.com/manhua/douluodalu4zhongjidouluo/')
    gk('/manhua/anbingdasheng/710943.html')
