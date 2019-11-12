from bs4 import BeautifulSoup
import requests

page_source = requests.get('https://www.similarweb.com/website/quora.com')
print(page_source.content)
print(page_source.status_code)

soup = BeautifulSoup(page_source.content, 'html.parser')
# soup_html =list(soup.children)
print(soup.prettify(encoding='UTF-8'))
# print(soup.find_all(class="engagementInfo-valueNumber"))