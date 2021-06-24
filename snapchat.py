import requests
from bs4 import BeautifulSoup

# Header
headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'
}

# URL
url = 'https://newsroom.snap.com/'

# Make the Request
r = requests.get(url, headers=headers)

# Parse the html tree
parser = BeautifulSoup(r.text)

# Find the container element
news_container = parser.find_all('div', class_='PostsSlice__Post-dgtynh-1')

# Extract the information
for new_container in news_container:
    job_title_element = new_container.find('h3')
    job_title = job_title_element.find('a').text
    print(job_title)
