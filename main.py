import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

amazon_item_URL = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
headers = {
    'user_agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
    'accept_language': "en-US,en;q=0.9"
}
target_price = 100.00
USER_EMAIL = "madhavdahal4@gmail.com"
PASSWORD = "atqcouxgdludfkgo"
response = requests.get(amazon_item_URL, headers=headers)
data = response.text
soup = BeautifulSoup(data,'lxml')
content = float(soup.select_one(selector=".a-offscreen").getText().replace('$',''))
title = soup.select_one(selector="#productTitle").getText()
if content < target_price:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=USER_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=USER_EMAIL,
            to_addrs=USER_EMAIL,
            msg=f"Subject: Amazon Price Alert\n\n{title} {amazon_item_URL}".encode("utf-8")
        )
