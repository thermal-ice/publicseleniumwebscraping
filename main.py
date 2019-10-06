import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import google_sheets
import webscraping


#Calls and intializes the webscraping object from the other file
webscraping_object = webscraping

webscrape_class = webscraping_object.webscraping_class()

#Gets the results of the webscraping
wsj_result = webscrape_class.wsj_scrape()

atrix_result = webscrape_class.atrixnet_scrape()

ruderal_result = webscrape_class.ruderal_scrape()

dack_result = webscrape_class.dack_scrape()

zone_result = webscrape_class.thinkZone_scrape()

#Close the driver
webscrape_class.close_selenium()


#Call the google sheets object (API)

mainTesting = google_sheets

googleSheets = mainTesting.googleSheets()

#Updates the cells in the sheet
googleSheets.send_WSJ_bs(wsj_result)

googleSheets.send_atrix_bs(atrix_result)
googleSheets.send_ruderal(ruderal_result)

googleSheets.send_dack(dack_result)

googleSheets.send_zone(zone_result)





