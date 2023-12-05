import requests
import json
from selenium.webdriver.chrome.options import Options
from seleniumwire import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

def get_product_groups(subcategorylink):

    # The target URL to make a GET request
    subcategorylink = subcategorylink.split("#")[0]
    if subcategorylink[:5] == "https":
        url = f"{subcategorylink}?GetAsJson=1"
    else:
        url = f"https://www.nemlig.com{subcategorylink}?GetAsJson=1"

    # Send a GET request to the URL
    print(url)
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Access the response content or the JSON content of the response
        content = response.content
        json_data = response.json()
        detailed_productgroups = json_data["content"]

        productgroups = []

        for entry in detailed_productgroups:
            if entry["TemplateName"] == "productlistshowallspot":
                productgroups.append(entry["ProductGroupId"])
        
        return productgroups
    else:
        print('An error has occurred. Status Code:', response.status_code)

        return []

def get_products_byid(subcategorylink, productgroupid, ctgr, sbctgr):

    # The target URL to make a GET request
    url = f"http://www.nemlig.com/webapi/AAAAAAAA-ECCEIIHy/*/1/0/Products/GetByProductGroupId?productGroupId={productgroupid}"


    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'referer': f'https://www.nemlig.com{subcategorylink}',
    }

    # Send a GET request to the URL
    response = requests.post(url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        # Access the response content or the JSON content of the response
        content = response.content
        json_data = response.json()
        detailed_products = json_data["Products"]

        products = []

        for entry in detailed_products:
            prdt = {
                "Category": ctgr,
                "SubCategroy": sbctgr,
                "Name": entry["Name"],
                "Url": "https://www.nemlig.com/" + entry["Url"],
                "Description": entry["Description"],
                "Price": entry["Price"],
                "PrimaryImage": entry["PrimaryImage"],
            }
            products.append(prdt)
        
        return products
    else:
        print('An error has occurred. Status Code:', response.status_code)

        return []


def get_products(subcategory, ctgr, sbctgr):
    print(ctgr, sbctgr)
    productgroups = get_product_groups(subcategory)
    products = []
    for gid  in productgroups:
        products += get_products_byid(subcategory, gid, ctgr, sbctgr)
    
    return products


# products = get_sprdt("/dagligvarer/drikkevarer/sodavand/cola")


# subcategory = "/dagligvarer/drikkevarer/sodavand/cola"

# products = get_products(subcategory)
# with open("products.json", "w", encoding="utf-8") as f:
#     json.dump(products, f, indent = 4, ensure_ascii=False)

