from pyzbar.pyzbar import decode
from PIL import Image
import requests
from bs4 import BeautifulSoup

url = 'https://consumer.oofd.kz/api/tickets/ticket/3af7c85d-4310-4543-b1d8-335538707305'
response = requests.get(url)
bs = BeautifulSoup(response.text, "lxml")
pars = bs.find('body')
if pars:
    print(pars.text)
else:
    print("No matching element found.")