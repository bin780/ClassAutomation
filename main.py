import pandas as pd
import numpy as np
from timeloop import Timeloop
from datetime import timedelta

from datetime import datetime

from selenium import webdriver

from selenium.webdriver.common.keys import Keys

tl = Timeloop()



def fun1():
    #global driver


    global df
    df=pd.read_excel('TimeTable//urls.xlsx')
    print(df)

@tl.job(interval=timedelta(seconds=10))
def fun():
    now=datetime.now()
    t=0
    index=0
    for i in df['time']:
        if i>=now.hour:
            t=i
            index=df[df['time']==t].index[0]
            break

    try:


        #df.columns=['time','0','1','2','3','4','5']
        print(now.weekday())
        print(now.hour)
        #print(pd.isnull(df[now.weekday()][0]))


        if pd.isnull(df[now.weekday()][index])==False:
            print(now.weekday())
            # browser = webdriver.Chrome(executable_path="WebDriver//chromedriver.exe")
            browser = webdriver.Firefox(executable_path="WebDriver//geckodriver")
            browser.get(df[now.weekday()][index])
            frame=browser.find_element_by_id('pbui_iframe')
            browser. switch_to.frame(frame)
            uname=browser.find_element_by_css_selector('.style-name-input-19PlX > input:nth-child(1)')
            email=browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[3]/input')
            btn=browser.find_element_by_xpath('//*[@id="guest_next-btn"]')

            uname.send_keys("jisjo")     ### write name here
            email.send_keys("xgxjg@x.com")   ### write email here
            btn.click()

            # browser.close()
        else:
            print(df['time'][0],pd.isnull(df[now.weekday()][0]))

    except Exception as e:
        print("here")
        print(e)



if __name__ == '__main__':
    fun1()
    tl.start(block=True)