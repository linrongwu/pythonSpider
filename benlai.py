#-*- coding: UTF-8 -*-
import requests
import  xlwt


def product(sysNo,headers,data):
    payload = {'productSysNo':sysNo}
    product_url = 'https://www.benlai.com/IProduct/ProductDetailNew?systemVersion=7.0&phoneModel=M6&localcity=244&source=3&nativeVersion=3.4.0&t=1513223139828&sign=C4C2BB0A57A53EAD7010F9D03FD2F15D&version=3.4.0&android_id=ac93d26754c2e2d1&channel=meizu&deviceId=865704033537268'
    product_req = requests.post(url=product_url, headers=headers, verify=False,data=payload).json()
    Data = product_req['data']
    productName = Data['productName']
    try:
        productArea = Data['productArea']
        productArea_name=productArea['area']
    except TypeError:
        productArea_name='null'

    productPrice = Data['productPrice']
    if str(productPrice['hasOrigPrice'])=='True':
        origPrice = productPrice['origPrice']
        price = productPrice['price']
    else:
        origPrice = productPrice['price']
        price = '0'

    commdata = {'productSysNo': sysNo,'pageid':'com.android.benlai.fragment.prddetail.CommentFragment','pageIndex':1,'reviewType':1,'pageSize':20,'isAll':0}
    product_commentList = 'https://www.benlai.com/IProduct/ProductCommentList?systemVersion=7.0&phoneModel=M6&localcity=244&source=3&nativeVersion=3.4.0&t=1513223686266&sign=AE6173BC31F904FA18152E0D67DE3EAE&version=3.4.0&android_id=ac93d26754c2e2d1&channel=meizu&deviceId=865704033537268'
    product_commentList_req=requests.post(url=product_commentList,headers=headers,verify=False,data=commdata).json()
    Comm_data = product_commentList_req['data']
    totalCommentImageNum = str(Comm_data['totalCommentImageNum'])
    totalCommentNum = str(Comm_data['totalCommentNum'])
    t = [productName, productArea_name, origPrice, price, totalCommentImageNum, totalCommentNum]

    product_commentLabel = 'https://www.benlai.com/IProduct/ProductCommentLabelList?systemVersion=7.0&phoneModel=M6&localcity=244&source=3&nativeVersion=3.4.0&t=1513223686294&sign=140C3D168D9A552733070CDD9564B9A4&version=3.4.0&android_id=ac93d26754c2e2d1&channel=meizu&deviceId=865704033537268'
    product_commentLabel_req=requests.post(url=product_commentLabel,headers=headers,verify=False,data=payload).json()

    if product_commentLabel_req['data']==None:
        data.append(t)
    else:
        for each in product_commentLabel_req['data']:
            labelName = each['labelName']
            labelCount = str(each['labelCount'])
            t.append(labelName)
            t.append(labelCount)
        data.append(t)



def typeproduct(heros_url,headers,data):
    req = requests.get(url=heros_url, headers=headers, verify=False).json()
    if req['data']==None:
        print("??")
    else:
        for each in req['data']:
            try:
                sysNo = each['sysNo']
            except KeyError:
                print('en')
            else:
                product(sysNo,headers,data)


