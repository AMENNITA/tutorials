import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

import requests
from bs4 import BeautifulSoup
from datetime import datetime


def get_sheet():
    """ This method will Authorize the google drive and will fetch the Sheet"""
    SCOPE = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
             "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
    credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', SCOPE)
    gc = gspread.authorize(credentials)
    # Return the First sheet
    return gc.open('price_tracker').sheet1


def get_sheet_df():
    SCOPE = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
             "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
    credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', SCOPE)
    gc = gspread.authorize(credentials)
    # Save the data into data frame

    sheet_values = gc.open('price_tracker').sheet1.get_all_values()
    # price_df = pd.DataFrame(sheet_values, columns=sheet_values.pop(0))
    # return price_df
    return None


def get_amazon_price(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/76.0.3809.132 Safari/537.36"}
    # Get the Page value
    page_content = requests.get(url=url, headers=headers).content
    soup = BeautifulSoup(page_content, 'html.parser')
    soup.prettify()
    # Find the Item and Price
    # item = soup.find(id="productTitle").get_text()
    # price = soup.find(id="priceblock_ourprice")
    # print(item)
    # print(price)
    pprint(soup)


def get_myntra_price(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/76.0.3809.132 Safari/537.36"}
    # Get the Page value
    page_content = requests.get(url, headers).text
    soup = BeautifulSoup(page_content, 'html.parser')
    soup.prettify()
    # print(soup)
    block = soup.findAll('script', {'type': 'application/ld+json'})[1]
    # Import json and extract the values
    import json
    json_value = json.loads(block.text)
    item = json_value["name"]
    price = json_value["offers"]["price"]
    brand = json_value["brand"]["name"]

    print("Item : {} and its Price {}".format(item, price))
    return item, int(price), brand


price_tracker = get_sheet()
print("No. of rows in the sheet {}".format(len(price_tracker.get_all_records())))


# Loop over each row and open the link
def send_notification(email):
    if email is not None:
        print("Notification sent successfully")


for i, row in enumerate(price_tracker.get_all_records()):
    # pprint(row)
    if i == 0:
        continue  # Skip the Header row
    row_num = i + 2  # Add two, one for Header and then for Index
    item_link = row['Item Link']
    orignal_price = int(row['Orignal Price'])
    desired_price = int(row['Desired Price'])
    item_name = checked_price = item_brand = ""
    if "myntra" in item_link:
        item_name, checked_price, item_brand = get_myntra_price(item_link)
    elif "amazon" in item_link:
        None
        # get_amazon_price('https://www.amazon.in/gp/product/B078QCWYL7/ref=ox_sc_act_title_2?smid=A1Q5BOZOQ6TZM0&psc=1')
    else:
        exit(0)
    # Update the Last checked details
    now = datetime.today().strftime("%d-%b-%Y %I:%M %p")
    price_tracker.update_cell(row_num, 4, item_name)
    price_tracker.update_cell(row_num, 5, checked_price)
    price_tracker.update_cell(row_num, 6, now)
    print("Updated Row {} successfully.".format(row_num))
    # Send notification if current price is less than the desired price
    if checked_price <= desired_price:
        send_notification(row['Notification Email'])
