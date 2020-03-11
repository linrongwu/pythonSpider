import urllib,requests
from PIL import Image
from io import BytesIO

def dealwithChapter(id,bookId,sequence,headers):
    url = "https://yymh886.com/query/book/chapter?bookId=%d"%bookId+"&chapterId=%d"%id
    req = requests.get(url=url, headers=headers, verify=False).json()
    if req['content']==None:
        print("none")
    else:
        for each in req['content']['imageList']:
            try:
                num = each['sequence']
                imgUrl = each['url']
                # response = requests.get(imgUrl)
                # image = Image.open(BytesIO(response.content))
                # image.save('F:\hm\%d'%bookId+'\%d'%id+'_'+num+'.jpg','jpg')
                urllib.request.urlretrieve(imgUrl,'F:/%d'%bookId+'_%d'%id+'_'+str(num)+'.jpg')
            except KeyError:
                print('error')
            else:
                print("ok")

def dealwithDirectory(url,headers):
    req = requests.get(url=url, headers=headers, verify=False).json()
    #print(req)
    if req['content']==None:
        print("none")
    else:
        for each in req['content']:
            try:
                id = each['id']
                bookId = each['bookId']
                sequence = each['sequence']
            except KeyError:
                print('error')
            else:
                dealwithChapter(id,bookId,sequence,headers)

if __name__ == '__main__':
    headers = {
    'Accept-Encoding': 'gzip, deflate, br',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36',
    'Host': 'yymh886.com',
    'Connection': 'Keep-Alive',
    'Cookie':'inviteriid=3262785; ciu_key=daa3f4bf-a6e4-4c8d-94b3-5fa4dab9c547$183.17.126.210; ticket=f5f8e3b6-2b58-4a1c-8a1c-0f18d0965347; JSESSIONID=t3ctvpiwz8lf1wdy8217tqgmk'
    }
    url ='https://yymh886.com/query/book/directory?bookId=1173 '
    dealwithDirectory(url, headers)