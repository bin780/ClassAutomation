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

@tl.job(interval=timedelta(seconds=1))
def fun():

    try:
        now = datetime.now()

        df.columns=['time','0','1','2','3','4','5']
        print(now.weekday())
        print(df[str(now.weekday())])

        # if df['time'][0]==now.hour and np.isnan(df[now.weekday()][0])==False:
        #     print(now.weekday())
        #     browser = webdriver.Firefox(executable_path="WebDriver//geckodriver")
        #     frame=browser.find_element_by_id('pbui_iframe')
        #     browser. switch_to.frame(frame)
        #     uname=browser.find_element_by_css_selector('.style-name-input-19PlX > input:nth-child(1)')
        #     email=browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[3]/input')
        #     btn=browser.find_element_by_xpath('//*[@id="guest_next-btn"]')
        #
        #     uname.send_keys("jisjo")     ### write name here
        #     email.send_keys("xgxjg@x.com")   ### write email here
        #     btn.click()
        #     df.drop(0,axis=1,inplace=True)
        #     # browser.close()
        # else:
        #     print(df['time'][0],np.isnan(df[now.weekday()][0]))

    except Exception as e:
        print("here")
        print(e)



if __name__ == '__main__':
    fun1()
    tl.start(block=True)