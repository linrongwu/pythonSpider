import urllib,requests
from PIL import Image
from io import BytesIO
import json

def dealwithChapter(chapter,bookId,sequence,headers):
    url = "https://www.diyihm.com/view/%d"%bookId+"/%d"%chapter
    req = requests.get(url=url, headers=headers, verify=False).text
    begin = req.find('volume')
    end = req.find('pay')
    data = req[begin:end].strip()
    json_ = data[8:len(data)-2]
    json_data = json.loads(json_)
    if json_data['pages']==None:
        print("none")
    else:
        num=1
        for each in json_data['pages']:
            try:   
                imgUrl = each
                urllib.request.urlretrieve(each,'F:/%d'%bookId+'_%d'%chapter+'_'+str(num)+'.jpg')
                num = num +1
            except KeyError:
                print('error')
            else:
                print("ok")

def dealwithDirectory(url,headers):
    req = requests.get(url=url, headers=headers, verify=False).text
    begin = req.find('initIntroData')
    end = req.find('UserCookie')
    data = req[begin+15:end].strip()
    json_ = data[0:len(data)-3]
    json_data = json.loads(json_)
    if json_data['data']==None:
        print("none")
    else:
        for each in json_data['data']:
            try:
                chapter = each['id']
                bookId = each['comic_id']
                sequence = each['chapter_order']
            except KeyError:
                print('error')
            else:
                dealwithChapter(chapter,bookId,sequence,headers)

if __name__ == '__main__':
    headers = {
    'Accept-Encoding': 'gzip, deflate, br',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
    'Host': 'www.diyihm.com',
    'Connection': 'Keep-Alive',
    'Cookie':'ascc_1057=1; __51cke__=; history_cookie_ppm=null; CFWztgFirstShowTime_856_Cookie=2020-3-11%2021%3A4%3A28; Hm_lvt_52ec474a2124c332da93cd0293a3980b=1583931869; UBGLAI63GV=ksipf.1583932796; __tins__20541705=%7B%22sid%22%3A%201583931724913%2C%20%22vd%22%3A%2020%2C%20%22expires%22%3A%201583934947468%7D; __51laig__=20; CFWztgVisitTotal_856_Cookie=13; Hm_lpvt_52ec474a2124c332da93cd0293a3980b=1583933148; __ty_cpvx_b_3460_cpv_plan_ids=%7C164%7C%7C135%7C; __ty_cpvx_b_3460_cpv_plan_uids=%7C3582%7C%7C64%7C'
    }
    url ='https://www.diyihm.com/comic/31'
    dealwithDirectory(url, headers)