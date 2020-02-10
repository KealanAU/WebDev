import requests, re
from PIL import Image
from bs4 import BeautifulSoup as BS

reg_match = "(https:\/\/manofmany\.com\/wp-content\/uploads\/\d{4}\/\d{2}\/Ranked-The-Top-20-Australian-Ice-Creams-of-All-Time-)([\w-]+)(\.jpg)"
ice_cream_link = 'https://manofmany.com/lifestyle/food/ranked-the-top-20-australian-ice-creams-of-all-time'

r =  requests.get(ice_cream_link)

if r.ok: 
    soup = BS(r.content, 'html.parser')

img_links = soup.find_all('img')

for i in img_links:
    url = i.get('src')
    if url[-3:] == "jpg":
        matched_reg = re.match(reg_match,url)
        if matched_reg :
            file_name = matched_reg.group(2)
            file_path = f'./src/assets/img/{file_name}.jpg'

            with open(file_path, "wb") as f:
                f.write(requests.get(url, stream=True).content)