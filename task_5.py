# Task 5

# Use the BeautifulSoup and requests Python packages to print out a list of all the news titles on the https://news.ycombinator.com/.
import requests
from bs4 import BeautifulSoup

url = 'https://news.ycombinator.com/'

titles_list = []

def scrape_url(url, page_range):
    for page in range(1, page_range+1):
        page_url = url+'news?p={0}'.format(page)
        page = requests.get(page_url).content
        soup = BeautifulSoup(page, 'html.parser')
        titles = soup.find_all('a', class_ = 'storylink')
        for title in titles:
            titles_list.append(title.text)
    
    return titles_list

print('Scraping....')
result = scrape_url(url, 15)
print(result)
print(len(result))


'''
page_1 = scrape_url(url=url+'news?p=1')
print(page_1[-1])

page_2 = scrape_url(url+'news?p=2')
print(page_2[-1])

scrape_url(url)
print(len(titles_list))
for page in range(1,4):
    
    scrape_url(page_url)

print(titles_list)


soup = BeautifulSoup(page.content, 'html.parser')

titles = soup.find_all('a', class_ = 'storylink')

for page in range(1, 16):
    page_url = url+'news?p={0}'.format(page)'''