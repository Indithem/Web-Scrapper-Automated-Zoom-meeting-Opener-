import time, logging
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, InvalidArgumentException
# from msedge.selenium_tools import Edge
logging.basicConfig(filename="log.log",format="[%(asctime)s] %(filename)s %(levelname)s %(message)s",level=logging.INFO)

# try:
#     browser = Edge(executable_path='../msedgedriver.exe')


# except InvalidArgumentException:
#     logging.warning("EDGE!")
options = webdriver.ChromeOptions()
options.add_argument(r"user-data-dir=C:\Users\[USER]\Desktop\python\selenium\class\Udatar")
#options.add_argument("--headless")
#options.add_argument("--window=size=%s"%"0,0")
try:
    browser = webdriver.Chrome(executable_path="../chromedriver.exe",options=options)
except InvalidArgumentException:
    logging.info("Chrome")

browser.get(url="https://web.whatsapp.com/")
logging.info("opened whatsapp")
got_dada= False
while not got_dada:
    try:
        dada=browser.find_element_by_xpath("//span[@title='Dada']")
        got_dada=True
    except NoSuchElementException:
        time.sleep(1)
        print("waiting to load")
logging.info("Found Contact")
browser.find_element_by_xpath('//*[@id="pane-side"]/div[1]/div/div/div[11]/div/div/div[2]/div[1]/div[1]/span/span').click()
time.sleep(5)
data = bytes(browser.page_source,"utf-8")
while len(data)< 1024*100:
    print("waiting to buffer")
    time.sleep(3)
    data = bytes(browser.page_source,"utf-8")
with open("WhatsApp.html","wb+") as f:
    f.write(data)
    
browser.quit()
logging.info("Bye Bye")