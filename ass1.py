import base64
import smtplib
import ssl
from email.mime.text import MIMEText
from email.utils import formatdate
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from sendmail import sendmail

def ambil():
    
    my_url = 'https://www.newegg.com/Desktop-Graphics-Cards/SubCategory/ID-48?Tid=7709'
    uclient = uReq(my_url)
    page_html = uclient.read()
    uclient.close()
    page_soup = soup(page_html,"html.parser")

    containers = page_soup.findAll("div", {"class":"item-container"})

    file_name = "assignment1.csv"
    f = open(file_name, "w")

    headers = "brand , shipping , price \n"
    f.write(headers)



    for container in containers:
        brand = container.a.img["title"]

        # title_container = container.findAll("a", {"class":"item-titles"})
        # product_name = title_container[0].text

        shipping_container = container.findAll("li", {"class":"price-ship"})
        shipping = shipping_container[0].text.strip()

        price_list = container.findAll("li", {"class":"price-current"})
        price = price_list[0].text.strip().replace("|","").replace('\r', '').replace('\n', '')


        print("brand : " + brand)
        # print("product_name : " + product_name)
        print("shipping :  " + shipping)
        print("price : " + price)
        print("_____________________________________________________________________________________________________________")


        f.write(brand.replace(",","|") + "," + shipping + "," + price.replace(",",".") + "\n")

    f.close()

def compare(self):
        sendmail()
if __name__ == "__main__":
    ambil()
if __name__ == "__main__":
    sendmail()
