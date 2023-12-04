import requests
import json


def get_subcategories(categorylink):

    # The target URL to make a GET request
    url = f"https://www.nemlig.com{categorylink}?GetAsJson=1"

    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        print(categorylink)
        # Access the response content or the JSON content of the response
        content = response.content
        json_data = response.json()

        
        subcategories = []

        
            

        for entry in json_data["content"]:
            if entry["TemplateName"] == "productlistonerowspot":
                if "SeeMoreLink" in entry:
                    subcategories.append({"Name": entry["Heading"], "SpotLink": entry["SeeMoreLink"]["Url"]})


        return subcategories
    else:
        print('An error has occurred. Status Code:', response.status_code)

        return []

# data = []
# subcategories = []
# categories = get_subcategories("/vin")

# for ctgr in categories:
#     if ctgr["SpotLink"][1:4] == "vin":
#         subcategories += get_subcategories(ctgr["SpotLink"])

# # for sbctgr  in subcategories:
# #     data += get_subcategories(sbctgr["SpotLink"])

# with open("sub_categories.json", "w") as f:
#     json.dump(subcategories, f)