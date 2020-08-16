import pandas as pd
import numpy as np
from timeloop import Timeloop
from datetime import timedelta

from datetime import datetime

from selenium import webdriver
import time

from selenium.webdriver.firefox.options import Options
from pynput.keyboard import  Key,Controller


from selenium.webdriver.common.keys import Keys



from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

tl = Timeloop()



def fun1():
    #global driver


    global df
    global key
    key = Controller()
    df=pd.read_excel('TimeTable//urls.xlsx')
    df['finished']=np.zeros(df.shape[0],dtype=np.int32)
    print("time table")
    print(df)

@tl.job(interval=timedelta(seconds=35))
def fun():
    now=datetime.now()
    t=0
    index=0
    for i in df['time']:
        if i==now.hour:
            t=i
            index=df[df['time']==t].index[0]
            break

    try:


        #df.columns=['time','0','1','2','3','4','5']
        # print(now.weekday())
        # print(now.hour)
        #print(pd.isnull(df[now.weekday()][0]))



        if pd.isnull(df[now.weekday()][index])==False and df['finished'][index]==0:
            f=1
            print(now.weekday())
            #browser = webdriver.Chrome(executable_path="WebDriver//chromedriver.exe")
            browser = webdriver.Firefox(executable_path="WebDriver//geckodriver.exe")
            options=Options()
            options.add_argument("use-fake-ui-for-media-stream")


            #fp=webdriver.FirefoxProfile()
            #fp.set_preference("browser.download.manager.showWhenStarting",False)
            browser.get(df[now.weekday()][index])
            browser.implicitly_wait(20)



            ele=browser.find_element_by_id('push_download_join_by_browser')
            ele.click()
            browser.implicitly_wait(30)
            frame=browser.find_element_by_id("pbui_iframe")
            browser. switch_to.frame(frame)
            browser.implicitly_wait(30)
            uname=browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/input')
            email=browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[3]/input')
            btn=browser.find_element_by_xpath('//*[@id="guest_next-btn"]')

            uname.send_keys("jisjo")                          ### write name here
            email.send_keys("xgxjg@x.com")             ### write email here
            btn.click()

            browser.implicitly_wait(10)
            key.press(Key.enter)
            key.release(Key.enter)
            df.at[index,'finished']=1
            #print(df)
            #browser.implicitly_wait(10)

            browser.implicitly_wait(10)




            # frame1 = browser.find_element_by_id("pbui_iframe")
            # browser.switch_to.frame(frame1)











            btn2=browser.find_element_by_id('interstitial_join_btn')
            btn2.click()



        else:
            print("time is now {}".format(now.time()))

    except Exception as e:

        print("here")
        print(e)




if __name__ == '__main__':
    try:
        fun1()
        tl.start(block=True)
    except Exception as e:
        print(e)