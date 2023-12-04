import http.client
import requests

payload = ''
headers = {
    "sec-ch-ua": "\"Google Chrome\";v=\"119\", \"Chromium\";v=\"119\", \"Not?A_Brand\";v=\"24\"",
    "version": "4.0.1",
    "x-correlation-id": "69a54c99-f20d-4992-9f10-ae011eb12c00",
    "x-xsrf-token": "45cBDmqgM93guddORnZzmLOrXq033KV6qiYYYpsUIIRBnU9wsjQVUDHxJbvvKAkU0ohGdyT43gKteCxTmK48DTUPUZY1",
    "device-size": "desktop",
    "sec-ch-ua-mobile": "?0",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "accept": "application/json, text/plain, */*",
    "x-queueit-ajaxpageurl": "https%3A%2F%2Fwww.nemlig.com%2Fdagligvarer%2Fdrikkevarer%2Fsodavand%2Fcola",
    "platform": "web",
    "sec-ch-ua-platform": "\"Linux\"",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://www.nemlig.com/dagligvarer/drikkevarer/sodavand/cola",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q=0.9",
    # "cookie": "ASP.NET_SessionId=ytavz32htjk3gpgi34p1fhqw; SC_ANALYTICS_GLOBAL_COOKIE=3e30e9a4576a4bb999ab485baacb95fe|False; IVCookieBasketKey=IVCookieBasketKey=c67ba4f4-8d38-4e66-87cf-26e5fb99e42d; IVCookieBasketKeyId=IVCookieBasketKeyId=966925767; ABTastySession=mrasn=&lp=https%253A%252F%252Fwww.nemlig.com%252Fdagligvarer%252Fdrikkevarer%252Fsodavand%252Fcola; ABTasty=uid=x949tavk44ht5ym6&fst=1701461164538&pst=-1&cst=1701461164538&ns=1&pvt=1&pvis=1&th=1114996.1382060.1.1.1.1.1701461165184.1701461165184.1.1; XSRF-TOKEN=45cBDmqgM93guddORnZzmLOrXq033KV6qiYYYpsUIIRBnU9wsjQVUDHxJbvvKAkU0ohGdyT43gKteCxTmK48DTUPUZY1; XSRF-COOKIE-TOKEN=Ks9DTu5dj9gbQos3EgdMNVhW2Sp4P0mZCzk_S_Ta0pZwblnzHMDluDH2r39Z2bRVrhqb8RiIrXwRDvl0JR4KWLvrhq01; QueueITAccepted-SDFrts345E-V3_nemligprod=EventId%3Dnemligprod%26QueueId%3D73a70efc-3e13-467a-91ad-5207a47855e1%26RedirectType%3Dsafetynet%26IssueTime%3D1701461168%26Hash%3Dc98773569a9d731d99cc916c475f5876cdac8a3a47aeca34af3a703d7413f913"
}
# The target URL to make a GET request
url = f"http://www.nemlig.com/webapi/AAAAAAAA-ECCEIIHy/2023120109-120-600/1/0/Products/GetByProductGroupId?productGroupId=c94e4901-7f80-4e59-99a9-20de9ae41a3e"

# Send a GET request to the URL
response = requests.get(url, headers= headers)

# Check if the request was successful
if response.status_code == 200:
    print('Success!')
    # Access the response content or the JSON content of the response
    content = response.content
    json_data = response.json()
    print(json_data)