import requests
import json


def get_categories():

    # The target URL to make a GET request
    url = 'https://www.nemlig.com/dagligvarer/drikkevarer?GetAsJson=1'

    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        print('Success!')
        # Access the response content or the JSON content of the response
        content = response.content
        json_data = response.json()
        detailed_categories = json_data["content"][1]["SubElements"]

        categories = []

        for entry in detailed_categories:
            categories.append({"Name": entry["Name"], "SpotLink": entry["SpotLink"]["Url"]})

        
        
        return categories
    else:
        print('An error has occurred. Status Code:', response.status_code)

        return []

# categories = get_categories()
# with open("categories.json", "w") as f:
#     json.dump(categories, f)