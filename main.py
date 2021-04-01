# WEBSITE WITH PRICE GRAPHIC: https://camelcamelcamel.com/
# THE PRODUCT I WANT: https://www.amazon.com/Sera-Aqua-Test-Aquarium-Test-Kits/dp/B003XJAZDW/ref=sr_1_2?dchild=1&keywords=sera&qid=1617169744&sr=8-2
# MY BROWSER HEADERS: http://myhttpheader.com/


import requests
import lxml
from bs4 import BeautifulSoup
import smtplib

my_email = "justtotestmycode@gmail.com"
password = "privet123456amoremio"

# AMAZON LINK:
url = "https://www.amazon.com/Sera-Aqua-Test-Aquarium-Test-Kits/dp/B003XJAZDW/ref=sr_1_2/?_encoding=UTF8&dchild=1&keywords=sera&qid=1617169744&sr=8-2&ref_=nav_newcust&claim_type=EmailAddress&new_account=1&"


# In addition to the URL, when you browser tries to load up a page in Amazon,
# it also passes a bunch of other information. e.g. Which browser you're using, which
# computer you have etc. These additional pieces of information is passed along in the
# request Headers. You can see your browser headers by going to this website:
# http://myhttpheader.com/

# CREATING A HEADER:
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",
    "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7"
}

# GETTING AMAZON PAGE:
response = requests.get(url, headers=header)


# PARSING OUR PAGE WITH BEAUTIFUL SOUP:
soup = BeautifulSoup(response.content, "lxml")

# FINDING A PRICE FROM PAGE:
price = soup.find(name="span", class_="a-size-medium a-color-price priceBlockBuyingPriceString")
price_text = price.getText()
price_without_currency = price_text.split("$")[1]
float_price = float(price_without_currency)
print(f"The product price is: {float_price}")

# FINDING A PRODUCT NAME:
product = soup.find(name="span", class_="a-size-large product-title-word-break")
product_text = product.getText()
pure_product_text = product_text.split("\n")[8]
print(f"The product you want is: {pure_product_text}")

if float_price < 90:
    message = f"Hey! The product you want: {pure_product_text} has the price {float_price} at Amazon!"
    # CONNECTING TO GMAIL SERVER:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()

        # LOGGING IN:
        connection.login(user=my_email, password=password)

        # SENDING EMAILS:
        # emails without title are often considered as spam. its better create a title - subject.
        connection.sendmail(
            from_addr=my_email,
            to_addrs="laramera@outlook.it",
            msg=f"Subject:Best Price!\n\n{message}"
        )
