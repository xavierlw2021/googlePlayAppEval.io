from PyQt5.QtWidgets import QMainWindow

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, csv

from UI import Ui_MainWindow

class MainWindow_controller(QMainWindow):
    def __init__(self):
        super().__init__() # in python3, super(Class, self).xxx = super().xxx
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_control()

    def setup_control(self):
        self.ui.btn_createCSV.clicked.connect(self.createCSV)    #開始執行

    def openChrome(self):
        option=webdriver.ChromeOptions()
        # option.add_argument("headless") #設定瀏覽器於背景作業
        # option.add_argument("--incognito")  #google play不適用無痕模式，故此行註解之

        ua = "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
        option.add_argument("user-agent={}".format(ua)) #使用偽裝header進入網站

        driver_path= r'E:/chromedriver.exe'  #webdriver檔案
        
        driver = webdriver.Chrome(driver_path, chrome_options=option)
        #設定driver變數為啟動webdriver，chrome_options=option是把瀏覽器於背景作業的參數加入

        return driver

    def create_resultPage(self, driver, result_num):
        uname_num = len(driver.find_elements_by_xpath("//div[@class='bAhLNe kx8XBd']/span"))
        time.sleep(5)
        check_num = 0
        move = driver.find_element_by_tag_name('body')
        time.sleep(1)
        try:
            move.find_element_by_xpath("//div[@class='RWsdse']//span[contains(text(),'最新')]").click()
        except:
            pass
        time.sleep(1)

        while result_num > uname_num: 
            print(f'擴展評論頁面({uname_num})') 
            move.send_keys(Keys.END)
            time.sleep(3)
            try:
                move.find_element_by_xpath("//span[contains(text(),'顯示更多內容')]").click()
            except:
                pass
            uname_num = len(driver.find_elements_by_xpath("//div[@class='bAhLNe kx8XBd']/span"))
            time.sleep(1)
            if uname_num == check_num:
                break
            elif uname_num < check_num:
                print(f'評論頁面擴展至{check_num}時，偵測到網頁重置')
                result_num = check_num
                check_num = 0
                continue
            check_num = uname_num

    def createCSV(self):
        url = self.ui.url_input.toPlainText()
        if '&gl=US&showAllReviews=true' not in url:
            url = url + '&gl=US&showAllReviews=true'

        try:
            result_num = int(self.ui.result_number.text())
        except:
            print('未輸入or輸入錯誤, 預設為100')
            result_num = 100

        driver = self.openChrome()
        try:
            driver.maximize_window()
            driver.get(url)
            time.sleep(5)
        except:
            self.ui.label_infomation.setText('網址錯誤，連結失敗')

        self.create_resultPage(driver, result_num)

        uname_path = "//div[@class='bAhLNe kx8XBd']/span"
        rank_path = "//div[@class='bAhLNe kx8XBd']//div[@class='pf5lIe']/div"
        date_path = "//div[@class='bAhLNe kx8XBd']//span[@class='p2TkOb']"
        evaluation_path = "//div[@class='d15Mdf bAhLNe']/div[@class='UD7Dzf']/span[@jsname='bN97Pc']"

        un_ele = driver.find_elements_by_xpath(uname_path)  #使用者名稱
        time.sleep(2)
        rk_ele = driver.find_elements_by_xpath(rank_path)  #星級
        time.sleep(2)
        pd_ele = driver.find_elements_by_xpath(date_path)   #發文日期
        time.sleep(2)
        eval_ele = driver.find_elements_by_xpath(evaluation_path)   #評價內文
        time.sleep(2)
        
        print('資料寫入中...')

        path = "app_eval.csv"
        with open(path, 'w', newline='', encoding='utf-8') as f:    
            wr = csv.writer(f)    
            wr.writerow(['ID', '評價', '日期', '評論'])
            for uname, rank, postDate, evalText in zip(un_ele, rk_ele, pd_ele, eval_ele):
                wr.writerow([uname.text, rank.get_attribute('aria-label')[4], postDate.text, evalText.text])    
            self.ui.label_infomation.setText('CSV建立完成!')

        driver.quit()