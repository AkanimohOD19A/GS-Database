# CONNECT TO GOOGLE SHEET
## Import Dependencies
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

## Connect to Google Sheet
scope = ['https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials. \
    from_json_keyfile_name("gs_credentials.json", scope)
client = gspread.authorize(credentials)

## Create a new g/sheet
sheet = client.create("NewDatabase")
# => share sheet with our origin account
sheet.share('danielamahtoday@gmail.com', perm_type='user', role='writer')

## Open the spreadsheet and upload data
## - Nu Data
df = pd.DataFrame(
    {
        'Header1': [1, 2, 3, 4, 5],
        'Header2': [6, 7, 8, 9, 10],
        'Header3': ["a", "b", "c", "d", "e"],
        'Header4': ["i", "came", "saw", "and", "conquered"]
    }
)

df.to_csv("nu-df.csv")

## - Open sheet
sheet = client.open("NewDatabase").sheet1
## - Read csv
df = pd.read_csv('nu-df.csv')
## - Export csv to sheet
sheet.update([df.columns.values.tolist()] + df.values.tolist())
