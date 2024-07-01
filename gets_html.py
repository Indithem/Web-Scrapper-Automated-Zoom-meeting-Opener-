import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, InvalidArgumentException, StaleElementReferenceException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import wait
from selenium.webdriver.support.expected_conditions import element_to_be_clickable,presence_of_element_located
from selenium.webdriver.support.ui import WebDriverWait

# from msedge.selenium_tools import Edge

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
    pass
browser.get(url="https://web.whatsapp.com/")
def propermethod(xpath:str,method:str="exists",msg:str='',wait_time:int=60)->WebElement:
    print("------------------\
        proper method startred "+msg\
        +"----------------------")
    mtd ={"clickable":element_to_be_clickable,
           "exists":presence_of_element_located}[method]
    return WebDriverWait(browser,wait_time,ignored_exceptions=(NoSuchElementException,StaleElementReferenceException))\
        .until(mtd(("xpath",xpath)),msg)

"""got_dada= False
while not got_dada:
    try:
        dada=browser.find_element_by_xpath("//span[@title='Dada']")
        got_dada=True
    except NoSuchElementException:
        time.sleep(1)
        print("waiting to load")"""

CONTACT = "Formula 2022"
propermethod(f"//span[@title='{CONTACT}']",wait_time=120,msg=f"search for {CONTACT}")
print("Found Contact")
# browser.find_element_by_xpath('//*[@id="pane-side"]/div[1]/div/div/div[11]/div/div/div[2]/div[1]/div[1]/span/span').click()
# propermethod('//*[@id="pane-side"]/div[1]/div/div/div[11]/div/div/div[2]/div[1]/div[1]/span/span',method="clickable",msg="click on dada",wait_time=5).click()
propermethod(f"//span[@title='{CONTACT}']",method="clickable",msg="click on dada",wait_time=5).click()
time.sleep(5)
data = bytes(browser.page_source,"utf-8")
while len(data)< 1024*135:
    print("waiting to buffer, have data size", len(data)/1024)
    browser.find_element_by_xpath("//div[substring(@class, string-length(@class) - string-length('copyable-area') + 1)  = 'copyable-area'] / div[@tabindex='0']")
    
    browser.execute_script('document.querySelector("#main > div._1LcQK > div > div._33LGR").scrollBy(0,-500)')
    time.sleep(3)
    data = bytes(browser.page_source,"utf-8")
with open("WhatsApp.html","wb+") as f:
    f.write(data)
    
browser.quit()