import os
import requests
from bs4 import BeautifulSoup
import smtplib
BUY_PRICE = 120.00
AMAZON_URL = "https://www.amazon.com/Yankee-Candle-Scented-Consistent-Fragrance/dp/B0F3DPXQP1?ref=dlx_deals_dg_dcl_B0F3DPXQP1_dt_sl14_c8_pi&pf_rd_r=AQ4KXHD5YRMYWC7K2D3R&pf_rd_p=7d7fd1a0-40b8-487f-8db9-b2480f2cfbc8"
header = {
    "Accept-Language": "pl,en-US;q=0.9,en;q=0.8,ru;q=0.7,de;q=0.6",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 OPR/122.0.0.0"
}
response = requests.get(AMAZON_URL, headers=header)
response.raise_for_status()
webpage = response.text
soup = BeautifulSoup(webpage, "html.parser")

item_name = soup.find(name="span", id="productTitle").getText()  # type: ignore
price_whole = soup.find(
    name="span", class_="a-price-whole").getText()  # type: ignore
price_fraction = soup.find(
    name="span", class_="a-price-fraction").getText()  # type: ignore

price = float(price_whole.replace(",", "") + price_fraction)

if price < BUY_PRICE:

    password = str(os.getenv("SMTP"))
    my_email = str(os.getenv("MYEMAIL"))
    to_mail = "tarkoving122@gmail.com"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=to_mail,
            msg=f"Subject:Amazon Price Alert!\n\n{item_name} is now {price} PLN!\n{AMAZON_URL}".encode
            (
                "utf-8"
            )
        )
else:
    print(f"The price is still too high: {price} PLN")
