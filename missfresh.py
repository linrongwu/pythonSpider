#-*- coding: UTF-8 -*-
import requests
import xlwt


def product(sku,headers,data1):

    product_url = 'https://pagoda-buy-acc.pagoda.com.cn:11521/api/v1/goods/detail/-1/4/2130/' + sku
    product_req = requests.get(url=product_url, headers=headers, verify=False).json()
    data = product_req['data']
    goodsDesc = data['goodsDesc']

    level = goodsDesc['level']
    productionPlace = goodsDesc['productionPlace']
    spec = goodsDesc['spec']

    name = data['goodsName']
    originalPrice  = data['originalPrice']
    price = data['price']
    t = [name,productionPlace,level,spec,originalPrice,price]
    data1.append(t)



def typeproduct(heros_url,headers,data):
    req = requests.get(url=heros_url, headers=headers, verify=False)
    print(req.text)
    '''
    for each in req['data']:
        try:
            sku = each['goodsID']
        except KeyError:
            print('en')
        else:
            product(sku,headers,data)
    '''


if __name__ == '__main__':
    '''
    workbook = xlwt.Workbook()
    sheet1 = workbook.add_sheet('test', cell_overwrite_ok=True)
    '''
    data=[]


    headers = {
        'Accept-Encoding': 'gzip, deflate, br',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
        'Host': 'list.tmall.com',
        'Connection': 'Keep-Alive'}
    '''
    #百货
    heros_url = "https://list.tmall.com/search_product.htm?spm=a3204.7933263.0.0.be8120cSNtPHk&cat=50512020&sort=s&style=g&search_condition=1&user_id=725677994,1910146537,2136152958&active=1&industryCatId=50512020&smAreaId=420100"
    typeproduct(heros_url, headers,data)
    

    #蔬菜
    heros_url = "https://as-vip.missfresh.cn/v3/product/category/hn-sc?platform=android&android_channel_value=meizu&session=android865704033537268&tdk=eyJvcyI6ImFuZHJvaWQiLCJ2ZXJzaW9uIjoiMy4wLjkiLCJwYWNrYWdlcyI6ImNuLm1pc3NmcmVzaC5hcHBsaWNhdGlvbl83LjEuMiIsInByb2ZpbGVfdGltZSI6MTI5LCJpbnRlcnZhbF90aW1lIjoxNjUwMDgxLCJ0b2tlbl9pZCI6IjdkNUVcL00rUDIycVA0dlZqSzR6QVJcL0EwckNQVWc3MlNHS2ZjUlBvQVNHdVVYTlhESTR3TTNCM0wydXRodytGK2hwWFFRVkNUT0prck1kMzBwSExPXC93PT0ifQ==&imei=c8b4fc2cc6d7cf62732415b47d6e17b1&access_token=&SM_Device_ID=2017120509563811ea421cde6b0119309424539b447fd001201fe35ffea283&version=7.1.2&screen_width=720&screen_height=1280"
    typeproduct(heros_url, headers,f,data)

    #热卖
    heros_url = "https://as-vip.missfresh.cn/v3/product/category/hn-newsy?platform=android&android_channel_value=meizu&session=android865704033537268&tdk=eyJvcyI6ImFuZHJvaWQiLCJ2ZXJzaW9uIjoiMy4wLjkiLCJwYWNrYWdlcyI6ImNuLm1pc3NmcmVzaC5hcHBsaWNhdGlvbl83LjEuMiIsInByb2ZpbGVfdGltZSI6MTI5LCJpbnRlcnZhbF90aW1lIjoxNzIwMDk4LCJ0b2tlbl9pZCI6IjdkNUVcL00rUDIycVA0dlZqSzR6QVJcL0EwckNQVWc3MlNHS2ZjUlBvQVNHdVVYTlhESTR3TTNCM0wydXRodytGK2hwWFFRVkNUT0prck1kMzBwSExPXC93PT0ifQ==&imei=c8b4fc2cc6d7cf62732415b47d6e17b1&access_token=&SM_Device_ID=2017120509563811ea421cde6b0119309424539b447fd001201fe35ffea283&version=7.1.2&screen_width=720&screen_height=1280"
    typeproduct(heros_url, headers,f,data)

    #火锅
    heros_url = "https://as-vip.missfresh.cn/v3/product/category/hncrd-%E7%81%AB%E9%94%85?platform=android&android_channel_value=meizu&session=android865704033537268&tdk=eyJvcyI6ImFuZHJvaWQiLCJ2ZXJzaW9uIjoiMy4wLjkiLCJwYWNrYWdlcyI6ImNuLm1pc3NmcmVzaC5hcHBsaWNhdGlvbl83LjEuMiIsInByb2ZpbGVfdGltZSI6MTI5LCJpbnRlcnZhbF90aW1lIjoxNzA4NDUxLCJ0b2tlbl9pZCI6IjdkNUVcL00rUDIycVA0dlZqSzR6QVJcL0EwckNQVWc3MlNHS2ZjUlBvQVNHdVVYTlhESTR3TTNCM0wydXRodytGK2hwWFFRVkNUT0prck1kMzBwSExPXC93PT0ifQ==&imei=c8b4fc2cc6d7cf62732415b47d6e17b1&access_token=&SM_Device_ID=2017120509563811ea421cde6b0119309424539b447fd001201fe35ffea283&version=7.1.2&screen_width=720&screen_height=1280"
    typeproduct(heros_url, headers,f,data)

    #乳品
    heros_url = "https://as-vip.missfresh.cn/v3/product/category/hn--milk?platform=android&android_channel_value=meizu&session=android865704033537268&tdk=eyJvcyI6ImFuZHJvaWQiLCJ2ZXJzaW9uIjoiMy4wLjkiLCJwYWNrYWdlcyI6ImNuLm1pc3NmcmVzaC5hcHBsaWNhdGlvbl83LjEuMiIsInByb2ZpbGVfdGltZSI6MTMxLCJpbnRlcnZhbF90aW1lIjo1NjY2NCwidG9rZW5faWQiOiI3ZDVFXC9NK1AyMnFQNHZWaks0ekFSOVE0MlhIeHl5OTZ6cU5BeFhwSkJGNEZ5dHlMU285STJZNWRwdTdWRUFWdXRudzBvK2QrM3ZpN2syMVwvSVNNSXJBPT0ifQ==&imei=c8b4fc2cc6d7cf62732415b47d6e17b1&access_token=&SM_Device_ID=2017120509563811ea421cde6b0119309424539b447fd001201fe35ffea283&version=7.1.2&screen_width=720&screen_height=1280"
    typeproduct(heros_url, headers,f,data)

    # 零食
    heros_url = "https://as-vip.missfresh.cn/v3/product/category/hn--snack?platform=android&android_channel_value=meizu&session=android865704033537268&tdk=eyJvcyI6ImFuZHJvaWQiLCJ2ZXJzaW9uIjoiMy4wLjkiLCJwYWNrYWdlcyI6ImNuLm1pc3NmcmVzaC5hcHBsaWNhdGlvbl83LjEuMiIsInByb2ZpbGVfdGltZSI6MTMxLCJpbnRlcnZhbF90aW1lIjo1NjY2NCwidG9rZW5faWQiOiI3ZDVFXC9NK1AyMnFQNHZWaks0ekFSOVE0MlhIeHl5OTZ6cU5BeFhwSkJGNEZ5dHlMU285STJZNWRwdTdWRUFWdXRudzBvK2QrM3ZpN2syMVwvSVNNSXJBPT0ifQ==&imei=c8b4fc2cc6d7cf62732415b47d6e17b1&access_token=&SM_Device_ID=2017120509563811ea421cde6b0119309424539b447fd001201fe35ffea283&version=7.1.2&screen_width=720&screen_height=1280"
    typeproduct(heros_url, headers,f,data)

    #水产
    heros_url = "https://as-vip.missfresh.cn/v3/product/category/hn--seafood?platform=android&android_channel_value=meizu&session=android865704033537268&tdk=eyJvcyI6ImFuZHJvaWQiLCJ2ZXJzaW9uIjoiMy4wLjkiLCJwYWNrYWdlcyI6ImNuLm1pc3NmcmVzaC5hcHBsaWNhdGlvbl83LjEuMiIsInByb2ZpbGVfdGltZSI6MTMxLCJpbnRlcnZhbF90aW1lIjo1NjY2NCwidG9rZW5faWQiOiI3ZDVFXC9NK1AyMnFQNHZWaks0ekFSOVE0MlhIeHl5OTZ6cU5BeFhwSkJGNEZ5dHlMU285STJZNWRwdTdWRUFWdXRudzBvK2QrM3ZpN2syMVwvSVNNSXJBPT0ifQ==&imei=c8b4fc2cc6d7cf62732415b47d6e17b1&access_token=&SM_Device_ID=2017120509563811ea421cde6b0119309424539b447fd001201fe35ffea283&version=7.1.2&screen_width=720&screen_height=1280"
    typeproduct(heros_url, headers,f,data)

    #粮油
    heros_url = "https://as-vip.missfresh.cn/v3/product/category/hn--liangyou?platform=android&android_channel_value=meizu&session=android865704033537268&tdk=eyJvcyI6ImFuZHJvaWQiLCJ2ZXJzaW9uIjoiMy4wLjkiLCJwYWNrYWdlcyI6ImNuLm1pc3NmcmVzaC5hcHBsaWNhdGlvbl83LjEuMiIsInByb2ZpbGVfdGltZSI6MTMxLCJpbnRlcnZhbF90aW1lIjo1NjY2NCwidG9rZW5faWQiOiI3ZDVFXC9NK1AyMnFQNHZWaks0ekFSOVE0MlhIeHl5OTZ6cU5BeFhwSkJGNEZ5dHlMU285STJZNWRwdTdWRUFWdXRudzBvK2QrM3ZpN2syMVwvSVNNSXJBPT0ifQ==&imei=c8b4fc2cc6d7cf62732415b47d6e17b1&access_token=&SM_Device_ID=2017120509563811ea421cde6b0119309424539b447fd001201fe35ffea283&version=7.1.2&screen_width=720&screen_height=1280"
    typeproduct(heros_url, headers,f,data)

    #轻食
    heros_url = "https://as-vip.missfresh.cn/v3/product/category/hn-qingshi?platform=android&android_channel_value=meizu&session=android865704033537268&tdk=eyJvcyI6ImFuZHJvaWQiLCJ2ZXJzaW9uIjoiMy4wLjkiLCJwYWNrYWdlcyI6ImNuLm1pc3NmcmVzaC5hcHBsaWNhdGlvbl83LjEuMiIsInByb2ZpbGVfdGltZSI6MTI5LCJpbnRlcnZhbF90aW1lIjoxODI2MTAyLCJ0b2tlbl9pZCI6IjdkNUVcL00rUDIycVA0dlZqSzR6QVJcL0EwckNQVWc3MlNHS2ZjUlBvQVNHdVVYTlhESTR3TTNCM0wydXRodytGK2hwWFFRVkNUT0prck1kMzBwSExPXC93PT0ifQ==&imei=c8b4fc2cc6d7cf62732415b47d6e17b1&access_token=&SM_Device_ID=2017120509563811ea421cde6b0119309424539b447fd001201fe35ffea283&version=7.1.2&screen_width=720&screen_height=1280"
    typeproduct(heros_url, headers,f,data)

    # 酒水
    heros_url = "https://as-vip.missfresh.cn/v3/product/category/hn-drink?platform=android&android_channel_value=meizu&session=android865704033537268&tdk=eyJvcyI6ImFuZHJvaWQiLCJ2ZXJzaW9uIjoiMy4wLjkiLCJwYWNrYWdlcyI6ImNuLm1pc3NmcmVzaC5hcHBsaWNhdGlvbl83LjEuMiIsInByb2ZpbGVfdGltZSI6MTI5LCJpbnRlcnZhbF90aW1lIjoxODI2MTAyLCJ0b2tlbl9pZCI6IjdkNUVcL00rUDIycVA0dlZqSzR6QVJcL0EwckNQVWc3MlNHS2ZjUlBvQVNHdVVYTlhESTR3TTNCM0wydXRodytGK2hwWFFRVkNUT0prck1kMzBwSExPXC93PT0ifQ==&imei=c8b4fc2cc6d7cf62732415b47d6e17b1&access_token=&SM_Device_ID=2017120509563811ea421cde6b0119309424539b447fd001201fe35ffea283&version=7.1.2&screen_width=720&screen_height=1280"
    typeproduct(heros_url, headers, f,data)

    # 熟食
    heros_url = "https://as-vip.missfresh.cn/v3/product/category/sss-hn-fastfood?platform=android&android_channel_value=meizu&session=android865704033537268&tdk=eyJvcyI6ImFuZHJvaWQiLCJ2ZXJzaW9uIjoiMy4wLjkiLCJwYWNrYWdlcyI6ImNuLm1pc3NmcmVzaC5hcHBsaWNhdGlvbl83LjEuMiIsInByb2ZpbGVfdGltZSI6MTI5LCJpbnRlcnZhbF90aW1lIjoxODI2MTAyLCJ0b2tlbl9pZCI6IjdkNUVcL00rUDIycVA0dlZqSzR6QVJcL0EwckNQVWc3MlNHS2ZjUlBvQVNHdVVYTlhESTR3TTNCM0wydXRodytGK2hwWFFRVkNUT0prck1kMzBwSExPXC93PT0ifQ==&imei=c8b4fc2cc6d7cf62732415b47d6e17b1&access_token=&SM_Device_ID=2017120509563811ea421cde6b0119309424539b447fd001201fe35ffea283&version=7.1.2&screen_width=720&screen_height=1280"
    typeproduct(heros_url, headers, f,data)
    # 水果
    heros_url = "https://as-vip.missfresh.cn/v3/product/category/hn-fruit?platform=android&android_channel_value=meizu&session=android865704033537268&tdk=eyJvcyI6ImFuZHJvaWQiLCJ2ZXJzaW9uIjoiMy4wLjkiLCJwYWNrYWdlcyI6ImNuLm1pc3NmcmVzaC5hcHBsaWNhdGlvbl83LjEuMiIsInByb2ZpbGVfdGltZSI6MTI5LCJpbnRlcnZhbF90aW1lIjoxODI2MTAyLCJ0b2tlbl9pZCI6IjdkNUVcL00rUDIycVA0dlZqSzR6QVJcL0EwckNQVWc3MlNHS2ZjUlBvQVNHdVVYTlhESTR3TTNCM0wydXRodytGK2hwWFFRVkNUT0prck1kMzBwSExPXC93PT0ifQ==&imei=c8b4fc2cc6d7cf62732415b47d6e17b1&access_token=&SM_Device_ID=2017120509563811ea421cde6b0119309424539b447fd001201fe35ffea283&version=7.1.2&screen_width=720&screen_height=1280"
    typeproduct(heros_url, headers, f,data)
    #肉
    heros_url = "https://as-vip.missfresh.cn/v3/product/category/hn-food?platform=android&android_channel_value=meizu&session=android865704033537268&tdk=eyJvcyI6ImFuZHJvaWQiLCJ2ZXJzaW9uIjoiMy4wLjkiLCJwYWNrYWdlcyI6ImNuLm1pc3NmcmVzaC5hcHBsaWNhdGlvbl83LjEuMiIsInByb2ZpbGVfdGltZSI6MTI5LCJpbnRlcnZhbF90aW1lIjoxODI2MTAyLCJ0b2tlbl9pZCI6IjdkNUVcL00rUDIycVA0dlZqSzR6QVJcL0EwckNQVWc3MlNHS2ZjUlBvQVNHdVVYTlhESTR3TTNCM0wydXRodytGK2hwWFFRVkNUT0prck1kMzBwSExPXC93PT0ifQ==&imei=c8b4fc2cc6d7cf62732415b47d6e17b1&access_token=&SM_Device_ID=2017120509563811ea421cde6b0119309424539b447fd001201fe35ffea283&version=7.1.2&screen_width=720&screen_height=1280"
    typeproduct(heros_url, headers, f,data)
    for i, p in enumerate(data):
        for j, q in enumerate(p):
            sheet1.write(i, j, q)
        workbook.save('D:\\data.xls')
    '''
