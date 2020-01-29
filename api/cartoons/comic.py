import requests
from lxml import etree


def get_mhname():
    try:
        url = 'https://18comic.live/'
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
        }
        res = requests.get(url, headers=header)
        tree = etree.HTML(res.content)
        names = tree.xpath('//*[@class="video-title title-truncate m-t-5"]/text()')
        href = tree.xpath('//*[@class="well well-sm"]/a/@href')
        cover = tree.xpath('//*[@class="well well-sm"]//div/img/@src')
        author = tree.xpath('//*[@class="well well-sm"]/div[1]/a/text()')
        time = tree.xpath('//*[@class="video-views pull-left"]/text()')
        json = []
        for (m, x, c, a, t) in zip(names, href, cover, author, time):
            # json.append({'name': m, 'url': x, 'cover': f, 'author': z, 'tag': b, 'time': g, 'latest': zx})
            json.append({'name': m, 'url': url + x, 'cover': c, 'author': a, 'time': t})
        print(json)
        return json
    except:
        print('出现错误')
        return 'null'


def mhurl1(url1):
    try:
        url = 'https://18comic.live'
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
        }
        res = requests.get(url1, headers=header)
        tree = etree.HTML(res.content)
        go_url = tree.xpath('//*[@class="btn btn-primary dropdown-toggle"][1]/@href')
        for i in go_url:
            urls = url + i
        ress = requests.get(urls, headers=header)
        trees = etree.HTML(ress.content)
        names = trees.xpath('//*[@class="top-comname"]/text()')
        imgs_url = trees.xpath('//*[@style="text-align:center;"]/img/@src')
        url1_json = []
        for i in imgs_url:
            url1_json.append({'img': i})
        print(url1_json)
        return url1_json
    except:
        print('出现错误')
        return 'null'


def search_photos(search_query):
    try:
        urls = 'https://18comic.live'
        url = 'https://18comic.live/search/photos?'
        search_querys = 'search_query=' + search_query
        urlss = url + search_querys
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
        }
        res = requests.get(urlss, headers=header)
        tree = etree.HTML(res.content)
        name = tree.xpath('//*[@class="video-title title-truncate m-t-5"]/text()')
        href = tree.xpath('//*[@class="well well-sm"]/a/@href')
        cover = tree.xpath('//*[@class="lazy_img img-responsive "]/@data-original')
        time = tree.xpath('//*[@class="video-views pull-left"]/text()')
        json = []
        for (n, h, c, t) in zip(name, href, cover, time):
            json.append({'name': n, 'url': urls + h, 'cover': c, 'time': t})
        print(json)
        return json
    except:
        print('出现错误')
        return 'null'

if __name__ == '__main__':
    search_photos('少女前线')
    print('获取最新漫画中\n')
    get_mhname()
    urls = input('请输入漫画url:\n')
    mhurl1(urls)
