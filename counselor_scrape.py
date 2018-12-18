import requests
import urllib

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3"}
url = "https://www.iecaonline.com/quick-links/member-directory/"

counselor_directory = requests.get(url=url, headers=headers).text
# print(counselor_directory)