#coding:utf-8
import unittest
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import  xlwt
class seleniumTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.PhantomJS()
        self.data=[]

    def testEle(self): 
        driver = self.driver
        driver.get('https://s.2.taobao.com/list/list.htm?spm=2007.1000261.1867087.5.135334f1MmVrJR&catid=50100398&st_trust=1&ist=1')
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(10)
        page=1
        soup = BeautifulSoup(driver.page_source, 'lxml')
        datalist = soup.select('.ks-waterfall')
        print(len(datalist))
        for each in datalist:
            if (len(each.select('.item-seller'))==0):
                print('不要')
            else:
                seller = (((each.select('.item-seller'))[0].select('.seller-nick'))[0].select('a'))[0].text
                iteminfo = (each.select('.item-info'))[0]

                itempic = ((iteminfo.select('.item-pic'))[0].select('a'))[0]
                href = itempic.attrs['href']
                title = itempic.attrs['title']
                browser = webdriver.PhantomJS()
                browser.get(href)
                html = BeautifulSoup(browser.page_source, 'lxml')

                price=((iteminfo.select('.item-attributes'))[0].select('.price'))[0].select('em')[0].text
                location=((iteminfo.select('.item-attributes'))[0].select('.item-location'))[0].text

                dec = each.select('.item-brief-desc')[0].text


                self.data.append(t)
        while page<100:
            page = page + 1
            #driver.find_element_by_xpath("//a[contains(text(),'下一页')]").click()  # selenium的xpath用法，找到包含“下一页”的a标签去点击
            driver.find_element_by_xpath("// *[ @ id = 'J_Pages'] / a[7]").click()
            time.sleep(5)  # 睡2秒让网页加载完再去读它的html代码
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            time.sleep(5)
            soup = BeautifulSoup(driver.page_source, "lxml")
            product = soup.select('.gl-item')
            print(len(product))
            for each in product:
                if (len(each.select('.p-tag3')) == 0) & (len(each.select('.p-tag')) == 0):
                    print('不要')
                else:

                    name = ((each.select('.p-name'))[0].select('em'))[0].text
                    price = ((each.select(".p-price"))[0].select("i"))[0].text
                    t = [name, price]
                    print(t)
                    self.data.append(t)
            print(page)

    def tearDown(self):
        workbook = xlwt.Workbook()
        sheet1 = workbook.add_sheet('test', cell_overwrite_ok=True)
        for i, p in enumerate(self.data):
            for j, q in enumerate(p):
                sheet1.write(i, j, q)
            workbook.save('E:\\data.xls')
        print('down')

if __name__ == "__main__":
    unittest.main()

