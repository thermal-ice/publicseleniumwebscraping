from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time


class webscraping_class():
    """
    __init__ contains the initialization of the Selenium Webdriver.

    All the 'scrape' methods are the methods for scraping the individual website in question.

    Close_selenium method closes the driver. I don't know whether to use quit or
    close, and so I used both ¯\_(ツ)_/¯
    """

    def __init__(self):
        self.chrome_options = Options()
        self.chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome("/Users/carloshuang/PycharmProjects/seleniumwebscraping/chromedriver",
                                       options = self.chrome_options)

    def wsj_scrape(self) -> "list":
        self.driver.get("http://projects.wsj.com/buzzwords2014/")

        wsj_bs = [self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[2]/div/p').text[1:-1]]

        for i in range(4):
            time.sleep(0.5)
            self.driver.find_element_by_id("random_phrase").click()
            the_bs = self.driver.find_element_by_xpath('//*[@id="response"]').text[1:-1]
            wsj_bs.append(the_bs)

        return wsj_bs

    def atrixnet_scrape(self) -> "list":
        self.driver.get("https://www.atrixnet.com/bs-generator.html")

        atrix_bs = []

        for i in range(5):
            time.sleep(0.05)
            self.driver.find_element_by_xpath("/html/body/div/table/tbody/tr/td/form/p[1]/input").click()
            the_bs = self.driver.find_element_by_id("bullshit").get_attribute("value")
            atrix_bs.append(the_bs)

        return atrix_bs

    def ruderal_scrape(self) -> "list":
        self.driver.get("http://www.ruderal.com/bullshit/bullshit.htm")

        ruder_bs = []

        for i in range(5):
            time.sleep(0.05)
            self.driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[3]/form/input[2]").click()
            the_bs = self.driver.find_element_by_name("txtTest").get_attribute("value")
            ruder_bs.append(the_bs)

        return ruder_bs

    def dack_scrape(self) ->"list":
        self.driver.get("https://www.dack.com/web/bullshit.html")

        dack_bs = []

        for i in range(5):
            time.sleep(0.05)
            self.driver.find_element_by_xpath("/html/body/table[4]/tbody/tr/td[3]/form/input[2]").click()
            the_bs = self.driver.find_element_by_name("txtTest").get_attribute("value")
            dack_bs.append(the_bs)

        return dack_bs

    def thinkZone_scrape(self) -> "list":
        self.driver.get("https://thinkzone.wlonk.com/Gibber/GibGen.htm")
        self.driver.find_element_by_xpath('//*[@id="form"]/select/option[8]').click()
        self.driver.find_element_by_xpath('//*[@id="form"]/div/div[7]/input').click()

        zone_bs = []
        for i in range(2):
            time.sleep(0.05)
            self.driver.find_element_by_class_name("bigbutton").click()
            the_bs = self.driver.find_element_by_xpath('//*[@id="form"]/textarea[2]').get_attribute("value").split(". ")
            zone_bs.extend(the_bs)

        return zone_bs


    def close_selenium(self):
        self.driver.close()
        self.driver.quit()