if __name__ == '__main__':
    workbook = xlwt.Workbook()
    sheet1 = workbook.add_sheet('data1', cell_overwrite_ok=True)
    data=[]

    headers = {
    'Accept-Encoding': 'gzip',
    'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 7.0; M6 Build/NRD90M)',\
    'Host': 'www.benlai.com',
    'Connection': 'Keep-Alive'}
    # for each in req['products']:
    #     try:
    #         name = each['name']
    #         sku = each['sku']
    #     except KeyError:
    #         print('en')
    #     else:
    #         product(sku,headers,f,data)


    #列1
    heros_url = "https://www.benlai.com/ISearch?channel=meizu&sign=93D81018C6658C635524145DFFD23241&source=3&pageid=com.android.benlai.activity.ProductListActivity&systemVersion=7.0&deviceId=865704033537268&phoneModel=M6&limit=20&offset=0&localcity=244&sort=0&version=3.4.0&nativeVersion=3.4.0&c1=3264&t=1513239601333&filterType=0&android_id=ac93d26754c2e2d1"
    typeproduct(heros_url, headers,data)

    #2
    heros_url = "https://www.benlai.com/ISearch?channel=meizu&sign=3AC7F375055B2A8202199D10681FFD57&source=3&pageid=com.android.benlai.activity.ProductListActivity&systemVersion=7.0&deviceId=865704033537268&phoneModel=M6&limit=20&offset=20&localcity=244&sort=0&version=3.4.0&nativeVersion=3.4.0&c1=3264&t=1513239606789&filterType=0&android_id=ac93d26754c2e2d1"
    typeproduct(heros_url, headers,data)

    #3
    heros_url = "https://www.benlai.com/ISearch?channel=meizu&sign=3F48B56614D35B68774931887EEEBCE3&source=3&pageid=com.android.benlai.activity.ProductListActivity&systemVersion=7.0&deviceId=865704033537268&phoneModel=M6&limit=20&offset=40&localcity=244&sort=0&version=3.4.0&nativeVersion=3.4.0&c1=3264&t=1513239610296&filterType=0&android_id=ac93d26754c2e2d1"
    typeproduct(heros_url, headers,data)

    #4
    heros_url = "https://www.benlai.com/ISearch?channel=meizu&sign=7A21CA46B4C987F4C230C350C4B31970&source=3&pageid=com.android.benlai.activity.ProductListActivity&systemVersion=7.0&deviceId=865704033537268&phoneModel=M6&limit=20&offset=60&localcity=244&sort=0&version=3.4.0&nativeVersion=3.4.0&c1=3264&t=1513239613774&filterType=0&android_id=ac93d26754c2e2d1"
    typeproduct(heros_url, headers,data)

    #5
    heros_url = "https://www.benlai.com/ISearch?channel=meizu&sign=AFA73E402506B1799FD5684E89D6DEDE&source=3&pageid=com.android.benlai.activity.ProductListActivity&systemVersion=7.0&deviceId=865704033537268&phoneModel=M6&limit=20&offset=80&localcity=244&sort=0&version=3.4.0&nativeVersion=3.4.0&c1=3264&t=1513239617201&filterType=0&android_id=ac93d26754c2e2d1"
    typeproduct(heros_url, headers,data)

    #6
    heros_url = "https://www.benlai.com/ISearch?channel=meizu&sign=1B22BFAA05B0C3E4964B13D3D72F5F5A&source=3&pageid=com.android.benlai.activity.ProductListActivity&systemVersion=7.0&deviceId=865704033537268&phoneModel=M6&limit=20&offset=100&localcity=244&sort=0&version=3.4.0&nativeVersion=3.4.0&c1=3264&t=1513239620166&filterType=0&android_id=ac93d26754c2e2d1"
    typeproduct(heros_url, headers,data)

    #7
    heros_url = "https://www.benlai.com/ISearch?channel=meizu&sign=2F3B3E180EF0FED9DE0F000BE49CC49A&source=3&pageid=com.android.benlai.activity.ProductListActivity&systemVersion=7.0&deviceId=865704033537268&phoneModel=M6&limit=20&offset=120&localcity=244&sort=0&version=3.4.0&nativeVersion=3.4.0&c1=3264&t=1513239623314&filterType=0&android_id=ac93d26754c2e2d1"
    typeproduct(heros_url, headers,data)

    #8
    heros_url = "https://www.benlai.com/ISearch?channel=meizu&sign=F0C3A71282014C6EE914D1549761ABC5&source=3&pageid=com.android.benlai.activity.ProductListActivity&systemVersion=7.0&deviceId=865704033537268&phoneModel=M6&limit=20&offset=140&localcity=244&sort=0&version=3.4.0&nativeVersion=3.4.0&c1=3264&t=1513239626156&filterType=0&android_id=ac93d26754c2e2d1"
    typeproduct(heros_url, headers,data)

    #9
    heros_url = "https://www.benlai.com/ISearch?channel=meizu&sign=4766BD88F8926914E96BBB9835A88754&source=3&pageid=com.android.benlai.activity.ProductListActivity&systemVersion=7.0&deviceId=865704033537268&phoneModel=M6&limit=20&offset=160&localcity=244&sort=0&version=3.4.0&nativeVersion=3.4.0&c1=3264&t=1513239629306&filterType=0&android_id=ac93d26754c2e2d1"
    typeproduct(heros_url, headers,data)

    #10
    heros_url = "https://www.benlai.com/ISearch?channel=meizu&sign=191EE9C33F37D34DCE6AED20234C6B41&source=3&pageid=com.android.benlai.activity.ProductListActivity&systemVersion=7.0&deviceId=865704033537268&phoneModel=M6&limit=20&offset=180&localcity=244&sort=0&version=3.4.0&nativeVersion=3.4.0&c1=3264&t=1513239632163&filterType=0&android_id=ac93d26754c2e2d1"
    typeproduct(heros_url, headers,data)

    #11
    heros_url = "https://www.benlai.com/ISearch?channel=meizu&sign=34C9D619DE9C8A39590DEC6124D5B28A&source=3&pageid=com.android.benlai.activity.ProductListActivity&systemVersion=7.0&deviceId=865704033537268&phoneModel=M6&limit=20&offset=200&localcity=244&sort=0&version=3.4.0&nativeVersion=3.4.0&c1=3264&t=1513239635943&filterType=0&android_id=ac93d26754c2e2d1"
    typeproduct(heros_url, headers,data)
    # 12
    heros_url = "https://www.benlai.com/ISearch?channel=meizu&sign=27D8D4DDB0E8C13FE03E2DA96D20F6F0&source=3&pageid=com.android.benlai.activity.ProductListActivity&systemVersion=7.0&deviceId=865704033537268&phoneModel=M6&limit=20&offset=220&localcity=244&sort=0&version=3.4.0&nativeVersion=3.4.0&c1=3264&t=1513239639446&filterType=0&android_id=ac93d26754c2e2d1:"
    typeproduct(heros_url, headers, data)
    #13
    heros_url = "https://www.benlai.com/ISearch?channel=meizu&sign=9894F597C34CBC90FD023C24AE066D56&source=3&pageid=com.android.benlai.activity.ProductListActivity&systemVersion=7.0&deviceId=865704033537268&phoneModel=M6&limit=20&offset=240&localcity=244&sort=0&version=3.4.0&nativeVersion=3.4.0&c1=3264&t=1513239642992&filterType=0&android_id=ac93d26754c2e2d1"
    typeproduct(heros_url, headers, data)

    #14
    heros_url = "https://www.benlai.com/ISearch?channel=meizu&sign=F376BF73CA594363B808894417DED307&source=3&pageid=com.android.benlai.activity.ProductListActivity&systemVersion=7.0&deviceId=865704033537268&phoneModel=M6&limit=20&offset=260&localcity=244&sort=0&version=3.4.0&nativeVersion=3.4.0&c1=3264&t=1513239646660&filterType=0&android_id=ac93d26754c2e2d1"
    typeproduct(heros_url, headers, data)


    #15
    heros_url = "https://www.benlai.com/ISearch?channel=meizu&sign=93E6252F5D92E75BDFCACA789F51BB85&source=3&pageid=com.android.benlai.activity.ProductListActivity&systemVersion=7.0&deviceId=865704033537268&phoneModel=M6&limit=20&offset=280&localcity=244&sort=0&version=3.4.0&nativeVersion=3.4.0&c1=3264&t=1513239649623&filterType=0&android_id=ac93d26754c2e2d1"
    typeproduct(heros_url, headers,data)

    #16
    heros_url = "https://www.benlai.com/ISearch?channel=meizu&sign=0002AAC3DCE750255167C928FB018641&source=3&pageid=com.android.benlai.activity.ProductListActivity&systemVersion=7.0&deviceId=865704033537268&phoneModel=M6&limit=20&offset=300&localcity=244&sort=0&version=3.4.0&nativeVersion=3.4.0&c1=3264&t=1513239652202&filterType=0&android_id=ac93d26754c2e2d1"
    typeproduct(heros_url, headers,data)

    #17
    heros_url = "https://www.benlai.com/ISearch?channel=meizu&sign=A89263FB8B84E202C535501BE328580E&source=3&pageid=com.android.benlai.activity.ProductListActivity&systemVersion=7.0&deviceId=865704033537268&phoneModel=M6&limit=20&offset=320&localcity=244&sort=0&version=3.4.0&nativeVersion=3.4.0&c1=3264&t=1513239655278&filterType=0&android_id=ac93d26754c2e2d1"
    typeproduct(heros_url, headers,data)

    # 18

    heros_url = "https://www.benlai.com/ISearch?channel=meizu&sign=AF2969C89206DD5074C43FF36CF0D974&source=3&pageid=com.android.benlai.activity.ProductListActivity&systemVersion=7.0&deviceId=865704033537268&phoneModel=M6&limit=20&offset=340&localcity=244&sort=0&version=3.4.0&nativeVersion=3.4.0&c1=3264&t=1513239659094&filterType=0&android_id=ac93d26754c2e2d1"
    typeproduct(heros_url, headers, data)

    # 19
    heros_url = "https://www.benlai.com/ISearch?channel=meizu&sign=03B335B688DC8A1A85C67D1BC45D8FF1&source=3&pageid=com.android.benlai.activity.ProductListActivity&systemVersion=7.0&deviceId=865704033537268&phoneModel=M6&limit=20&offset=360&localcity=244&sort=0&version=3.4.0&nativeVersion=3.4.0&c1=3264&t=1513239662538&filterType=0&android_id=ac93d26754c2e2d1"
    typeproduct(heros_url, headers, data)


    #20
    heros_url = "https://www.benlai.com/ISearch?channel=meizu&sign=D15C12037EE83ACE21F966E7395DA442&source=3&pageid=com.android.benlai.activity.ProductListActivity&systemVersion=7.0&deviceId=865704033537268&phoneModel=M6&limit=20&offset=380&localcity=244&sort=0&version=3.4.0&nativeVersion=3.4.0&c1=3264&t=1513239666612&filterType=0&android_id=ac93d26754c2e2d1"
    typeproduct(heros_url, headers,data)

    #21
    heros_url = "https://www.benlai.com/ISearch?channel=meizu&sign=A177D9FB9A468A8544AE07C88B06D749&source=3&pageid=com.android.benlai.activity.ProductListActivity&systemVersion=7.0&deviceId=865704033537268&phoneModel=M6&limit=20&offset=399&localcity=244&sort=0&version=3.4.0&nativeVersion=3.4.0&c1=3264&t=1513239669167&filterType=0&android_id=ac93d26754c2e2d1"
    typeproduct(heros_url, headers,data)
    '''
    # 22
    heros_url = "https://www.benlai.com/ISearch?channel=meizu&sign=4E93C6EA01B3C83C4515AF2F68671A04&source=3&pageid=com.android.benlai.activity.ProductListActivity&systemVersion=7.0&deviceId=865704033537268&phoneModel=M6&limit=20&offset=420&localcity=244&sort=0&version=3.4.0&nativeVersion=3.4.0&c1=3136&t=1513238135899&filterType=0&android_id=ac93d26754c2e2d1"
    typeproduct(heros_url, headers, data)

    # 23
    heros_url = "https://www.benlai.com/ISearch?channel=meizu&sign=DC8AC2B5D19D4F7E5F089DF9F16840F1&source=3&pageid=com.android.benlai.activity.ProductListActivity&systemVersion=7.0&deviceId=865704033537268&phoneModel=M6&limit=20&offset=440&localcity=244&sort=0&version=3.4.0&nativeVersion=3.4.0&c1=3136&t=1513238139487&filterType=0&android_id=ac93d26754c2e2d1"
    typeproduct(heros_url, headers, data)


    #24
    heros_url = "https://www.benlai.com/ISearch?channel=meizu&sign=94EF3F9795690496F254D950EFA8A432&source=3&pageid=com.android.benlai.activity.ProductListActivity&systemVersion=7.0&deviceId=865704033537268&phoneModel=M6&limit=20&offset=460&localcity=244&sort=0&version=3.4.0&nativeVersion=3.4.0&c1=3136&t=1513238142548&filterType=0&android_id=ac93d26754c2e2d1"
    typeproduct(heros_url, headers,data)

    #25
    heros_url = "https://www.benlai.com/ISearch?channel=meizu&sign=6796064C7CF90D7BDA6F29F6B6F63035&source=3&pageid=com.android.benlai.activity.ProductListActivity&systemVersion=7.0&deviceId=865704033537268&phoneModel=M6&limit=20&offset=480&localcity=244&sort=0&version=3.4.0&nativeVersion=3.4.0&c1=3136&t=1513238145768&filterType=0&android_id=ac93d26754c2e2d1"
    typeproduct(heros_url, headers,data)

    # 26
    heros_url = "https://www.benlai.com/ISearch?channel=meizu&sign=F378CAB6237F4CD141F7C5A46DBFB960&source=3&pageid=com.android.benlai.activity.ProductListActivity&systemVersion=7.0&deviceId=865704033537268&phoneModel=M6&limit=20&offset=500&localcity=244&sort=0&version=3.4.0&nativeVersion=3.4.0&c1=3136&t=1513238148347&filterType=0&android_id=ac93d26754c2e2d1"
    typeproduct(heros_url, headers, data)

    # 27
    heros_url = "https://www.benlai.com/ISearch?channel=meizu&sign=E7B70BFB521DB4BE76C3357C2E23E997&source=3&pageid=com.android.benlai.activity.ProductListActivity&systemVersion=7.0&deviceId=865704033537268&phoneModel=M6&limit=20&offset=520&localcity=244&sort=0&version=3.4.0&nativeVersion=3.4.0&c1=3136&t=1513238150778&filterType=0&android_id=ac93d26754c2e2d1"
    typeproduct(heros_url, headers, data)

    # 28
    heros_url = "https://www.benlai.com/ISearch?channel=meizu&sign=EB9B3857E77D829FBB052477C4641BB8&source=3&pageid=com.android.benlai.activity.ProductListActivity&systemVersion=7.0&deviceId=865704033537268&phoneModel=M6&limit=20&offset=540&localcity=244&sort=0&version=3.4.0&nativeVersion=3.4.0&c1=3136&t=1513238153200&filterType=0&android_id=ac93d26754c2e2d1"
    typeproduct(heros_url, headers, data)


    #29
    heros_url = "https://www.benlai.com/ISearch?channel=meizu&sign=3D2EFF379097B51405435E4FF158B24D&source=3&pageid=com.android.benlai.activity.ProductListActivity&systemVersion=7.0&deviceId=865704033537268&phoneModel=M6&limit=20&offset=560&localcity=244&sort=0&version=3.4.0&nativeVersion=3.4.0&c1=3136&t=1513238156180&filterType=0&android_id=ac93d26754c2e2d1"
    typeproduct(heros_url, headers,data)

    #30
    heros_url = "https://www.benlai.com/ISearch?channel=meizu&sign=8663EE1BD39474AA1E92401299ABBE11&source=3&pageid=com.android.benlai.activity.ProductListActivity&systemVersion=7.0&deviceId=865704033537268&phoneModel=M6&limit=20&offset=580&localcity=244&sort=0&version=3.4.0&nativeVersion=3.4.0&c1=3136&t=1513238157830&filterType=0&android_id=ac93d26754c2e2d1"
    typeproduct(heros_url, headers,data)

    # 31
    heros_url = "https://www.benlai.com/ISearch?channel=meizu&sign=4AC6E272137E8D240DA4EEDDCD2AB42A&source=3&pageid=com.android.benlai.activity.ProductListActivity&systemVersion=7.0&deviceId=865704033537268&phoneModel=M6&limit=20&offset=595&localcity=244&sort=0&version=3.4.0&nativeVersion=3.4.0&c1=3136&t=1513238159258&filterType=0&android_id=ac93d26754c2e2d1"
    typeproduct(heros_url, headers, data)
    '''


    for i, p in enumerate(data):
        for j, q in enumerate(p):
            sheet1.write(i, j, q)
        workbook.save('E:\\data9.xls')
