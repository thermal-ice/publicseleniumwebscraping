
import gspread

from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

class googleSheets():
    """
    __init__ contains intialization for API connection with google sheets.
    the "send" methods will update the column of their website.

    Make sure the credential file is creds.json, (or edit the string).

    Google is pretty cool for supporting all these APIs C:
    """

    def __init__(self):
        self.scope = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/spreadsheets","https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
        self.creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", self.scope)

        self.client = gspread.authorize(self.creds)

        self.sheets = self.client.open("jargon_webscrape").sheet1

    def send_WSJ_bs(self,the_bs_list):
        for i in range(2,7):
            self.sheets.update_cell(i,2,the_bs_list[i-2])

    def send_atrix_bs(self,the_bs_list):
        for i in range(2,7):
            self.sheets.update_cell(i,3,the_bs_list[i-2])

    def send_ruderal(self,the_bs_list):
        for i in range(2,7):
            self.sheets.update_cell(i,4,the_bs_list[i-2])

    def send_dack(self,the_bs_list):
        for i in range(2,7):
            self.sheets.update_cell(i,5,the_bs_list[i-2])

    def send_zone(self,the_bs_list):
        for i in range(2,7):
            self.sheets.update_cell(i,6,the_bs_list[i-2])







# data = sheets.get_all_records()
#
# sheetrow = sheets.row_values(3)
# sheet_column = sheets.col_values(2)
# sheet_cell = sheets.cell(2,3).value
#
# insertRow = ["7","Michael", 321312, "Black"]
# #sheets.insert_row(insertRow,3)
# #sheets.delete_row(4)
# sheets.update_cell(2,4,"Changed agin")
#
# print(sheets.row_count)
#
# pprint(sheet_cell)


