from get_categories import get_categories
from get_subcategories import get_subcategories
from get_products import get_products
import json

data = []
categories = get_categories()
for ctgr in categories:
    if ctgr["Name"] == "Vin":
        subcategories = []
        categories = get_subcategories("/vin")

        for ctgr in categories:
            if ctgr["SpotLink"][1:4] == "vin":
                subcategories += get_subcategories(ctgr["SpotLink"])

        # for sbctgr  in subcategories:
        #     data += get_subcategories(sbctgr["SpotLink"])
    else:
        subcategories = get_subcategories(ctgr["SpotLink"])
    for sbctgr in subcategories:
        products = get_products(sbctgr["SpotLink"], ctgr["Name"], sbctgr["Name"])
        data += products
        with open("data.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent = 4, ensure_ascii=False)
    if subcategories == []:
        print("==========non all ================", ctgr["SpotLink"])
        products = get_products(ctgr["SpotLink"], ctgr["Name"], ctgr["Name"])
        data += products
        with open("data.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent = 4, ensure_ascii=False)
    # break
# print(data)