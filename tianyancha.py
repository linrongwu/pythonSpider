# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 09:48:28 2019

@author: String
"""
#coding=utf-8
import MySQLdb
from selenium import webdriver
from selenium.webdriver import ActionChains

class Boss:
    def __init__(self,url):
        self.driver = webdriver.Chrome()
        self.driver.get(url) #首页
        self.company_name=[]
        self.i = 1
        
    def getdata(self):
        end = self.driver.find_element_by_class_name('-end').text
        page =end[3:]
        while self.i< int(page):
            companyDiv = self.driver.find_elements_by_class_name("left-col")
            for company in companyDiv: 
                self.company_name.append(company.text)
            self.i=self.i+1
            self.driver.get("https://www.tianyancha.com/elibs_quoted/p"+str(self.i))
        return self.company_name
        
    def getbreakFlag(self):
        return self.breakflag

class Mysql:
    
    def __init__(self,host,port,uesr,passwd,db):
        self.conn = MySQLdb.connect(
                host = host,
                port = port,
                user = uesr,
                passwd = passwd,
                db = db,
                )
    
    def execute(self,sql):
        cur = self.conn.cursor()
        cur.execute(sql)
        cur.close()
        self.conn.commit()
        
        
    def close(self):
        self.conn.close()
        
    
if __name__ == '__main__':
    url = "https://www.tianyancha.com/elibs_quoted"
    boss = Boss(url)
    company_name = []
    company_name = boss.getdata()
    print("break")
    print(company_name)
    