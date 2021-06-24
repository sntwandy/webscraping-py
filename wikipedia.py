import requests
from lxml import html

headers = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
}

# URL root
url = "https://www.wikipedia.org/"

# Requirements
r = requests.get(url, headers=headers)
# Parse the html response
parser = html.fromstring(r.text)
# Get by id the element using lxml
# english = parser.get_element_by_id('js-link-box-en')

# print(english.text_content())

# Get the text using xpath
languages = parser.xpath("//div[contains(@class, 'central-featured-lang')]//strong/text()")

for language in languages:
    print(language)
# print(languages)
