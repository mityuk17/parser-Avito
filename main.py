import requests
from bs4 import BeautifulSoup


#proxie = {
#   "https": "https",
#    "http": "http",
#    "username": "username",
#    "password": "password"
#}

id = "id"
url = 'https://www.avito.ru/'+ id
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
#ad_www
ad_www = soup.find("link")
ad_www = (ad_www["href"])
#ad_price
ad_price = soup.find("span", class_ = "js-item-price")
ad_price = ad_price["content"]
#ad_name
ad_name = soup.find("span", class_ ="title-info-title-text").text
#ad_date_registration_human
ad_date_registration_human = soup.find("div", class_ = "title-info-metadata-item-redesign").text.strip()
#user_reviews
try:
    user_reviews = soup.find("span", class_ = "seller-info-rating-score").text.strip()
except AttributeError:
    user_reviews = None
#user_date_registr_human
user_info = soup.find_all("div", class_ = "seller-info-value")
user_date_registr_human = user_info[1].text.strip().split()
if len(user_date_registr_human) > 5:
    user_date_registr_human = " ".join(user_date_registr_human[:5])
else:
    user_date_registr_human = " ".join(user_date_registr_human)
#user_name
user_name = user_info[0].text
user_name = user_name.split()[0].strip()
#ad_views
ad_views = soup.find("div", class_ = "title-info-metadata-item title-info-metadata-views")
ad_views = ad_views.text.split()[0]
#ad_region
ad_region = soup.find("span", class_ = "item-address__string").text.strip()
#user_active
user_active = soup.find("div", class_ = "js-favorite-seller-buttons seller-info-favorite-seller-buttons")
user_active = user_active["data-props"].split(",")[3].split(":")[1].strip("\"").split()
try:
    user_active = user_active[0]
except IndexError:
    user_active = None
# user_type
user_type = soup.find_all("script")
for i in user_type:
    if str(i).startswith("<script>"):
        q = user_type.index(i)
        break
user_type = (user_type[q].text.split(":"))
isCompany = user_type[660].split(",")[0]
isShop = user_type[661].split(",")[0]
if isCompany == "true":
    user_type = "company"
elif isShop == "true":
    user_type = "shop"
else:
    user_type = "person"
#categories
category = soup.find_all("script")
category = (category[q].text.split(":"))
ad_category_1 = category[4].split(",")[0]
ad_category_2 = category[5].split(",")[0]

#seller_hash
seller_hash = id

dict = {'seller_hash': seller_hash,
'ad_views': ad_views,
'ad_www':ad_www,
'ad_region':ad_region,
'ad_name':ad_name,
'ad_date_registration_human':ad_date_registration_human,
'ad_price':ad_price,
'ad_category_1':ad_category_1,
'ad_category_2':ad_category_2,
'user_type':user_type,
'user_name':user_name,
'user_date_registr_human':user_date_registr_human,
'user_reviews':user_reviews,
'user_active':user_active,
        }

print(dict)