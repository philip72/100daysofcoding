# kilometers=float(input("enter what u want to convert to miles"))
# kilometersToMiles=0.621371
# miles=kilometersToMiles*kilometersToMiles
# print('%0.2f kilometres is equal to %0.2f miles'%(kilometers,miles))

import requests
from bs4 import BeautifulSoup
url='https://www.jumia.co.ke/mlp-xiaomi-store/'
r=requests.get(url)
print(r.text)

